from gxl_ai_utils.utils import utils_file

meld_path = "/mnt/sfs/asr/test_data/test_sets_format_3000/caption_0107_esc50"

mer_path = "/mnt/sfs/asr/test_data/test_sets_format_3000/caption_0107_vocalsound"

# for meld
dict_list = utils_file.load_dict_list_from_jsonl(f'{meld_path}/data.list')
text_dict = {}
for dict_i in dict_list:
    text_dict[dict_i["key"]] = dict_i["txt"]
utils_file.write_dict_to_scp(text_dict,
                            f"{meld_path}/text")
# for mer
dict_list = utils_file.load_dict_list_from_jsonl(f'{mer_path}/data.list')
text_dict = {}
for dict_i in dict_list:
    text_dict[dict_i["key"]] = dict_i["txt"]
utils_file.write_dict_to_scp(text_dict,
                            f"{mer_path}/text")