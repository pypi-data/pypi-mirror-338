import subprocess
import sys
sys.path.insert(0, "../../../")
from gxl_ai_utils.utils import utils_file

orign_dir = "/home/work_nfs7"
output_dir = "/home/nfs7_new"
output_user = 'ubuntu'
output_password = '1'
output_host = "192.168.0.77"

sub_dirs = [
"zhzhang",
"xlgeng",
"kxxia",
"zkliu",
"znlin",
"gjli",
"syliu",
"lhli",
"gbma",
"jxyao",
"cbhao",
"jbhu",
"yacao",
"pkchen",
"zhguo",
"hfxue",
"hkxie",
"cywang",
"mshliu",
"ypjiang",
"pcguo",
"yhdai",
"zxzhao",
"bykang",
"zqwang",
]

sub_dirs = [
    "azhang",
    "charts",
    "data_aishell0055",
    "emotion_dataset_processed",
    "ix-applications",
    "kafka_2.13-3.5.1",
    "NoManLand",
    "SoulBox",
    "TamerlanT",
    "TamerlanT",
    "TamerlanT",
    "TamerlanT",
    "TamerlanT",
]

runner = utils_file.GxlDynamicProcessPool()
# 将一个目录copy到root_dir下面
for item in sub_dirs:
    sub_dir_i = f'{orign_dir}/{item}'
    runner.add_task(utils_file.do_sync_copy_dir_upload, [sub_dir_i,output_dir , output_password, output_user, output_host])
    # utils_file.do_sync_copy_dir_upload(sub_dir_i,output_dir , output_password, output_user, output_host)
runner.start()