import os.path
import sys
from gc import is_finalized

sys.path.insert(0, '../../../')
from gxl_ai_utils.utils import utils_file
#
# root_dir_lab = "/home/work_nfs15/asr_data/data/test_sets_format_3000"
# root_dir_huawei = "/mnt/sfs/asr/test_data/test_sets_format_3000"
# testsets = [
#     "public_test/roobo_100",
#     "caption",
#     "emotion", "public_test/MELD_test", "public_test/MER23_test",
#     "style",
#     "gender",  "public_test/aishell1_gender", "public_test/kaggle_gender",
#     "age",  "public_test/kaggle_age",
#     "chat","public_test/AirBench_speech",
# ]
# for test_set in testsets:
#     print("test_set: ", test_set)
#     input_path = f"{root_dir_lab}/{test_set}/data4huawei.list"
#     input_data_path = f"{root_dir_lab}/{test_set}/data.list"
#     dict_list = utils_file.load_dict_list_from_jsonl(input_data_path)
#     wav_list = []
#     new_dict_list = []
#     for item in dict_list:
#         wav_list.append(item["wav"])
#         item['wav'] = f"/mnt/sfs/asr/test_data/test_sets_format_3000/{test_set}/wav/{os.path.basename(item['wav'])}"
#         new_dict_list.append(item)
#     utils_file.write_dict_list_to_jsonl(new_dict_list, input_path)
#     output_data_path = f"{root_dir_huawei}/{test_set}/data.list"
#     input_text_path = f"{root_dir_lab}/{test_set}/text"
#     if True or test_set == "caption" or test_set == "emotion" or not utils_file.if_file_exist(input_text_path):
#         text_dict = {}
#         dict_list = utils_file.load_dict_list_from_jsonl(input_path)
#         for dict_i in dict_list:
#             text_dict[dict_i['key']] = dict_i['txt']
#         utils_file.write_dict_to_scp(text_dict, input_text_path)
#     output_text_path = f"{root_dir_huawei}/{test_set}/text"
#     utils_file.do_sync_copy_file_upload(input_path, output_data_path,
#                                         username="root",
#                                         password="Fy!mATB@QE",
#                                         remote_host="139.210.101.41",
#                                         )
#     utils_file.do_sync_copy_file_upload(input_text_path, output_text_path,
#                                         username="root",
#                                         password="Fy!mATB@QE",
#                                         remote_host="139.210.101.41",
#                                         )


# input_path = f"/home/xlgeng/.cache/tmp.list"
# input_text_path = f"/home/xlgeng/.cache/text.list"
# test_set = 'caption_aslp_record'
# input_data_path = f"/home/work_nfs9/yacao/nfs7_copy/yacao/1227_audio_tagging_wjtian/audio_caption_test_0113.list"
# dict_list = utils_file.load_dict_list_from_jsonl(input_data_path)
# wav_list = []
# new_dict_list = []
# for item in dict_list:
#     wav_list.append(item["wav"])
#     item['wav'] = f"/mnt/sfs/asr/test_data/test_sets_format_3000/{test_set}/wav/{os.path.basename(item['wav'])}"
#     new_dict_list.append(item)
# utils_file.write_dict_list_to_jsonl(new_dict_list, input_path)
#
# output_data_path = f"/mnt/sfs/asr/test_data/test_sets_format_3000/{test_set}/data.list"
# text_dict = {}
# dict_list = utils_file.load_dict_list_from_jsonl(input_path)
# for dict_i in dict_list:
#     text_dict[dict_i['key']] = dict_i['txt']
# utils_file.write_dict_to_scp(text_dict, input_text_path)
# output_text_path = f"/mnt/sfs/asr/test_data/test_sets_format_3000/{test_set}/text"
# utils_file.do_sync_copy_file_upload(input_path, output_data_path,
#                                     username="root",
#                                     password="Fy!mATB@QE",
#                                     remote_host="139.210.101.41",
#                                     )
# utils_file.do_sync_copy_file_upload(input_text_path, output_text_path,
#                                     username="root",
#                                     password="Fy!mATB@QE",
#                                     remote_host="139.210.101.41",
#                                     )
# time_now = utils_file.do_get_now_time()
# dict_list = utils_file.load_dict_list_from_jsonl(input_data_path)
# wav_path_list = []
# for dict_i in dict_list:
#     wav_path_list.append(dict_i['wav'])
# fake_path = utils_file.do_get_fake_file()
# utils_file.write_list_to_file(wav_path_list, fake_path)
#
# utils_file.do_sync_files_upload_data_multi_thread(
#     file_list_path=fake_path,
#     username="root",
#     password="Fy!mATB@QE",
#     remote_host="139.210.101.41",
#     remote_dir=f"/mnt/sfs/asr/test_data/test_sets_format_3000/{test_set}/wav",
#     num_thread=4
# )
# esl_time = utils_file.do_get_elapsed_time(time_now)
# utils_file.logging_info(f"Total time: {esl_time} s")



