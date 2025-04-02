from gxl_ai_utils.utils import utils_file
test_data_dir="/home/node54_tmpdata/xlgeng/code/wenet_whisper_finetune_xlgeng/examples/wenetspeech/whisper/data/test_sets"
data_list_path_list = utils_file.get_list_for_wav_dir(test_data_dir,suffix='list', recursive=True)
for data_list_path in data_list_path_list:
    print(data_list_path)
    text_path  = data_list_path.replace('data.list','text')
    dict_list = utils_file.load_dict_list_from_jsonl(data_list_path)
    text_dict = {}
    for dict_i in dict_list:
        text_dict[dict_i['key']] = dict_i['txt']
    utils_file.write_dict_to_scp(text_dict,text_path)
