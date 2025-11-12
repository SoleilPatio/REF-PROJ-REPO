#!python
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
from api_key_helper import load_api_key




# === 各個指令對應的功能函式 ===
def cmd_apikey():
    key = load_api_key("API_KEY-ALPHA_VANTAGE.local")
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


 # 模擬 switch-case 的 dispatch table
COMMANDS = {
    "apikey": cmd_apikey,
    "news_sentiment": cmd_news_sentiment,
    "symbol_search": cmd_symbol_search,
    "time_series_daily":cmd_time_series_daily,
}

def cmd_default(*args):
    print("Unknown command:", " ".join(args))
    print("Available commands:")
    for key in COMMANDS:
      print(key)

# === switch-case 主控邏輯 ===
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <command> [args...]")
        print("Available commands:")
        for key in COMMANDS:
          print(f"  - {key}")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    # 取得對應函式，若找不到則用預設函式
    func = COMMANDS.get(command, cmd_default)
    func(*args)  # 將其餘參數傳入



# === 程式進入點 ===
API_KEY = load_api_key("API_KEY-ALPHA_VANTAGE.local")

if __name__ == "__main__":
    main()
