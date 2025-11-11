
---

### 🧩 一、**Core Stock APIs（股票價格資料）**

> 用於抓取股票的歷史與即時價格資料，是最常用的一群。

| 類別                                       | 功能                       | 應用範例               |
| ---------------------------------------- | ------------------------ | ------------------ |
| **Intraday / Daily / Weekly / Monthly**  | 取得分鐘、日、週、月 K 線資料（OHLCV）。 | 製作 K 線圖、技術分析、回測策略。 |
| **Adjusted 版本**                          | 含除權息調整後的價格。              | 計算報酬率、長期績效分析。      |
| **Quote Endpoint**                       | 即時單一股票報價（含成交量）。          | 建立即時行情板或警報系統。      |
| **Realtime Bulk Quotes (Premium)**       | 批量即時報價。                  | 監控多檔股票同時變化。        |
| **Ticker Search / Global Market Status** | 查代號、查全球市場是否開盤。           | 搜尋股票或自動跳過休市時間。     |

---

### 💰 二、**Options Data APIs（選擇權資料）**

| 類別                             | 功能              | 應用          |
| ------------------------------ | --------------- | ----------- |
| **Realtime Options (Premium)** | 即時選擇權價格與Greeks。 | 製作選擇權分析儀表板。 |
| **Historical Options**         | 歷史選擇權資料。        | 訓練波動率預測模型。  |

---

### 🧠 三、**Alpha Intelligence™（市場情緒與洞察）**

| 類別                                   | 功能                | 應用             |
| ------------------------------------ | ----------------- | -------------- |
| **News & Sentiments**                | 抓取新聞與情緒分數。        | 訓練情緒分析模型、輔助決策。 |
| **Earnings Call Transcript**         | 財報電話會議逐字稿。        | NLP 分析企業用語與展望。 |
| **Top Gainers & Losers**             | 當日漲跌幅前幾名。         | 熱門股追蹤、異常波動偵測。  |
| **Insider Transactions**             | 內部人買賣紀錄。          | 分析高管動向。        |
| **Analytics (Fixed/Sliding Window)** | 自動計算統計窗口的技術或情緒指標。 | 建立機器學習特徵。      |

---

### 🧾 四、**Fundamental Data（基本面資料）**

> 關於公司財報與基本面分析的完整資料群。

| 類別                                               | 功能            | 應用           |
| ------------------------------------------------ | ------------- | ------------ |
| **Company Overview**                             | 公司摘要、PE、產業分類。 | 建立公司檔案。      |
| **ETF Profile & Holdings**                       | ETF 構成成分。     | 建立 ETF 分析系統。 |
| **Corporate Actions（Dividends / Splits）**        | 股息、分割紀錄。      | 計算調整後報酬率。    |
| **Income Statement / Balance Sheet / Cash Flow** | 財報三表。         | 財務分析、估值模型。   |
| **Shares Outstanding**                           | 發行股數。         | 計算市值與EPS。    |
| **Earnings History / Estimates / Calendar**      | 歷史與預期財報、財報日期。 | 預測獲利趨勢。      |
| **Listing / Delisting / IPO Calendar**           | 上市、下市與IPO時程。  | 追蹤市場新股變化。    |

---

### 🌍 五、**Forex (FX)**

| 類別                                      | 功能           | 應用           |
| --------------------------------------- | ------------ | ------------ |
| **Exchange Rates**                      | 即時匯率。        | 外匯報價、跨國投資換算。 |
| **Intraday / Daily / Weekly / Monthly** | 不同時間粒度的匯率歷史。 | 外匯策略與回測。     |

---

### 🪙 六、**Cryptocurrencies（加密貨幣）**

| 類別                                      | 功能          | 應用         |
| --------------------------------------- | ----------- | ---------- |
| **Exchange Rates**                      | 加密幣對法幣匯率。   | 加密資產估值。    |
| **Intraday / Daily / Weekly / Monthly** | 各時間區間的價格走勢。 | 交易策略與趨勢偵測。 |

---

### ⚙️ 七、**Commodities（原物料）**

| 類別                                                                    | 功能        | 應用           |
| --------------------------------------------------------------------- | --------- | ------------ |
| **Crude Oil (WTI/Brent)**                                             | 原油價格。     | 能源市場監控。      |
| **Natural Gas, Copper, Aluminum, Wheat, Corn, Cotton, Sugar, Coffee** | 主要商品價格。   | 通膨預測、產業成本分析。 |
| **Global Commodities Index**                                          | 全球商品綜合指數。 | 經濟景氣分析。      |

---

### 📈 八、**Economic Indicators（經濟指標）**

| 類別                                                                                  | 功能               | 應用           |
| ----------------------------------------------------------------------------------- | ---------------- | ------------ |
| **Real GDP / GDP per Capita**                                                       | 國內生產總值。          | 景氣循環研究。      |
| **Treasury Yield / Fed Funds Rate**                                                 | 公債殖利率、聯準會利率。     | 利率走勢預測。      |
| **CPI / Inflation / Retail Sales / Durable Goods / Unemployment / Nonfarm Payroll** | 通膨、零售、耐久財、失業、非農。 | 經濟模型、宏觀交易策略。 |

---

### 📊 九、**Technical Indicators（技術指標）**

> 計算各種技術分析指標，可直接用於策略開發或AI特徵工程。

| 分類                  | 常見指標                                               | 應用        |
| ------------------- | -------------------------------------------------- | --------- |
| **趨勢線與均線**          | SMA, EMA, WMA, DEMA, TEMA, TRIMA, KAMA, MAMA, VWAP | 均線交叉策略。   |
| **震盪與動能**           | MACD, RSI, STOCH, CCI, ADX, MOM, ROC               | 預測轉折點。    |
| **波動與區間**           | BBANDS, ATR, NATR, TRANGE                          | 風險管理。     |
| **量價指標**            | OBV, AD, ADOSC                                     | 量價背離分析。   |
| **希爾伯特轉換系列 (HT_*)** | 自動辨識趨勢週期。                                          | AI預測特徵提取。 |

---


