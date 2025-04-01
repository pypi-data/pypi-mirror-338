from gxl_ai_utils.utils import utils_file
# input_data_dir = "/root/autodl-tmp/corpus/AISHELL-ASR0018/SPEECHDATA"
# output_dir = "/root/autodl-tmp/gengxuelong/data/AISHELL-ASR0018"
# utils_file.makedir_sil(output_dir)
# wav_scp_path = utils_file.join_path(output_dir, "wav.scp")
# utils_file.do_get_scp_for_wav_dir(input_data_dir,wav_scp_file_path=wav_scp_path, recursive=True)
# input_text_origin_path = "/root/autodl-tmp/corpus/AISHELL-ASR0018/DOC/content.txt"
# text_dict = utils_file.load_dict_from_scp(input_text_origin_path)
# new_text_dict = {}
# for key in text_dict:
#     new_key = key.replace(".wav","")
#     new_text_dict[new_key] = text_dict[key]
# utils_file.write_dict_to_scp(new_text_dict, wav_scp_path.replace("wav.scp","text"))
# wav_scp_path = utils_file.join_path(output_dir, "wav.scp")
# text_path = wav_scp_path.replace("wav.scp","text")
# data_list_path = utils_file.join_path(output_dir, "data.list")
# utils_file.do_convert_wav_text_scp_to_jsonl(wav_scp_path, text_path, data_list_path)

def make_data_for_child_data():
    input_dir = "/root/autodl-tmp/gengxuelong/data/child_data/data/test/test/test"
    output_dir = "/root/autodl-tmp/gengxuelong/data/child_data/data/test/scp"
    wav_dict = utils_file.do_get_scp_for_wav_dir(input_dir,suffix=".wav", recursive=True)
    text_dict = {}
    for key, value in wav_dict.items():
        json_file_path = value.replace(".wav",".json")
        item_dict = utils_file.load_dict_from_json(json_file_path)
        text_str = item_dict["text"]
        text_dict[key] = text_str
    utils_file.write_dict_to_scp(text_dict, utils_file.join_path(output_dir, "text"))
    utils_file.write_dict_to_scp(wav_dict, utils_file.join_path(output_dir, "wav.scp"))
    data_list_path = utils_file.join_path(output_dir, "data.list")
    utils_file.do_convert_wav_text_scp_to_jsonl(utils_file.join_path(output_dir, "wav.scp"), utils_file.join_path(output_dir, "text"), data_list_path)

if __name__ == '__main__':
    make_data_for_child_data()


