1. python 都是 windows 安裝版
2. 系統PATH固定指定到Python\ 真正版本看Python link到哪一個版本
3. Python313忘記是哪一個應用有問題，所以安裝到根目錄去(爲了統一,做了一個link回來這個目錄)
4. windows 提供 py可以偵測系統有哪些版本的python (但要windows 安裝的才行)
  - py -0p  ==> list python version in system
  - py -3.10 ==> run python 3.10


# 指定python環境(Windows)
py -3.13 -m venv .venv-win-3.13
.\.venv-win-3.13\Scripts\activate
python -V
pip install -r requirements.txt


# 指定python環境(Linux/WSL)
pyenv install 3.13.0         # 一次性
pyenv local 3.13.0           # 這個資料夾預設 3.13
python -m venv .venv-wsl-3.13
source .venv-wsl-3.13/bin/activate
python -V
pip install -r requirements.txt



