from gxl_ai_utils.utils import utils_file

input_token_data_dir = "/mnt/sfs/asr/update_data/3500_chat"
old_path = f"{input_token_data_dir}/shards_list_old.txt"
input_path = f"{input_token_data_dir}/shards_list.txt"
path_list = utils_file.load_list_file_clean(input_path)
res_list = []
for path_i in path_list:
    if not utils_file.if_file_exist(path_i) or utils_file.get_file_size(path_i)< 1:
        print(f'{path_i} not exist or size is 0')
    else:
        res_list.append(path_i)

utils_file.copy_file(input_path, old_path)
utils_file.write_list_to_file(res_list, input_path)
