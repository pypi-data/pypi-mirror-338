import sys
sys.path.insert(0, "../../../")
from gxl_ai_utils.utils import utils_file

# root_output_dir = "/mnt/sfs/asr/update_data/asr2chat_by_llm"
#
# # 得到wenetspeech的所有shards路径
# all_shards_list_path = "/mnt/sfs/asr/asr/shards_list.txt"
# lines = utils_file.load_list_file_clean(all_shards_list_path)
# res_list = []
# for line_i in lines:
#     if "wenetspeech" in line_i:
#         res_list.append(line_i)
# output_wenetspeech_shards_list_path = root_output_dir + "/wenetspeech_shards_list.txt"
# utils_file.write_list_to_file(res_list, output_wenetspeech_shards_list_path)
#
# # 开始解压全部结果
# wav_path = f'{root_output_dir}/wav.scp'
# text_path = f'{root_output_dir}/text'
# # 对虽有wenetspeech进行tar包解压
# utils_file.do_uncompress_shard(output_wenetspeech_shards_list_path, f'{root_output_dir}/origin_wav',
#                                num_thread=32,
#                                wav_path=wav_path,
#                                text_path=text_path)

# 通过raw file得到common format data.list
wav_dir = "/home/work_nfs15/asr_data/data/wenetspeech/train"
wav_path = "/home/work_nfs15/asr_data/data/wenetspeech/train/wav.scp"
# utils_file.do_get_scp_for_wav_dir(wav_dir, wav_path, recursive=True)

text_path = "/home/work_nfs15/asr_data/data/wenetspeech/train_shards/wenetspeech_new_all/text"

fake_wav_path = utils_file.do_get_fake_file()
# wav_dict = utils_file.load_dict_from_scp(wav_path)
new_txt_dict_path = "/home/work_nfs15/asr_data/data/wenetspeech/wenetspeech_asr_chat_by_llm/gxl_1800.list"
new_txt_path = "/home/work_nfs15/asr_data/data/wenetspeech/wenetspeech_asr_chat_by_llm/text"
new_wav_path = "/home/work_nfs15/asr_data/data/wenetspeech/wenetspeech_asr_chat_by_llm/wav.scp"
# new_text_dict = utils_file.load_dict_from_scp(new_txt_dict_path)
# wav_dict_2 = {}
# text_dict_2 = {}
# for key, value in new_text_dict.items():
#     new_key = key+"_wenet"
#     if new_key not in wav_dict or new_key not in wav_dict:
#         print(f"{new_key} not in wav_dict or text_dict")
#         continue
#     wav_path_i = wav_dict[new_key]
#     text_items = value.strip().split()
#     if len(text_items) != 2:
#         print(f"{key} text_items not 2, value : {value}, len: {len(text_items)}")
#         continue
#     new_text = "<开始回答>".join(text_items)
#     text_dict_2[new_key] = new_text
#     wav_dict_2[new_key] = wav_path_i
#
# utils_file.write_dict_to_scp(text_dict_2, new_txt_path)
# utils_file.write_dict_to_scp(wav_dict_2, new_wav_path)


# 对data.list 进行压缩
# data_list = utils_file.do_get_formatted_datalist_for_all_task(
#     new_wav_path,
#     new_txt_path,
#     dataset_name='wenetspeech_by_llm_asr_chat',
#     task_tag="<TRANSCRIBE> <S2TCHAT>"
# )
output_raw_path =  "/home/work_nfs15/asr_data/data/wenetspeech/wenetspeech_asr_chat_by_llm/data.list"
# utils_file.write_dict_list_to_jsonl(data_list, output_raw_path)

from make_shard_for_common_format import make_shards
make_shards(
    output_raw_path,
    "/home/work_nfs15/asr_data/data/wenetspeech/wenetspeech_asr_chat_by_llm/shards",
    num_utts_per_shard=1000,
    prefix='wenetspeech_by_llm_asr_chat',
    resample=16000,
    num_threads=32
)