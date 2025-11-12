#!/usr/bin/python3
#...................................
# clslib standard header: if executed by import, add path to sys.path
#...................................
import os, sys
if __name__ != "__main__":
  current_dir = os.path.dirname(os.path.abspath(__file__))
  if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
#...................................

import os
import sys
import random




def load_api_key(filename: str) -> str:
    """從與此 Python 檔案同目錄的檔案中隨機選出一個 API key。"""
    current_dir = os.path.dirname(os.path.abspath(__file__))  # 取得目前程式所在目錄
    filepath = os.path.join(current_dir, filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]  # 去除空行與換行

    if not lines:
        raise ValueError(f"{filepath} is empty or contains no valid keys.")
    return random.choice(lines)




# === 各個指令對應的功能函式 ===
def cmd_apikey():
    key = load_api_key("APIKEY-alphavantage.local")
    print(f"Random API Key: {key}")

def cmd_news_sentiment(tickers):
    import requests
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={tickers}&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()
    print(data)

def cmd_symbol_search(keyword):
    import requests
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()
    print(data)

def cmd_time_series_daily(symbol, outputsize="full"): #outputsize="full" or "compact"
    import requests
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize={outputsize}&apikey={API_KEY}"
    r = requests.get(url)
    data = r.json()
    print(data)


def cmd_echo(*args):
    print(" ".join(args))

def cmd_default(*args):
    print("Unknown command:", " ".join(args))

# === switch-case 主控邏輯 ===
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <command> [args...]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    # 模擬 switch-case 的 dispatch table
    commands = {
        "apikey": cmd_apikey,
        "news_sentiment": cmd_news_sentiment,
        "symbol_search": cmd_symbol_search,
        "time_series_daily":cmd_time_series_daily,
    }

    # 取得對應函式，若找不到則用預設函式
    func = commands.get(command, cmd_default)
    func(*args)  # 將其餘參數傳入



# === 程式進入點 ===
API_KEY = load_api_key("APIKEY-alphavantage.local")

if __name__ == "__main__":
    main()
