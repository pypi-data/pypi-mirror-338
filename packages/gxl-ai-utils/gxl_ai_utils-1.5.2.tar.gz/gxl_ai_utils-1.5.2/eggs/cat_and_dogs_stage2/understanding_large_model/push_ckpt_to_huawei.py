import os.path
import random
import sys
sys.path.insert(0, '../../../')
from gxl_ai_utils.utils import utils_file

def split_file(input_file,here_parts_dir, num_parts):
    utils_file.makedir_sil(here_parts_dir)
    file_name = os.path.basename(input_file)
    with open(input_file, 'rb') as f:
        f.seek(0, 2)  # 将文件指针移动到文件末尾
        file_size = f.tell()  # 获取文件大小
        chunk_size = file_size // num_parts  # 计算每一份的大小
        utils_file.logging_limit_print(f'chunk_size:{chunk_size}')
        f.seek(0)  # 将文件指针移回文件开头
        for i in range(num_parts):
            part_file = f"{here_parts_dir}/{file_name}_{i}.gxl_part"
            utils_file.logging_info(f'part_file:{part_file}')
            with open(part_file, 'wb') as part:
                if i == num_parts - 1:  # 最后一部分可能会大一些，处理文件大小不能整除的情况
                    data = f.read()
                else:
                    data = f.read(chunk_size)
                part.write(data)


def combine_files(output_file, remote_parts_dir, num_parts):
    file_name = os.path.basename(output_file)
    utils_file.makedir_sil(remote_parts_dir)
    with open(output_file, 'wb') as out:
        for i in range(num_parts):
            part_file = f"{remote_parts_dir}/{file_name}_{i}.gxl_part"
            utils_file.logging_info(part_file)
            with open(part_file, 'rb') as part:
                data = part.read()
                out.write(data)

def upload_parts(remote_parts_dir, input_file, here_parts_dir, num_thread=28):
    file_list = []
    file_name = os.path.basename(input_file)
    for i in range(100):
        file_list.append(f"{here_parts_dir}/{file_name}_{i}.gxl_part")
    fake_path = utils_file.do_get_fake_file()
    random.shuffle(file_list)
    utils_file.write_list_to_file(file_list, fake_path)
    # utils_file.do_sync_files_download_data_multi_thread(
    #     file_list_path=fake_path,
    #     username="root",
    #     password="Fy!mATB@QE",
    #     remote_host="139.210.101.41",
    #     local_directory=output_dir,
    #     num_thread=num_thread
    # )
    utils_file.do_sync_files_upload_data_multi_thread(
        file_list_path=fake_path,
        username="root",
        password="Fy!mATB@QE",
        remote_host="139.210.101.41",
        remote_dir=remote_parts_dir,
        num_thread=num_thread
    )


if __name__ == "__main__":
    input_tar_file = "/home/work_nfs16/code/xlgeng/.cache/transformers/models--Qwen--Qwen2.5-7B-Instruct-1M.tar"
    output_remote_file = "/mnt/sfs/asr/env/.cache/transformers/models--Qwen--Qwen2.5-7B-Instruct-1M.tar"
    remote_parts_dir = "/mnt/sfs/asr/env/.cache/transformers/models--Qwen--Qwen2.5-7B-Instruct-1M/parts"
    here_parts_dir = "/home/work_nfs16/code/xlgeng/.cache/transformers/models--Qwen--Qwen2.5-7B-Instruct-1M/parts"
    utils_file.makedir_sil(here_parts_dir)
    # utils_file.makedir_sil(remote_parts_dir)
    split_file(input_tar_file, here_parts_dir, 100)
    upload_parts(remote_parts_dir, input_tar_file, here_parts_dir, num_thread=8)
    # combine_files(output_remote_file, remote_parts_dir, 100)