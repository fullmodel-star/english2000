# 📚 國中英語 2000 單字

一個**離線可用、免安裝、零追蹤**的國中英語單字學習 PWA（漸進式網頁應用程式）。
涵蓋會考必備 **2000 個單字**，用「間隔複習 ＋ 單元闖關 ＋ 錯題本」幫學生把單字背熟。

> 純單一 HTML 檔、資料全存在手機本機、不上傳雲端、不需註冊、沒有廣告。

> **版本**：v1.1（2026-07-02）　｜　🔴 圖示「ABC 2000」（紅）　｜　📱 響應式　｜　✍️ 填空題　｜　🔊 翻卡朗讀例句
> **線上版**：<https://fullmodel-star.github.io/english2000/>　（詳細異動見 [更新記錄.md](更新記錄.md)）

---

## ✨ 功能

- **2000 單字**：每字含例句、中譯、詞性、主題；261 個高頻多義字附「另解」第二義項
- **單字卡**：3D 翻卡、滑動評分、翻面自動朗讀「單字＋例句」（TTS）、番茄鐘專注計時、SRS 間隔複習（Leitner 盒）
- **單元闖關**：分 40 單元（每單元 50 字），學習 → 測驗驗收 → ≥80% 過關蓋 ⭐ 解鎖下一關（可開自由模式跳關）
- **測驗**：英→中／中→英／拼字輸入／**填空**（例句挖空＋中文提示，加強記憶）四種題型、可選 10／20／50 題、可指定單元、中途存檔續做
- **錯題本**：答錯自動收錄、英中雙向各連對 2 次才畢業、間隔複習、錯因標籤、👹 魔王字、上次選錯提示
- **遊戲化**：XP 等級、連勝 combo、音效震動、19 種徽章
- **今日任務**：學新字／複習／清錯題三段進度，綁連續天數
- **響應式版面**：手機直式單欄；平板 / 大螢幕自動放寬、單元多欄、卡片放大（`--appw` + media query）
- **會考倒數**：設考試日，自動算「每天該背幾字」
- **班級用**：學生匯出進度 JSON，老師用 `teacher.html` 拖入彙整成班級總表＋CSV
- **貼心設定**：深色模式跟系統、簡潔模式、減壓／家長模式、螢幕時間提醒、家長 PIN 鎖、聽覺自動發音、新手引導

---

## 🚀 使用方式

### 直接用
用瀏覽器開啟 `index.html` 即可。

### 安裝成 App（需用 GitHub Pages 等 https 網址開啟）
- **Android**：Chrome 開啟 → 選單 →「安裝應用程式 / 加到主畫面」
- **iPhone / iPad**：Safari 開啟 → 分享 →「加入主畫面」

安裝後可全螢幕、離線使用。

---

## 🌐 部署到 GitHub Pages

**已部署**：repo `english2000`（帳號 fullmodel-star）→ **<https://fullmodel-star.github.io/english2000/>**

> ⚠️ 若線上版是在 2026-07-02 加入「響應式版面」之前上傳的，需**重新 push** 本資料夾最新檔案才會更新到響應式版。

重新部署步驟：
1. 把本資料夾所有檔案上傳到 GitHub repo（`index.html` 需在 repo 根目錄）。
2. repo → **Settings → Pages → Build and deployment → Source 選 `Deploy from a branch`，分支選 `main`／資料夾選 `/ (root)`**，儲存。
3. 稍等 1～2 分鐘建置完成，Pages 頁面上方會出現綠色「Your site is live at …」網址橫幅。
4. 用該 **https 網址**開啟，PWA（離線、安裝）才會生效。

---

## 📁 檔案結構

| 檔案 | 說明 |
|---|---|
| `index.html` | 主程式（學生背單字）— 單檔即整個 App |
| `teacher.html` | 老師班級彙整頁（拖入學生匯出檔 → 總表 + CSV） |
| `manifest.json` / `sw.js` | PWA 設定與離線快取 Service Worker |
| `icon-*.png` / `apple-touch-icon.png` / `icon.svg` | App 圖示（Android / iOS） |
| `files/` | 單字資料與重建工具（`wordlist_full.json`、`examples_progress.json`、`multisense.json`、`merge_examples.py`、`smoke_test.py`） |
| `docs/` | 開發文件（學生回饋報告、專業檢視報告、系統架構規劃） |
| `README.md` / `更新記錄.md` | 說明與版本異動記錄 |

> 實際運作只需要 `index.html`、`teacher.html`、`manifest.json`、`sw.js` 與 icon 檔；`files/`、`docs/` 與 `.md` 為資料／文件，不影響執行。

---

## 🔒 隱私

- 完全離線，**不連任何外部伺服器**（已用 CSP `connect-src 'none'` 強制）。
- 學習紀錄只存在使用者裝置的 `localStorage`，可隨時「匯出備份 / 清除」。
- 無帳號、無追蹤、無廣告、無第三方程式碼。適合未成年使用。

---

## 📄 授權

單字字表參考教育部國中英語 2000 字課綱；例句為本專案自製。供教學與學習使用。
