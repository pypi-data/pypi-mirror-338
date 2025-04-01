from typing import Union

import numpy as np
import parselmouth

class DiscConfig:
    """Discriminator configurations.
    """
    def __init__(self):
        self.tmp=1
        # self.periods = [2, 3, 5, 7, 11]
        # self.channels = [32, 128, 512, 1024]
        # self.kernels = 5
        # self.strides = 3
        # self.postkernels = 3
        # self.leak = 0.1

class ModelConfig:
    """NANSY++ configurations.
    """
    def __init__(self):
        self.tmp=1
        self.sr = 16000

        # # unknown all STFT hyperparameters
        # self.mel = 80
        # self.mel_hop = 256
        # self.mel_win = 1024
        self.mel_win_fn = 'hann'
        self.mel_windows = 1024
        self.mel_strides = 160
        # self.mel_fmin = 0
        # self.mel_fmax = 8000

        # # unknown
        # # , default negative-slope of nn.LeakyReLU
        # self.leak = 0.01
        # # , default dropout rate of nn.Transformer
        # self.dropout = 0.1

        # # Wav2Vec2Wrapper
        # self.w2v2_name = 'facebook/wav2vec2-large-xlsr-53'
        # self.w2v2_lin = 15

        # # FrameLevelSynthesizer
        # self.frame_kernels = 3
        # self.frame_dilations = [1, 3, 9, 27, 1, 3, 9, 27]
        # self.frame_blocks = 2

        # # LinguisticEncoder
        # self.ling_hiddens = 128
        # self.ling_preconv = 2
        # self.ling_kernels = [3] * 8 + [1] * 2

        # # ConstantQTransform
        # self.cqt_hop = 256
        # self.cqt_fmin = 32.7
        # # self.cqt_fmax = 8000
        # self.cqt_bins = 191
        # self.cqt_bins_per_octave = 24

        # # PitchEncoder
        # self.pitch_freq = 160
        # self.pitch_prekernels = 7
        # self.pitch_kernels = 3
        # self.pitch_channels = 128
        # self.pitch_blocks = 2
        # # unknown
        # self.pitch_gru = 256
        # # unknown
        # self.pitch_hiddens = 256
        # self.pitch_f0_bins = 64
        # self.pitch_start = 50  # hz
        # self.pitch_end = 1000

        # # Synthesizer
        # self.synth_channels = 64
        # self.synth_kernels = 3
        # self.synth_dilation_rate = 2
        # self.synth_layers = 10
        # self.synth_cycles = 3

        # # TimberEncoder
        # self.timb_global = 192
        # self.timb_channels = 512
        # self.timb_prekernels = 5
        # self.timb_scale = 8
        # self.timb_kernels = 3
        # self.timb_dilations = [2, 3, 4]
        # self.timb_bottleneck = 128
        # # NANSY++: 3072
        # self.timb_hiddens = 1536
        # self.timb_latent = 512
        # self.timb_timber = 128
        # self.timb_tokens = 50
        # # unknown
        # self.timb_heads = 8
        # # unknown
        # self.timb_slerp = 0.5

class DataConfig:
    """Configuration for dataset construction.
    """
    def __init__(self, batch):
        """Initializer.
        Args:
            batch: size of the batch.
                if None is provided, single datum will be returned.
        """
        # audio config
        self.sr = 16000

        # # stft
        # self.fft = 1024
        self.hop = 160
        # self.win = self.fft
        # self.win_fn = 'hann'

        # # mel-scale filter bank
        # self.mel = 80
        # self.fmin = 0
        # self.fmax = 8000

        # # for preventing log-underflow
        # self.eps = 1e-5

        # # sample size
        # self.batch = batch

class TrainConfig:
    """Configuration for training loop.
    """
    def __init__(self, sr: int, hop: int):
        """Initializer.
        Args:
            sr: sample rate.
            hop: stft hop length.
        """

        # # augment
        # self.num_code = 32
        self.formant_shift = 1.4
        self.pitch_shift = 2.
        self.pitch_range = 1.5
        self.cutoff_lowpass = 60
        self.cutoff_highpass = 7000
        self.q_min = 2
        self.q_max = 5
        self.num_peak = 8
        self.g_min = -12
        self.g_max = 12
        # # pitch consistency
        # self.cqt_shift_min = -12
        # self.cqt_shift_max = 12
        # # linguistic informations
        # self.kappa = 0.1

        # # objective
        # # 16khz sr, default win=[1920, 320, 80], hop=[640, 80, 40] in NSF
        # self.wins = [2048, 512, 128]
        # self.hops = [512, 128, 32]


class Config:
    """Integrated configuration.
    """
    def __init__(self):
        self.data = DataConfig(batch=None)
        self.train = TrainConfig(self.data.sr, self.data.hop)
        self.model = ModelConfig()
        self.disc = DiscConfig()

    def validate(self):
        assert self.data.sr == self.model.sr, \
            'inconsistent data and model settings'

    def dump(self):
        """Dump configurations into serializable dictionary.
        """
        return {k: vars(v) for k, v in vars(self).items()}

    @staticmethod
    def load(dump_):
        """Load dumped configurations into new configuration.
        """
        conf = Config()
        for k, v in dump_.items():
            if hasattr(conf, k):
                obj = getattr(conf, k)
                load_state(obj, v)
        return conf

def load_state(obj, dump_):
    """Load dictionary items to attributes.
    """
    for k, v in dump_.items():
        if hasattr(obj, k):
            setattr(obj, k, v)
    return obj

class PraatAugment:
    """Praat based augmentation.
    """
    def __init__(self,
                 config: Config,
                 pitch_steps: float = 0.01,
                 pitch_floor: float = 75,
                 pitch_ceil: float = 600):
        """Initializer.
        Args:
            config: configurations.
            pitch_steps: pitch measurement intervals.
            pitch_floor: minimum pitch.
            pitch_ceil: maximum pitch.
        """
        self.config = config
        self.pitch_steps = pitch_steps
        self.pitch_floor = pitch_floor
        self.pitch_ceil = pitch_ceil

    def augment(self,
                snd: Union[parselmouth.Sound, np.ndarray],
                formant_shift: float = 1.,
                pitch_shift: float = 1.,
                pitch_range: float = 1.,
                duration_factor: float = 1.) -> np.ndarray:
        """Augment the sound signal with praat.
        """
        if not isinstance(snd, parselmouth.Sound):
            snd = parselmouth.Sound(snd, sampling_frequency=self.config.model.sr)
        pitch = parselmouth.praat.call(
            snd, 'To Pitch', self.pitch_steps, self.pitch_floor, self.pitch_ceil)
        ndpit = pitch.selected_array['frequency']
        # if all unvoiced
        nonzero = ndpit > 1e-5
        if nonzero.sum() == 0:
            return snd.values[0]
        # if voiced
        median, minp = np.median(ndpit[nonzero]).item(), ndpit[nonzero].min().item()
        # scale
        updated = median * pitch_shift
        scaled = updated + (minp * pitch_shift - updated) * pitch_range
        # for preventing infinite loop of `Change gender`
        # ref:https://github.com/praat/praat/issues/1926
        if scaled < 0.:
            pitch_range = 1.
        out, = parselmouth.praat.call(
            (snd, pitch), 'Change gender',
            formant_shift,
            median * pitch_shift,
            pitch_range,
            duration_factor).values
        return out