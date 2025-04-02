"""
从caption的测试集的data.list得到text
"""
from gxl_ai_utils.utils import utils_file

input_dir = "/home/node54_tmpdata/xlgeng/code/wenet_whisper_finetune/examples/wenetspeech/whisper/gxl_data/test_sets/caption"
partions = ['caption_1','caption_2']
for partion in partions:
    tmp_data_list = utils_file.join_path(input_dir, partion, 'data.list')
    output_text_path = utils_file.join_path(input_dir, partion, 'text')
    dict_list = utils_file.load_dict_list_from_jsonl(tmp_data_list)
    text_dict = {}
    for dict_i in dict_list:
        text_dict[dict_i['key']] = dict_i['txt']
    utils_file.write_dict_to_scp(text_dict, output_text_path)
