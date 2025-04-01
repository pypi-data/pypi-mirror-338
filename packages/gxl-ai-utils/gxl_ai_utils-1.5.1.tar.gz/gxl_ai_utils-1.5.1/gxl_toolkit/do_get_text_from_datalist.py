import argparse
from gxl_ai_utils.utils import utils_file

parser = argparse.ArgumentParser()
parser.add_argument("--data_list_path", type=str)
parser.add_argument("--text_path", type=str)
parser.add_argument('--part', type=str, default='txt')

args = parser.parse_args()
dict_list = utils_file.load_dict_list_from_jsonl(args.data_list_path)
text_dict = {}
part = args.part
if part == 'txt':
    for dict_i in dict_list:
        text_dict[dict_i["key"]] = dict_i["txt"]
else:
    for dict_i in dict_list:
        res = dict_i[part]
        if not res.startswith('<'):
            res = '<' + res
        if not res.endswith('>'):
            res += '>'
        text_dict[dict_i["key"]] = res

utils_file.write_dict_to_scp(text_dict, args.text_path)
