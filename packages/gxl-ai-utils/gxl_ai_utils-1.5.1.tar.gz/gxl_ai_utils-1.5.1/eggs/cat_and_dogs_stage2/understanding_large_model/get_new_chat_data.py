"""
有一个大约1000万条单论对话和大量多轮对话的nlp数据集，地址： https://github.com/thu-coai/CDial-GPT
该文件对其进行处理，并生成语音

"""
from datasets import load_dataset
data_dir = '/home/work_nfs15/asr_data/data/chat_data/CDial-GPT'
partion = ['base','large']
partion2 = ['train','dev','test']
for p in partion:
    for p2 in partion2:
        print(p,p2)
        data_path = f'{data_dir}/{p}/{p2}.json'
        print(data_path)
        # 加载数据集
        dataset = load_dataset("lccc", "base")  # or "large"

        # 假设我们选择保存训练集（train）为文件
        train_dataset = dataset[p2]
        # 如果你想保存为 JSON 格式
        train_dataset.to_pandas().to_json(data_path, orient="records", lines=True)

def format():
    """"""
    #整理格式
