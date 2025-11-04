[n8n doc](https://docs.n8n.io/)

# [Install-npm](https://docs.n8n.io/hosting/installation/npm/)
- 查看版本
npm view n8n versions --json
npm view n8n dist-tags

- 安裝版本
npm install -g n8n@0.126.1
npm install -g n8n@next

- 啓動
n8n
n8n start

- 更新
npm update -g n8n   ==>to latest version

# Reference Command
[npm]:Node Package Manager (管理套件)
- 查看安裝套件
npm list -g --depth=0
npm root -g             ==> 查看全域套件安裝位置
npm list -g n8n         ==> 查看單一套件版本
npm info n8n            ==> 查看套件詳細資訊

[nvm]:Node Version Manager (管理Node.js版本)
- [安裝windows nvm](https://github.com/coreybutler/nvm-windows)
  - install dir: C:\APN\DEV\nvm4w\nodejs ==> 失敗，有點可怕的東西
  - 自己切換路徑好像比較快
- 版本
node -v





