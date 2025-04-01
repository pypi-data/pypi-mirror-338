from __future__ import absolute_import, division, print_function, unicode_literals

import glob
import os
import numpy as np
import argparse
import json
import torch
from tqdm import tqdm
from time import time
from utils import AttrDict
from models import Generator
import soundfile as sf
from scipy.interpolate import interp1d

h = None
device = None


def load_checkpoint(filepath, device):
    assert os.path.isfile(filepath)
    print("Loading '{}'".format(filepath))
    checkpoint_dict = torch.load(filepath, map_location=device)
    print("Complete.")
    return checkpoint_dict


def scan_checkpoint(cp_dir, prefix):
    pattern = os.path.join(cp_dir, prefix + '*')
    cp_list = glob.glob(pattern)
    if len(cp_list) == 0:
        return ''
    return sorted(cp_list)[-1]


def process_data(wavlm_file):
    wavlm = np.load(wavlm_file)
    return torch.from_numpy(wavlm).unsqueeze(0)


def inference(a):
    generator = Generator(h).to(device)

    state_dict_g = load_checkpoint(a.checkpoint_file, device)
    generator.load_state_dict(state_dict_g['generator'])

    filelist = os.listdir(a.input)
    os.makedirs(a.output, exist_ok=True)

    generator.eval()
    generator.remove_weight_norm()
    rtfs = []


    print(generator)
    # exit()
    with torch.no_grad():
        for i, filename in tqdm(enumerate(filelist)):
            start = time()
            wavlm_feature = process_data(os.path.join(a.input, filename))
            wavlm_feature = wavlm_feature.to(device)
            y_g_hat = generator(wavlm_feature)
            audio = y_g_hat.squeeze()
            rtf = (time() - start) / (audio.size(-1) / h.sampling_rate)
            rtfs.append(rtf)
            audio = audio.cpu().numpy()

            output_file = os.path.join(a.output, os.path.splitext(filename)[0] + '.wav')
            sf.write(output_file, audio, h.sampling_rate)
            print(output_file, f"\tRTF: {rtf:.4f}")
    print(f"Avg RTF: {sum(rtfs) / len(rtfs):.6f}")


def main():
    print('Initializing Inference Process..')

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='test_mel_files')
    parser.add_argument('--output', default='generated_files_from_mel')
    parser.add_argument('--checkpoint_file',
                        default="/home/work_nfs7/ypjiang/code/knn-hifigan/logs/wavlm_24k/g_00480000.pt")
    a = parser.parse_args()

    config_file = os.path.join(os.path.split(a.checkpoint_file)[0], 'config.json')
    with open(config_file) as f:
        data = f.read()

    global h
    json_config = json.loads(data)
    h = AttrDict(json_config)

    torch.manual_seed(h.seed)
    global device
    if torch.cuda.is_available():
        torch.cuda.manual_seed(h.seed)
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')

    inference(a)


if __name__ == '__main__':
    main()

