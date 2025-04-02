import sys
sys.path.insert(0,"../../../")

from gxl_ai_utils.utils import utils_file

root_output_dir = "/mnt/sfs/asr/test_data/test_sets_format_3000"
# for 3500chat
input_tar_path = "/mnt/sfs/asr/update_data/3500_chat/tmp"
output_raw_path =f"{root_output_dir}/3500_chat/data.list"
utils_file.do_convert_shards2raw(None, raw_data_list_path=output_raw_path, output_wav_dir_path=input_tar_path)
output_text_path = f'{root_output_dir}/3500_chat/text'
output_token_path =f"{root_output_dir}/3500_chat/speech_token"
dict_list = utils_file.load_dict_list_from_jsonl(output_raw_path)
text_dict = {}
token_dict = {}
for dict_i in dict_list:
    text_dict[dict_i['key']] = dict_i['txt']
    token_dict[dict_i['key']] = utils_file.do_convert_str_to_float_list(dict_i['speech_token'])
utils_file.write_dict_to_scp(text_dict, output_text_path)
utils_file.write_dict_to_scp(token_dict, output_token_path)

input_tar_path = "/mnt/sfs/asr/update_data/3500_asr/tmp"
output_raw_path =f"{root_output_dir}/3500_asr/data.list"
utils_file.do_convert_shards2raw(None, raw_data_list_path=output_raw_path, output_wav_dir_path=input_tar_path)
output_text_path = f'{root_output_dir}/3500_asr/text'
output_token_path =f"{root_output_dir}/3500_asr/speech_token"
dict_list = utils_file.load_dict_list_from_jsonl(output_raw_path)
text_dict = {}
token_dict = {}
for dict_i in dict_list:
    text_dict[dict_i['key']] = dict_i['txt']
    token_dict[dict_i['key']] = utils_file.do_convert_str_to_float_list(dict_i['speech_token'])
utils_file.write_dict_to_scp(text_dict, output_text_path)
utils_file.write_dict_to_scp(token_dict, output_token_path)


