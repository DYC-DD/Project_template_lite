import time
import torch
import sys
import numpy as np
from sklearn.preprocessing import OneHotEncoder


# 計時器
class Timer:
    def __init__(self):
        """ 初始化 Timer 類別，並將開始時間設置為 None """
        self.start_time = None

    def start(self):
        """ 啟動計時器，記錄當前時間 """
        self.start_time = time.time()

    def stop(self):
        """ 停止計時器，並返回運行的時間(以小時、分鐘、秒、毫秒為單位) """
        if self.start_time is None:
            raise Exception("計時器尚未開始，請先呼叫 start()")
        
        end_time = time.time()  # 取得結束時間
        elapsed_time = end_time - self.start_time  # 計算經過的時間
        
        hours = int(elapsed_time // 3600)  # 小時
        minutes = int((elapsed_time % 3600) // 60)  # 分鐘
        seconds = int(elapsed_time % 60)  # 秒
        milliseconds = int((elapsed_time * 1000) % 1000)  # 毫秒
        
        # 以小時:分鐘:秒.毫秒的格式返回運行時間
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"


# 檢查 cuda,python,torch version
def cuda_version():
    # 檢查 Python 版本
    python_version = sys.version
    print(f"Python 版本: {python_version}")

    # 檢查 PyTorch 版本
    pytorch_version = torch.__version__
    print(f"PyTorch 版本: {pytorch_version}")

    # 檢查 CUDA 是否可用
    cuda_available = torch.cuda.is_available()
    print(f"CUDA 可用: {cuda_available}")

    if cuda_available:
        # 如果 CUDA 可用，檢查 CUDA 版本和 GPU 裝置
        print(f"CUDA 版本: {torch.version.cuda}")
        print(f"GPU 數量: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
        # 取得目前使用中的 GPU 裝置
        current_device = torch.cuda.current_device()
        print(f"目前的 GPU 裝置：{torch.cuda.get_device_name(current_device)}")


# one hot encode工具
def one_hot_encode(data):
    """
    將輸入的資料轉換為 One-Hot 編碼格式。

    參數:
    data (list or array-like): 要進行 One-Hot 編碼的資料（可以是列表、陣列或其他可迭代的結構）

    回傳:
    np.ndarray: 經過 One-Hot 編碼後的陣列
    """
    # 初始化OneHotEncoder
    encoder = OneHotEncoder(sparse_output=False)

    # 將輸入資料轉換為2D格式
    data_reshaped = np.array(data).reshape(-1, 1)

    # 進行One-Hot編碼
    one_hot_encoded = encoder.fit_transform(data_reshaped)

    return one_hot_encoded
# 範例使用
# data = ['cat', 'dog', 'bird', 'cat', 'dog']
# encoded_data = one_hot_encode(data)
# print(encoded_data)