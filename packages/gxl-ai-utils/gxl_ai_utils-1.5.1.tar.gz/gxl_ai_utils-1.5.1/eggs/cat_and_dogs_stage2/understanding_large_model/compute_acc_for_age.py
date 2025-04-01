import os
import sys
import re

from gxl_ai_utils.utils import utils_file

import jieba
import tqdm


def get_tag_from_str(input_str):
    # 使用正则表达式提取所有 <> 中的内容
    matches = re.findall(r'<.*?>', input_str)
    # 输出结果
    if len(matches)==0:
        return '<--no_tag-->'
    return matches[1].upper()
def do_compute_acc(ref_file, hyp_file, output_dir):
    """
    计算正确率和错误率，并列出混淆矩阵
    :return:
    """
    utils_file.makedir_sil(output_dir)
    utils_file.logging_info('开始计算正确率，acc')
    acc_path = os.path.join(output_dir, 'acc')
    hyp_dict = utils_file.load_dict_from_scp(hyp_file)
    ref_dict = utils_file.load_dict_from_scp(ref_file)
    tag_hyp_dict = {}
    for key, value in hyp_dict.items():
        tag_hyp_dict[key] = get_tag_from_str(value)
    tag_ref_dict = {}
    for key, value in ref_dict.items():
        tag_ref_dict[key] = get_tag_from_str(value)
    output_acc_f = open(acc_path, 'w', encoding='utf-8')
    same_num = 0
    all_tags = set()
    # utils_file.print_dict(utils_file.do_get_random_subdict(tag_ref_dict, 10))
    for tag in tag_ref_dict.values():
        all_tags.add(tag)
    # for tag in tag_hyp_dict.values():
    #     all_tags.add(tag)
    labels = sorted(list(all_tags))

    utils_file.logging_info(f'标签种类为：{labels}')
    # labels = [style_convert_dict.get(label, label) for label in labels]
    utils_file.logging_info(f'标签种类为：{labels}')
    num_classes = len(labels)
    matrix = [[0] * num_classes for _ in range(num_classes)]
    for key, hyp_tags in tag_hyp_dict.items():
        if key not in tag_ref_dict:
            continue
        ref_tags = tag_ref_dict[key]
        # 判断标签是否相同
        if ref_tags == hyp_tags:
            if_same = True
            same_num += 1
            index = labels.index(ref_tags)
            matrix[index][index] += 1
        else:
            if_same = False
            # 标签不同的情况，找到真实标签和预测标签对应的索引，在相应的位置加1
            ref_index = labels.index(ref_tags)
            if hyp_tags in labels:
                hyp_index = labels.index(hyp_tags)
                matrix[ref_index][hyp_index] += 1
        # 向文件写入数据
        output_acc_f.write(f"key: {key}\n")
        output_acc_f.write(f"ref_tag: {ref_tags}\n")
        output_acc_f.write(f"hyp_tag: {hyp_tags}\n")
        output_acc_f.write(f"if_same: {if_same}\n")
        output_acc_f.write("\n")  # 添加空行分隔不同的条目
    acc_num = same_num / len(tag_hyp_dict)
    output_acc_f.write(f'正确率为：{acc_num}')
    output_acc_f.flush()
    output_acc_f.close()
    # utils_file.copy_file(acc_path, os.path.join(output_dir2, 'acc'), use_shell=True)
    # figure_path = os.path.join(output_dir, 'confusion_matrix.png')
    # do_showing_confusion_matrix(labels, matrix, output_fig_path=figure_path)
    # utils_file.copy_file(figure_path, os.path.join(output_dir2, 'confusion_matrix.png'))
    return {
        'acc': acc_num,
        # 'wer': wer_all,
    }

res_text_path = "/home/work_nfs15/asr_data/ckpt/understanding_model/epoch_16_with_asr-chat_full_data_50percent_pureX/test_step_26249.pt/age_gender/age_gender_only_age/llmasr_decode/text"
res_text_path = "/home/work_nfs15/asr_data/ckpt/understanding_model/epoch_16_with_asr-chat_full_data_50percent_pureX/test_step_26249.pt/asr_age_gender/llmasr_decode/text"
lab_data_list_path = "/home/work_nfs15/asr_data/data/test_sets_format_3000/age_gender/age_gender_only_gender/data.list"
text_lab_path = "/home/work_nfs15/asr_data/data/test_sets_format_3000/age_gender/age_gender_only_gender/text"
dict_list = utils_file.load_dict_list_from_jsonl(lab_data_list_path)
dict_text = {}
for dict_i in dict_list:
    txt = dict_i['txt']
    dict_text[dict_i['key']] = txt
utils_file.write_dict_to_scp(dict_text, text_lab_path)
res = do_compute_acc(text_lab_path, res_text_path, "./tmp")
print(res)
    