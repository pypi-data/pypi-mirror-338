from gxl_ai_utils.utils import utils_file

user_name = 'aslp'
password = "ASLPaslp"
remote_host = "10.68.109.101"
path_list = "/home/work_nfs14/pkchen/data/asr_token/asr/shards_list.txt"
output_dir = "/home/node54_tmpdata2/data4understand/asr_token"
utils_file.makedir_sil(output_dir)
utils_file.do_sync_files(
    file_list_path=path_list,
    password=password,
    username=user_name,
    remote_host=remote_host,
    local_directory=output_dir,
)
shards_list_path = f'{output_dir}/shards_list.txt'
utils_file.do_get_list_for_wav_dir(
    output_dir,shards_list_path, suffix='.tar'
)
