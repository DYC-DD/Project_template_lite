# Project_template

##### Project 資料夾範本

---

### 專案資料夾 開發結構樹狀圖
```
Project_template/
├── config/                        # 用於存放系統設定檔
│   ├── config.yaml                # 專案的配置文件，使用YAML格式存放全局設定參數
│   ├── key.env                    # 金鑰
│   ├── logging.conf               # 日誌設定檔，配置Python的日誌記錄器
│   └── settings.ini               # 系統或應用層面的配置文件，使用INI格式存放設置項
│
├── data/                          # 存放專案所需的數據集
│   ├── feature/                   # 特徵文件
│   ├── processed/                 # 處理過的數據文件
│   ├── raw/                       # 原始數據文件
│   └── cleaned_data.ipynb         # 資料處理
│
├── docs/                          # 存放專案的相關文檔，如API說明、設計文檔等
│
├── envs/                          # 用於存放環境設定相關文件
│   ├── Dockerfile                 # 用於建立Docker容器的設定檔，方便專案的容器化部署
│   └── environment.yml            # Conda環境的配置文件
│
├── src/                           # 存放專案的源代碼
│   ├── utils/                     # 存放常用的輔助函數或工具模組
│   │   ├── cuda_version.py        # 檢測CUDA版本GPU及Python版本
│   │   ├── get_directory.py       # 方便調用不同目錄下的程式
│   │   ├── one_hot_encode.py      # 轉為One-Hot工具
│   │   └── time.py                # 計時器，計算執行時間
│   ├── main.py                    # 主程序入口，通常用於啟動應用
│   └── module.py                  # 各自實現不同功能的模組
│
├── tests/                         # 存放測試代碼
│   ├── test_module.ipynb          # 測試筆記本
│   └── test_module.py             # 對應 src/ 中模組的測試文件
│
├── LICENSE                        # 項目的授權許可文件
├── README.md                      # 項目說明文件
├── requirements.txt               # 列出專案所需的Python庫和版本
└── setup.py                       # 專案的安裝腳本
```
---
### 專案資料夾 開發結構詳解
- `config/`: 用於存放系統設定檔。
    - `config.yaml`: 專案的配置文件，使用YAML格式存放全局設定參數。
    - `key.env`：金鑰。
    - `logging.conf`: 日誌設定檔，配置Python的日誌記錄器。
    - `settings.ini`: 系統或應用層面的配置文件，使用INI格式存放設置項。
- `data/`: 存放專案所需的數據集。
    - `feature/`：特徵文件。
    - `processed/`: 處理過的數據文件。
    - `raw/`: 原始數據文件。
    - `cleaned_data.ipynb`：資料處裡。
- `docs/`: 存放專案的相關文檔，如API說明、設計文檔等。
- `envs/`: 用於存放環境設定相關文件。
    - `Dockerfile`: 用於建立Docker容器的設定檔，方便專案的容器化部署。
    - `environment.yml`: Conda 環境的配置文件，列出專案依賴項，可使用 `conda env create -f environment.yml` 來建立環境。
- `src/`: 存放專案的源代碼。建議將代碼模組化，並保持每個模塊的職責單一。
    - `utils/`: 存放常用的輔助函數或工具模組。
        - `cuda_version.py`：檢測CUDA版本GPU及Python版本。
        - `get_directory.py`：方便調用不同目錄下的程式。
        - `one_hot_encode.py`：轉為 One-Hot工具。
        - `time.py`：計時器，計算執行時間。
    - `main.py`: 主程序入口，通常用於啟動應用。
    - `module.py`: 各自實現不同功能的模組。
- `tests/`: 存放測試代碼，使用 unittest 或 pytest 等測試框架撰寫。
    - `test_module.ipynb`：測試筆記本。
    - `test_module.py`: 對應 src/ 中模組的測試文件。
- `LICENSE`: 項目的授權許可文件，指定專案的版權資訊。
- `README.md`: 項目說明文件，簡要介紹專案的目標、使用方法和主要功能。
- `requirements.txt`: 列出專案所需的Python庫和版本，通過 `pip install -r requirements.txt` 可以快速安裝依賴項。
- `setup.py`: 專案的安裝腳本，定義專案的包信息和依賴關係，使用 pip 安裝時非常有用。
