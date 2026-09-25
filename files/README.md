# 國中英語學習 App — 題庫與 AI 架構

## 目錄結構
```
english-app/
├── data/
│   ├── words/
│   │   ├── wordlist_2000.json   ← 教育部 2000 字（基礎1200+挑戰800）
│   │   └── wordlist_2000.csv
│   └── questions/
│       └── gept_questions.json  ← GEPT初級靜態題庫（字彙/文法/閱讀）
├── prompts/
│   └── prompt_templates.json    ← AI動態出題模板（5種題型）
└── scripts/
    ├── build_wordlist.py
    └── build_questions.py
```

## 兩大題庫來源

### 1. 教育部 2000 字表（靜態）
- 基礎 1200 字（level 1）：國中必背核心字彙
- 挑戰 800 字（level 2）：GEPT 初級延伸字彙
- 依主題分類：daily / school / food / nature / emotion / sport...
- 授權：課綱公開資料，可自由使用

### 2. GEPT 初級題庫
- 字彙選擇題、文法選擇題、閱讀測驗
- 非商業用途可使用官方預試題
- 格式：JSON，含題目、選項、解析

## AI 動態出題（Claude API）

### 呼叫方式
```javascript
const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1000,
    system: template.system,
    messages: [{ role: "user", content: filledPrompt }]
  })
});
```

### 五種題型模板
| 模板 | 用途 | 觸發時機 |
|------|------|---------|
| vocab_fill | 字彙填空 | 單字卡答錯後補強 |
| grammar_fill | 文法選擇 | 文法練習模組 |
| error_correction | 改錯題 | 進階文法挑戰 |
| reading_passage | 閱讀短文+測驗 | 閱讀理解模組 |
| sentence_making | 造句批改 | 寫作練習模組 |

## 模組對應

| 模組 | 靜態來源 | AI 動態 |
|------|---------|--------|
| 單字卡 | 教育部 2000 字 | AI 生成例句 |
| 文法練習 | GEPT 文法題 | grammar_fill / error_correction |
| 閱讀理解 | GEPT 閱讀題 | reading_passage |
| 番茄鐘 | — | — |

## 推薦開發順序
1. 完成字表 JSON → 單字卡模組
2. 載入 GEPT 題庫 → 文法 + 閱讀靜態題
3. 串接 Claude API → AI 動態補強出題
4. 整合番茄鐘節奏控制

## 字彙分級對照
| 程度 | 使用字表 | 對應年級 |
|------|---------|---------|
| 基礎 | level 1（1200字）| 國中 7-8 年級 |
| 進階 | level 1+2（2000字）| 國中 8-9 年級 |
