"""
将所有数据搬运到转移盘
"""
import os

import tqdm

from gxl_ai_utils.utils import utils_file

output_dir = "/home/asr_transfer_dir"
data_conf_path = "./data_multi_task_3.yaml"
data_dict = utils_file.load_dict_from_yaml(data_conf_path)
for key, value in data_dict.items():
    utils_file.logging_info('开始处理如下数据：', key)
    shards_path = value["path"]
    shards_list = utils_file.load_list_file_clean(shards_path)
    output_dir_tmp = os.path.join(output_dir, key)
    utils_file.makedir_sil(output_dir_tmp)
    for shard_item_path in tqdm.tqdm(shards_list, desc=f"copy shards:{key}", total=len(shards_list)):
        output_file_path_item = utils_file.join_path(output_dir_tmp, os.path.basename(shard_item_path))
        utils_file.copy_file(shard_item_path, output_file_path_item, use_shell=True, is_jump=True)
    utils_file.logging_info('处理完成',key)
    utils_file.do_get_list_for_wav_dir(output_dir_tmp,os.path.join(output_dir_tmp,'shards_list.txt'),
                                       suffix='tar')