# time_now = utils_file.do_get_now_time()
# input_shards_path = "/home/work_nfs9/znlin/S2TCHAT/shards_list.txt"
# dataname = "asr_chat_znlin_2025-1-24"
# fake_file = utils_file.do_replace_str_for_file_and_return_new_file(input_shards_path,'/home/work_nfs9/znlin/S2TCHAT/shards',f"/mnt/sfs/asr/update_data/{dataname}")
# utils_file.do_sync_copy_file_upload(fake_file,f"/mnt/sfs/asr/update_data/{dataname}/shards_list.txt",
#                                     username="root",
#                                     password="Fy!mATB@QE",
#                                     remote_host="139.210.101.41",
#                                     )
# utils_file.do_sync_files_upload_data_multi_thread(
#     file_list_path=input_shards_path,
#     username="root",
#     password="Fy!mATB@QE",
#     remote_host="139.210.101.41",
#     remote_dir=f"/mnt/sfs/asr/update_data/{dataname}",
#     num_thread=10
# )
# esl_time = utils_file.do_get_elapsed_time(time_now)
# utils_file.logging_info(f"Total time: {esl_time} s")


# time_now = utils_file.do_get_now_time()
# input_shards_path = "/home/environment2/pkchen/cutwav/withid/shards_list.txt"
# dataname = "asr_chat_pkchen_2025-1-24"
# fake_file = utils_file.do_replace_str_for_file_and_return_new_file(input_shards_path,'/home/environment2/pkchen/cutwav/withid/shards',f"/mnt/sfs/asr/update_data/{dataname}")
# utils_file.do_sync_copy_file_upload(fake_file,f"/mnt/sfs/asr/update_data/{dataname}/shards_list.txt",
#                                     username="root",
#                                     password="Fy!mATB@QE",
#                                     remote_host="139.210.101.41",
#                                     )
# utils_file.do_sync_files_upload_data_multi_thread(
#     file_list_path=input_shards_path,
#     username="root",
#     password="Fy!mATB@QE",
#     remote_host="139.210.101.41",
#     remote_dir=f"/mnt/sfs/asr/update_data/{dataname}",
#     num_thread=10
# )
# esl_time = utils_file.do_get_elapsed_time(time_now)
# utils_file.logging_info(f"Total time: {esl_time} s")

# time_now = utils_file.do_get_now_time()
# input_shards_path = "/home/work_nfs15/asr_data/data/wenetspeech/wenetspeech_asr_chat_by_llm/shards/shards_list.txt"
# dataname = "asr_chat_wenetspeech_enhance_2025-1-24"
# fake_file = utils_file.do_replace_str_for_file_and_return_new_file(input_shards_path,'/home/work_nfs15/asr_data/data/wenetspeech/wenetspeech_asr_chat_by_llm/shards',f"/mnt/sfs/asr/update_data/{dataname}")
# utils_file.do_sync_copy_file_upload(fake_file,f"/mnt/sfs/asr/update_data/{dataname}/shards_list.txt",
#                                     username="root",
#                                     password="Fy!mATB@QE",
#                                     remote_host="139.210.101.41",
#                                     )
# utils_file.do_sync_files_upload_data_multi_thread(
#     file_list_path=input_shards_path,
#     username="root",
#     password="Fy!mATB@QE",
#     remote_host="139.210.101.41",
#     remote_dir=f"/mnt/sfs/asr/update_data/{dataname}",
#     num_thread=10
# )
# esl_time = utils_file.do_get_elapsed_time(time_now)
# utils_file.logging_info(f"Total time: {esl_time} s")


