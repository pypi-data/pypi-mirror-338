import os.path
import random
import sys
sys.path.insert(0, '../../../')
from gxl_ai_utils.utils import utils_file

def split_file(input_file, num_parts):
    # utils_file.makedir_sil(output_dir)
    with open(input_file, 'rb') as f:
        f.seek(0, 2)  # 将文件指针移动到文件末尾
        file_size = f.tell()  # 获取文件大小
        chunk_size = file_size // num_parts  # 计算每一份的大小
        utils_file.logging_limit_print(f'chunk_size:{chunk_size}')
        f.seek(0)  # 将文件指针移回文件开头
        for i in range(num_parts):
            part_file = f"{input_file}_{i}.gxl_part"
            utils_file.logging_limit_print(f'part_file:{part_file}')
            with open(part_file, 'wb') as part:
                if i == num_parts - 1:  # 最后一部分可能会大一些，处理文件大小不能整除的情况
                    data = f.read()
                else:
                    data = f.read(chunk_size)
                part.write(data)


def combine_files(input_file, old_input_file, num_parts):
    output_file = input_file
    with open(output_file, 'wb') as out:
        for i in range(num_parts):
            part_file = f"{old_input_file}_{i}.gxl_part"
            print(part_file)
            with open(part_file, 'rb') as part:
                data = part.read()
                out.write(data)

def download_parts(old_input_file, output_dir,parts_num, num_thread=28):
    file_list = []
    for i in range(parts_num):
        file_list.append(f"{old_input_file}_{i}.gxl_part")
    fake_path = utils_file.do_get_fake_file()
    random.shuffle(file_list)
    utils_file.write_list_to_file(file_list, fake_path)
    utils_file.do_sync_files_download_data_multi_thread(
        file_list_path=fake_path,
        username="root",
        password="Fy!mATB@QE",
        remote_host="139.210.101.41",
        local_directory=output_dir,
        num_thread=num_thread
    )


if __name__ == "__main__":
    input_file = "/mnt/sfs/asr/code/wenet_undersdand_and_speech_xlgeng/examples/wenetspeech/whisper/exp/epoch_16_with_asr-chat_full_data_50percent_pureX/step_26249.pt"
    input_file = "/mnt/sfs/asr/code/wenet_undersdand_and_speech_xlgeng/examples/wenetspeech/whisper/exp/epoch21_cosyvoice1_new-set_token_1w_plus-multi_task/step_49999.pt"
    output_dir = input_file.replace('.pt', '')
    num_parts = 100  # 要分割的份数
    # split_file(input_file, num_parts)
    output_lab_dir = '/home/work_nfs16/asr_data/ckpt/understanding_model/epoch21_cosyvoice1_new/step_49999'
    utils_file.makedir_sil(output_lab_dir)
    download_parts(input_file,output_lab_dir,num_parts, num_thread=5)
    input_file_lab = output_lab_dir+".pt"
    old_input_file = f'{output_lab_dir}/{os.path.basename(input_file)}'
    combine_files(input_file_lab, old_input_file, num_parts)
