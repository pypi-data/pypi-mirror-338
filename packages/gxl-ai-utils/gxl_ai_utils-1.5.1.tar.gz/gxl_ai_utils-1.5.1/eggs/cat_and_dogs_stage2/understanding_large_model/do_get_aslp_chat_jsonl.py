import re
from gxl_ai_utils.utils import utils_file
# s = '"wav": "/mnt/sfs/asr/test_data/test_sets_format_3000/aslp_chat_test_for_asr/lei_xie_6.wav", "emotion": "<NONE>", "gender": "<NONE>", "lang": "<CN>", "duration": "4.195", "speaker": "<NONE>", "extra": {"dataset": "alsp_chat"}, "task": "<S2TCHAT>", "txt": "能不能介绍下故宫的情况"'
def get_str(str_i):
    wav_pattern = r'"wav": "([^"]+)"'
    txt_pattern = r'"txt": "([^"]+)"'

    wav_result = re.search(wav_pattern, str_i)
    txt_result = re.search(txt_pattern, str_i)

    if wav_result:
        wav_path = wav_result.group(1)
    else:
        wav_path = "None"

    if txt_result:
        text = txt_result.group(1)
    else:
        text = "None"
    return wav_path, text

# lines = utils_file.load_list_file_clean(input_wav_path)
# dict_list = []
# for line in lines:
#     wav_path, text = get_str(line)
#     if wav_path is None or wav_path=="None" or len(wav_path)<8:
#         continue
#     print(f'wav_path:{wav_path}, text:{text}')
#     dict_i = {'wav': wav_path, 'txt': text, 'key': utils_file.do_get_file_pure_name_from_path(wav_path),
#               'emotion': "<None>", 'gender': "<None>", 'lang': "<CN>", 'duration': "4.195", 'speaker': "<None>",
#               'extra': {}, 'task': "<S2TCHAT>"}
#     dict_list.append(dict_i)
# utils_file.write_dict_list_to_jsonl(dict_list, input_wav_path)

input_wav_path = "/mnt/sfs/asr/test_data/test_sets_format_3000/aslp_chat_test_for_asr/data.list"
text_path = "/mnt/sfs/asr/test_data/test_sets_format_3000/aslp_chat_test_for_asr/text"
dict_list = utils_file.load_dict_list_from_jsonl(input_wav_path)
text_dict = {}
for dict_i in dict_list:
    text_dict[dict_i['key']] = dict_i['txt']
utils_file.write_dict_to_scp(text_dict, text_path)


input_wav_path = "/mnt/sfs/asr/test_data/test_sets_format_3000/aslp_chat_test/data.list"
text_path = "/mnt/sfs/asr/test_data/test_sets_format_3000/aslp_chat_test/text"
dict_list = utils_file.load_dict_list_from_jsonl(input_wav_path)
text_dict = {}
for dict_i in dict_list:
    text_dict[dict_i['key']] = dict_i['txt']
utils_file.write_dict_to_scp(text_dict, text_path)