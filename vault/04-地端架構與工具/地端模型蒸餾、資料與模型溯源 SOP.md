---
title: 地端模型蒸餾、資料與模型溯源 SOP
type: Operational SOP Note
domain: Model Distillation & Data Provenance
tags:
  - Distillation
  - DataProvenance
  - ModelProvenance
  - ConfidenceScore
author: AIEC Defense Expert Team
version: 1.0
last_updated: 2026-07-26
status: Complete
---

# 🧪 地端模型蒸餾、資料與模型溯源 SOP

> [!IMPORTANT]
> 本 SOP 專門呼應 NCSIST AIEC 架構圖 (`AIEC_1.pptx`) 中**「地端模型蒸餾/微調」、「Data & Model Provenance 溯源」與「信心分數 (Confidence Score) 校準」**模組。

```
[教師模型 Teacher Model (70B)] ──(Knowledge Distillation 知識蒸餾)──> [邊緣學生模型 Edge Student (7B/3B)]
                                                                               │
                                                                               ▼
[資料/模型溯源 Data & Model Provenance] <──(邏輯檢查 / 清洗規則 / 版本號)──── [信心分數 Confidence Score 校準]
```

## 📌 核心作業程序與控制點

### 1. Edge 端模型蒸餾與輕量化 (Edge Distillation)
- 將地端 70B 主權大模型之知識蒸餾 (Knowledge Distillation) 至 7B/3B 輕量化邊緣模型，兼顧作戰時延與精度。

### 2. 資料與模型溯源 (Data & Model Provenance)
- **Data Provenance (資料溯源)**：記錄每一筆訓練樣本之採集來源、邏輯檢查規則、清洗演算法版本號 (`v1.4.2`) 與標籤品質。
- **Model Provenance (模型溯源)**：追溯模型訓練超參數、權重 Checkpoint 雜湊值與微調歷程。一旦模型發生戰術誤判，能於 10 分鐘內回溯並隔離污染數據。

### 3. 信心分數 (Confidence Score) 與可解釋路徑
- 所有輸出必須伴隨校準後之信心指數 (Confidence Score, score)，評估 ECE 期望校準誤差 ($\mathrm{ECE} \le 0.05$)，防止盲目過度信任。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[NCSIST AIEC 國防 AI 評測與認證總體架構]]
- [[SHIELD 治理循環活動]]
- [[5. 信任校準與過度依賴]]
- [[15. 系統軌跡可追溯性與可稽核性]]
