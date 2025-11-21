import os
import random

"""
從與此 Python 原始檔相同目錄下的 .local 檔案讀取 API Key。
若檔案有多行（多個 API Key），則隨機選一個回傳。

參數：
    filename (str): ex. "API_KEY-ALPHA_VANTAGE.local"

回傳：
    str: 隨機選中的 API Key

例外：
    FileNotFoundError: 若找不到檔案。
    ValueError: 若檔案存在但沒有任何有效的 key。
"""

def load_api_key(filename: str) -> str:

    # 取得目前這個檔案所在的資料夾
    base_dir = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(base_dir, filename)

    if not os.path.exists(key_path):
        raise FileNotFoundError(f"找不到 API 金鑰檔案：{key_path}")

    with open(key_path, "r", encoding="utf-8") as f:
        keys = [line.strip() for line in f.readlines() if line.strip() and not line.startswith("#")]

    if not keys:
        raise ValueError(f"檔案 {key_path} 內沒有任何有效的 API Key。")

    # 隨機挑一個 key（用來分散流量）
    api_key = random.choice(keys)

    # info
    # print(f"[INFO] {filename} api_key = {api_key}")

    return api_key