# time_now = utils_file.do_get_now_time()
# dataname = "TEXT2TOKEN_part_1"
# input_shards_path = f"/home/node48_tmpdata/hkxie/4O/speech_data_final/{dataname}/shards_list.txt"
# fake_file = utils_file.do_replace_str_for_file_and_return_new_file(input_shards_path,f'/home/node48_tmpdata/hkxie/4O/speech_data_final/{dataname}/shards',f"/mnt/sfs/asr/update_data/{dataname}")
# utils_file.do_sync_copy_file_upload(fake_file,f"/mnt/sfs/asr/update_data/{dataname}/shards_list.txt",
#                                     username="root",
#                                     password="Fy!mATB@QE",
#                                     remote_host="139.210.101.41",
#                                     )
# utils_file.do_sync_files_upload_data_multi_thread(
#     file_list_path=input_shards_path,
#     username="root",
#     password="Fy!mATB@QE",
#     remote_host="139.210.101.41",
#     remote_dir=f"/mnt/sfs/asr/update_data/{dataname}",
#     num_thread=8
# )
# esl_time = utils_file.do_get_elapsed_time(time_now)
# utils_file.logging_info(f"Total time: {esl_time} s")



# time_now = utils_file.do_get_now_time()
# dataname = "TEXT2TOKEN_part_2"
# input_shards_path = f"/home/node48_tmpdata/hkxie/4O/speech_data_final/{dataname}/shards_list.txt"
# fake_file = utils_file.do_replace_str_for_file_and_return_new_file(input_shards_path,f'/home/node48_tmpdata/hkxie/4O/speech_data_final/{dataname}/shards',f"/mnt/sfs/asr/update_data/{dataname}")
# utils_file.do_sync_copy_file_upload(fake_file,f"/mnt/sfs/asr/update_data/{dataname}/shards_list.txt",
#                                     username="root",
#                                     password="Fy!mATB@QE",
#                                     remote_host="139.210.101.41",
#                                     )
# utils_file.do_sync_files_upload_data_multi_thread(
#     file_list_path=input_shards_path,
#     username="root",
#     password="Fy!mATB@QE",
#     remote_host="139.210.101.41",
#     remote_dir=f"/mnt/sfs/asr/update_data/{dataname}",
#     num_thread=5
# )
# esl_time = utils_file.do_get_elapsed_time(time_now)
# utils_file.logging_info(f"Total time: {esl_time} s")


# time_now = utils_file.do_get_now_time()
# dataname = "TEXT2TOKEN_part_3"
# input_shards_path = f"/home/node48_tmpdata/hkxie/4O/speech_data_final/{dataname}/shards_list.txt"
# fake_file = utils_file.do_replace_str_for_file_and_return_new_file(input_shards_path,f'/home/node48_tmpdata/hkxie/4O/speech_data_final/{dataname}/shards',f"/mnt/sfs/asr/update_data/{dataname}")
# utils_file.do_sync_copy_file_upload(fake_file,f"/mnt/sfs/asr/update_data/{dataname}/shards_list.txt",
#                                     username="root",
#                                     password="Fy!mATB@QE",
#                                     remote_host="139.210.101.41",
#                                     )
# utils_file.do_sync_files_upload_data_multi_thread(
#     file_list_path=input_shards_path,
#     username="root",
#     password="Fy!mATB@QE",
#     remote_host="139.210.101.41",
#     remote_dir=f"/mnt/sfs/asr/update_data/{dataname}",
#     num_thread=5
# )
# esl_time = utils_file.do_get_elapsed_time(time_now)
# utils_file.logging_info(f"Total time: {esl_time} s")


#
# time_now = utils_file.do_get_now_time()
# input_shards_path = f"/home/node57_data2/tlzuo/dataset/DB-ASR-106_withid/speechtoken/shard.list"
# dataname = "speech2text_token_DB-ASR-106_add_by_2025-3_5"
# fake_file = utils_file.do_replace_str_for_file_and_return_new_file(input_shards_path,f'/home/node57_data2/tlzuo/dataset/DB-ASR-106_withid/speechtoken/shards',f"/mnt/sfs/asr/update_data/{dataname}")
# utils_file.do_sync_copy_file_upload(fake_file,f"/mnt/sfs/asr/update_data/{dataname}/shards_list.txt",
#                                     username="root",
#                                     password="Fy!mATB@QE",
#                                     remote_host="139.210.101.41",
#                                     )
# utils_file.do_sync_files_upload_data_multi_thread(
#     file_list_path=input_shards_path,
#     username="root",
#     password="Fy!mATB@QE",
#     remote_host="139.210.101.41",
#     remote_dir=f"/mnt/sfs/asr/update_data/{dataname}",
#     num_thread=10
# )
# esl_time = utils_file.do_get_elapsed_time(time_now)
# utils_file.logging_info(f"Total time: {esl_time} s")

