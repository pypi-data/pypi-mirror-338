import sys
sys.path.insert(0, '../../../')
from gxl_ai_utils.utils import utils_file

time_now = utils_file.do_get_now_time()
utils_file.do_sync_files(
    file_list_path="/home/work_nfs3/syliu/for_gxl/Sex/sex/shards_list.txt",
    username="xlgeng",
    password="ggg123456.",
    remote_host="10.68.81.54",
    local_directory="/home/node54_tmpdata2/data4understand/update_data/sex",
    # num_thread=16
)
esl_time = utils_file.do_get_elapsed_time(time_now)
utils_file.logging_info(f"Total time: {esl_time} s")

# time_now = utils_file.do_get_now_time()
# utils_file.do_sync_files(
#     file_list_path="/home/work_nfs3/syliu/for_gxl/Age/age/shards_list.txt",
#     username="xlgeng",
#     password="ggg123456.",
#     remote_host="10.68.81.54",
#     local_directory="/home/node54_tmpdata2/data4understand/update_data/age",
#     # num_thread=16
# )
# esl_time = utils_file.do_get_elapsed_time(time_now)
# utils_file.logging_info(f"Total time: {esl_time} s")