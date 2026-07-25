---
title: 國防 AI 評測 6 大方法論與 SOP
type: Methodology Note
domain: Testing Methodologies
tags:
  - EvaluationMethodology
  - RedTeaming
  - SOP
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🧪 國防 AI 評測 6 大方法論與 SOP

1. **黑箱評測 (Black-box Testing)**：僅經由 API 介面輸入對抗樣本進行效能壓力測試。
2. **白箱評測 (White-box Testing)**：調用模型內部權重與梯度，產出 SHAP / LIME 特徵歸因圖。
3. **基準測試 (Benchmark Testing)**：使用 ImageNet-C, AgentBench, PromptBench 等標準數據集。
4. **紅軍演練 (Red Teaming)**：利用 garak, CALDERA 模擬真實敵方對抗攻擊與 Prompt 注入。
5. **專家評估 (Human-in-the-Loop Evaluation)**：指揮官配戴 EEG 與眼動儀評估認知負荷。
6. **營運持續監控 (Continuous Operational Monitoring)**：線上部署 PyOD 與 Alibi 監控數據漂移。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[MITRE ATLAS 人工智慧對抗威脅矩陣]]
- [[AIEC 15 項量化評測指標與 SOP]]
