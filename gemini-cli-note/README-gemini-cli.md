## [Windows Install]()
npm install -g @google/gemini-cli




## [Ubuntu Install]()
## install nodejs

curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v
npm -v



---

## 🧭 一步一步設定 npm 全域路徑到 `~/bin/.npm-global`

### 1️⃣ 建立目錄

mkdir -p ~/bin/.npm-global

### 2️⃣ 設定 npm 使用這個目錄作為全域路徑

npm config set prefix '~/bin/.npm-global'

這會在 `~/.npmrc` 中加一行：

```
prefix=~/bin/.npm-global
```

---

### 3️⃣ 加入 PATH 環境變數

將 npm 的全域可執行檔路徑加入 shell 的 PATH。
（依你使用的 shell，編輯 `.bashrc` 或 `.zshrc`）

```bash
echo 'export PATH="$HOME/bin/.npm-global/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

### 4️⃣ 測試設定是否生效

```bash
which npm
npm prefix -g
```

應該會顯示你的路徑：

```
/home/clouds/bin/.npm-global
```

---

### 5️⃣ 現在重新安裝 gemini-cli（不需要 sudo）

```bash
npm install -g @google/gemini-cli
```

---

### 6️⃣ 確認可以使用

```bash
which gemini
gemini -h
```

