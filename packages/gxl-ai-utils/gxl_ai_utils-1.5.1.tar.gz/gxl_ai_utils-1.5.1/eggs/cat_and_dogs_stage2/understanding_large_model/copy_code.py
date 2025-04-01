import sys
sys.path.insert(0,'../../../')
from gxl_ai_utils.utils import utils_file

"""
把杨泽使用的代码拷贝到我的目录下，但是不拷贝大的pt文件
"""
input_dir = "/home/node60_tmpdata/gjli"
output_dir = "/home/work_nfs16/xlgeng/code/wenet_speech_token"
utils_file.makedir_sil(output_dir)
utils_file.do_copy_directory_only_codefile_with_true_suffix(
    input_dir, output_dir, true_suffix_tuple=tuple()
)