time_now = utils_file.do_get_now_time()
root_input_dir = "/home/node48_tmpdata/hkxie/4O/speech_data_final/TEXT2TOKEN_part_5"
input_shards_path = f"{root_input_dir}/shards_list.txt"
dataname = "TEXT2TOKEN_part_5"
remote_root_dir="/mnt/sfs/asr/update_data"
fake_file = utils_file.do_replace_str_for_file_and_return_new_file(input_shards_path,f'{root_input_dir}/shards',f"{remote_root_dir}/{dataname}")
utils_file.do_sync_copy_file_upload(fake_file,f"{remote_root_dir}/{dataname}/shards_list.txt",
                                    username="root",
                                    password="Fy!mATB@QE",
                                    remote_host="139.210.101.41",
                                    )
utils_file.do_sync_files_upload_data_multi_thread(
    file_list_path=input_shards_path,
    username="root",
    password="Fy!mATB@QE",
    remote_host="139.210.101.41",
    remote_dir=f"{remote_root_dir}/{dataname}",
    num_thread=5 # 30h
)
esl_time = utils_file.do_get_elapsed_time(time_now)
utils_file.logging_info(f"Total time: {esl_time} s")

time_now = utils_file.do_get_now_time()
root_input_dir = "/home/node48_tmpdata/hkxie/4O/speech_data_final/TEXT2TOKEN_part_6"
input_shards_path = f"{root_input_dir}/shards_list.txt"
dataname = "TEXT2TOKEN_part_6"
remote_root_dir="/mnt/sfs/asr/update_data"
fake_file = utils_file.do_replace_str_for_file_and_return_new_file(input_shards_path,f'{root_input_dir}/shards',f"{remote_root_dir}/{dataname}")
utils_file.do_sync_copy_file_upload(fake_file,f"{remote_root_dir}/{dataname}/shards_list.txt",
                                    username="root",
                                    password="Fy!mATB@QE",
                                    remote_host="139.210.101.41",
                                    )
utils_file.do_sync_files_upload_data_multi_thread(
    file_list_path=input_shards_path,
    username="root",
    password="Fy!mATB@QE",
    remote_host="139.210.101.41",
    remote_dir=f"{remote_root_dir}/{dataname}",
    num_thread=5 # 30h
)
esl_time = utils_file.do_get_elapsed_time(time_now)
utils_file.logging_info(f"Total time: {esl_time} s")

time_now = utils_file.do_get_now_time()
root_input_dir = "/home/node48_tmpdata/hkxie/4O/speech_data_final/TEXT2TOKEN_part_7"
input_shards_path = f"{root_input_dir}/shards_list.txt"
dataname = "TEXT2TOKEN_part_7"
remote_root_dir="/mnt/sfs/asr/update_data"
fake_file = utils_file.do_replace_str_for_file_and_return_new_file(input_shards_path,f'{root_input_dir}/shards',f"{remote_root_dir}/{dataname}")
utils_file.do_sync_copy_file_upload(fake_file,f"{remote_root_dir}/{dataname}/shards_list.txt",
                                    username="root",
                                    password="Fy!mATB@QE",
                                    remote_host="139.210.101.41",
                                    )
utils_file.do_sync_files_upload_data_multi_thread(
    file_list_path=input_shards_path,
    username="root",
    password="Fy!mATB@QE",
    remote_host="139.210.101.41",
    remote_dir=f"{remote_root_dir}/{dataname}",
    num_thread=5 # 30h
)
esl_time = utils_file.do_get_elapsed_time(time_now)
utils_file.logging_info(f"Total time: {esl_time} s")

time_now = utils_file.do_get_now_time()
root_input_dir = "/home/node48_tmpdata/hkxie/4O/speech_data_final/TEXT2TOKEN_part_8"
input_shards_path = f"{root_input_dir}/shards_list.txt"
dataname = "TEXT2TOKEN_part_8"
remote_root_dir="/mnt/sfs/asr/update_data"
fake_file = utils_file.do_replace_str_for_file_and_return_new_file(input_shards_path,f'{root_input_dir}/shards',f"{remote_root_dir}/{dataname}")
utils_file.do_sync_copy_file_upload(fake_file,f"{remote_root_dir}/{dataname}/shards_list.txt",
                                    username="root",
                                    password="Fy!mATB@QE",
                                    remote_host="139.210.101.41",
                                    )
utils_file.do_sync_files_upload_data_multi_thread(
    file_list_path=input_shards_path,
    username="root",
    password="Fy!mATB@QE",
    remote_host="139.210.101.41",
    remote_dir=f"{remote_root_dir}/{dataname}",
    num_thread=5 # 30h
)
esl_time = utils_file.do_get_elapsed_time(time_now)
utils_file.logging_info(f"Total time: {esl_time} s")