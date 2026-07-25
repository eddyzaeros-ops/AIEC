---
title: SHIELD 治理循環活動
type: Governance Note
domain: Defense AI Lifecycle
tags:
  - AIEC
  - SHIELD
  - Lifecycle
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🔄 SHIELD 治理循環活動

SHIELD 為 AIEC 國防 AI 全生命週期動態治理與監督框架，分為六大連續步驟：

| 階段代號 | 階段名稱 | 核心任務與審計重點 | 代表性工具與規範 |
| :--- | :--- | :--- | :--- |
| **S** | **Set** (目標界定) | 定義系統邊界、應用類別 (A~F類)、RoE 人機授權與 CMMC 資安等級 | [[國防 AIEC 核心任務與交戰規則 (RoE)]] |
| **H** | **Hone** (精煉調校) | 資料清洗、安全對齊、LoRA 微調與 GGUF 量化部署 | [[地端 LLM 推論引擎與 Middleware 工具鏈]] |
| **I** | **Improve** (連續改進) | 根據紅軍演練漏洞回饋進行模型重訓練與護欄補強 | [[MITRE ATLAS 人工智慧對抗威脅矩陣]] |
| **E** | **Evaluate** (量化評測) | 執行 [[AIEC 15 項量化評測指標與 SOP]]，核發 TRL 通過證書 | [[AIEC 15 項量化評測指標與 SOP]] |
| **L** | **Log** (高保真日誌) | 強制保存傳感器輸入、Confidence Score、XAI 熱力圖與 API 軌跡 | [[F類 - 決策支援與預測分析]] |
| **D** | **Detect** (漂移偵測) | 線上即時監控數據分布與概念漂移 (Concept Drift) | [[PyOD]] / Alibi Detect |

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[AIEC 規範與治理雙支柱]]
- [[AIEC 15 項量化評測指標與 SOP]]
