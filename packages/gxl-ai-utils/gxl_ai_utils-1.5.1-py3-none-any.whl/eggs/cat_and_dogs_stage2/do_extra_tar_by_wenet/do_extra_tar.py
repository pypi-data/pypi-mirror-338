import os
import shutil

import torch
import torchaudio
import yaml
from gxl_ai_utils.utils import utils_file
from torch.utils.data import DataLoader

from wenet.dataset.dataset import Dataset
config_dict = yaml.load(open("train.yaml", "r"), Loader=yaml.FullLoader)
dataset_conf = config_dict['dataset_conf']

test_dataset = Dataset("shard",
                       "/mnt/sfs/asr/update_data/asr_chat_wenetspeech_enhance_2025-1-24/shards_list.txt",
                       # "./tmp.list",
                       {},
                       None,
                       dataset_conf,
                       partition=False)

test_data_loader = DataLoader(test_dataset, batch_size=1, num_workers=10)

time_now = utils_file.do_get_now_time()
output_dir = "/mnt/sfs/asr/update_data/raw_data/asr_chat_znlin_2025-1-24"
utils_file.makedir(output_dir)
utils_file.makedir(f'{output_dir}/wav')
text_scp_path = os.path.join(output_dir, "text.scp")
text_f = open(text_scp_path, 'w', encoding='utf-8')
wav_scp_path = os.path.join(output_dir, "wav.scp")
wav_f = open(wav_scp_path, 'w', encoding='utf-8')

for i, batch in enumerate(test_data_loader):
    sorted_key, sorted_txt, sorted_wav = batch
    sorted_key = [k[0] for k in sorted_key]
    sorted_txt = [t[0] for t in sorted_txt]
    sorted_wav = [w[0] for w in sorted_wav]
    print(f'i: {i}')
    for key, txt, wav in zip(sorted_key, sorted_txt, sorted_wav):
        text_f.write(f'{key}\t{txt}\n')
        wav_path = os.path.join(f'{output_dir}/wav', f'{key}.wav')
        # torchaudio.save(wav_path, wav, 16000)
        with open(wav_path, "wb") as wav_file:
            wav_file.write(wav)
        wav_f.write(f'{key}\t{wav_path}\n')
        if i % 10000 == 0:
            text_f.flush()
            wav_f.flush()
time_elapsed = utils_file.do_get_elapsed_time(time_now)
print(f'time_elapsed: {time_elapsed}')