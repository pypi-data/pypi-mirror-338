import numpy as np
import argparse

# 定义命令行参数解析器
parser = argparse.ArgumentParser(description="Load a .npy file and print its content.")
parser.add_argument("file_path", type=str, help="Path to the .npy file")

# 解析命令行参数
args = parser.parse_args()

# 加载 .npy 文件
data = np.load(args.file_path)

# 打印数据
print("Data loaded from .npy file:")
print(data)
print("Shape of the data:", data.shape)
