import torch
# 检查 CUDA 是否可用
print(torch.cuda.is_available())  # 输出 True 则表示 GPU 可用[5,8](@ref)
# 获取当前 CUDA 设备信息（如果可用）
if torch.cuda.is_available():
    print(f"CUDA 设备名称: {torch.cuda.get_device_name(0)}")  # 输出 GPU 型号，例如 'NVIDIA GeForce RTX 3060'[4](@ref)
    print(f"CUDA 版本: {torch.version.cuda}")  # 输出 PyTorch 识别的 CUDA 版本号[5](@ref)
    print(f"GPU 设备数量: {torch.cuda.device_count()}")  # 输出可用的 GPU 数量[4](@ref)

import cv2
print(cv2.__version__)

#import numpy as np
#print(np.__version__)

import pandas as pd
print(pd.__version__)
