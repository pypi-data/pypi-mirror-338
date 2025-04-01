from typing import Optional

import numpy as np
import torch
import torch.nn as nn

from peq import ParametricEqualizer
from praat import PraatAugment, Config


class Augment(nn.Module):
    """Waveform augmentation.
    """
    def __init__(self, config: Config):
        """Initializer.
        Args:
            config: Nansy configurations.
        """
        super().__init__()
        self.config = config
        self.praat = PraatAugment(config)
        self.peq = ParametricEqualizer(
            config.model.sr, config.model.mel_windows)
        self.register_buffer(
            'window',
            torch.hann_window(config.model.mel_windows),
            persistent=False)
        f_min, f_max, peaks = \
            config.train.cutoff_lowpass, \
            config.train.cutoff_highpass, config.train.num_peak
        # peaks except frequency min and max
        self.register_buffer(
            'peak_centers',
            f_min * (f_max / f_min) ** (torch.arange(peaks + 2)[1:-1] / (peaks + 1)),
            persistent=False)

    def forward(self,
                wavs: torch.Tensor,
                pitch_shift: Optional[torch.Tensor] = None,
                pitch_range: Optional[torch.Tensor] = None,
                formant_shift: Optional[torch.Tensor] = None,
                quality_power: Optional[torch.Tensor] = None,
                gain: Optional[torch.Tensor] = None) -> torch.Tensor:
        """Augment the audio signal, random pitch, formant shift and PEQ.
        Args:
            wavs: [torch.float32; [B, T]], audio signal.
            pitch_shift: [torch.float32; [B]], pitch shifts.
            pitch_range: [torch.float32; [B]], pitch ranges.
            formant_shift: [torch.float32; [B]], formant shifts.
            quality_power: [torch.float32; [B, num_peak + 2]],
                exponents of quality factor, for PEQ.
            gain: [torch.float32; [B, num_peak + 2]], gain in decibel.
        Returns:
            [torch.float32; [B, T]], augmented.
        """
        # B
        bsize, _ = wavs.shape
        # [B, F, T / S], complex64
        fft = torch.stft(
            wavs,
            self.config.model.mel_windows,
            self.config.model.mel_strides,
            self.config.model.mel_windows,
            self.window,
            return_complex=True)
        # PEQ
        if quality_power is not None:
            # alias
            q_min, q_max = self.config.train.q_min, self.config.train.q_max
            # [B, num_peak + 2]
            q = q_min * (q_max / q_min) ** quality_power
            if gain is None:
                # [B, num_peak]
                gain = torch.zeros_like(q[:, :-2])
            # [B, num_peak]
            center = self.peak_centers[None].repeat(bsize, 1)
            # [B, F]
            peaks = torch.prod(
                self.peq.peaking_equalizer(center, gain[:, :-2], q[:, :-2]), dim=1)
            # [B, F]
            lowpass = self.peq.low_shelving(
                self.config.train.cutoff_lowpass, gain[:, -2], q[:, -2])
            highpass = self.peq.high_shelving(
                self.config.train.cutoff_highpass, gain[:, -1], q[:, -1])
            # [B, F]
            filters = peaks * highpass * lowpass
            # [B, F, T / S]
            fft = fft * filters[..., None]
        # [B, T]
        out = torch.istft(
            fft,
            self.config.model.mel_windows,
            self.config.model.mel_strides,
            self.config.model.mel_windows,
            self.window).clamp(-1., 1.)
        # max value normalization
        out = out / out.abs().amax(dim=-1, keepdim=True).clamp_min(1e-7)
        if formant_shift is None and pitch_shift is None and pitch_range is None:
            return out
        # praat-based augmentation
        if formant_shift is None:
            formant_shift = torch.ones(bsize)
        if pitch_shift is None:
            pitch_shift = torch.ones(bsize)
        if pitch_range is None:
            pitch_range = torch.ones(bsize)
        out = torch.tensor(
            np.stack([
                self.praat.augment(o, fs.item(), ps.item(), pr.item())
                for o, fs, ps, pr in zip(
                    out.cpu().numpy(),
                    formant_shift.cpu().numpy(),
                    pitch_shift.cpu().numpy(),
                    pitch_range.cpu().numpy())], axis=0),
            device=out.device, dtype=torch.float32)
        return out


    def sample_like(self, signal) :
            """Sample augmentation parameters.
            Args:
                signal: [torch.float32; [B, T]], speech signal.
            Returns:
                augmentation parameters.
            """
            # [B]
            bsize, _ = signal.shape
            def sampler(ratio):
                shifts = torch.rand(bsize, device=signal.device) * (ratio - 1.) + 1.
                # flip
                flip = torch.rand(bsize) < 0.5
                shifts[flip] = shifts[flip] ** -1
                return shifts
            # sample shifts
            fs = sampler(self.config.train.formant_shift)
            ps = sampler(self.config.train.pitch_shift)
            pr = sampler(self.config.train.pitch_range)
            # parametric equalizer
            peaks = self.config.train.num_peak
            # quality factor
            power = torch.rand(bsize, peaks + 2, device=signal.device)
            # gains
            g_min, g_max = self.config.train.g_min, self.config.train.g_max
            gain = torch.rand(bsize, peaks + 2, device=signal.device) * (g_max - g_min) + g_min
            return fs, ps, pr, power, gain

if __name__ == '__main__':
    import torchaudio
    wav, sr = torchaudio.load('/home/work_nfs15/asr_data/data/test_sets_format_3000/chat/origin_wav/102005088.mp3.wav')
    print(wav.shape)
    config = Config()
    model = Augment(config)
    fshift, pshift, prange, power, gain = model.sample_like(wav)
    out = model.forward(wav, pshift, prange, fshift, power, gain)
    nan = out.isnan().any(dim=-1)
    print(nan.all())
    torchaudio.save('1.wav', out, 16000)