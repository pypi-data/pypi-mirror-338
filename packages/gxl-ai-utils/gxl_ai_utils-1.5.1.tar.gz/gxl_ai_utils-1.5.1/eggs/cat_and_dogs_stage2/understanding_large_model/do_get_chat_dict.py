from gxl_ai_utils.utils import utils_file
# path_1 = "/mnt/sfs/asr/update_data/3500_chat_asr/3500_with_asr_chat.list"
# output_path =  "/mnt/sfs/asr/update_data/3500_chat_asr/3500_with_asr_chat.jsonl"
# lines = utils_file.load_list_file_clean(path_1)
# dict_list = []
# for line in lines:
#     dict_i = {}
#     items = line.strip().split('\t')
#     if len(items) != 5:
#         utils_file.logging_warning("line error: {} len != 3 , continue".format(line) )
#         continue
#     dict_i["key"] = items[0]
#     dict_i["Q"] = items[2]
#     dict_i["A"] = items[3]
#     dict_list.append(dict_i)
# utils_file.write_dict_list_to_jsonl(dict_list, output_path)

root_dir = "/mnt/sfs/asr/update_data/3500_chat_asr"
path_list = utils_file.do_get_list_for_wav_dir(root_dir, suffix='jsonl')
res_dict = {}
for path_i in path_list:
    dict_list = utils_file.load_dict_list_from_jsonl(path_i)
    for dict_i in utils_file.tqdm(dict_list, total=len(dict_list)):
        key = dict_i["key"]
        if key in res_dict:
            utils_file.logging_warning("key {} exist in res_dict".format(key))
        new_txt = dict_i["Q"].replace(" ", "") + "<回答>" + dict_i["A"].replace(" ", "")
        res_dict[key] = new_txt
output_path = "/mnt/sfs/asr/update_data/3500_chat_asr/gxl_all_3500_with_asr_chat.scp"
utils_file.write_dict_to_scp(res_dict, output_path)
