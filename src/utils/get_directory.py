import os

def get_directory(level=0):
    """
    根據所給的層數，取得當前文件的指定目錄。
    
    :param level: 從當前文件向上層的層數，0 表示當前文件所在目錄，1 表示父目錄，2 表示父目錄的父目錄，依此類推。
    :return: 指定目錄的路徑
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 根據層數往上走對應的目錄
    for _ in range(level):
        current_dir = os.path.dirname(current_dir)
        
    return current_dir


"""
範例
current_dir = get_directory()  # 當前檔案的目錄
parent_dir = get_directory(level=1)  # 父目錄
grandparent_dir = get_directory(level=2)  # 父目錄的父目錄以此類推
"""