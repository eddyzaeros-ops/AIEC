---
title: JATIC 七大共通構面
type: Framework Note
domain: JATIC Evaluation
tags:
  - JATIC
  - EvaluationDimensions
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🏛️ JATIC 七大共通構面 (Common Evaluation Dimensions)

聯合 AI 測試中心 (JATIC) 定義國防 AI 系統必須通過的 7 大評測構面：

1. ** Robustness (對抗與自然穩健性)**：對抗貼片與天候干擾下維持精度，參閱 [[1. 對抗韌性]]、[[2. 自然穩健性]]。
2. ** Resiliency (系統韌性與失效安全)**：異常時 100ms 內安全中斷，參閱 [[4. 可中止性與失效安全]]。
3. ** Explainability (可解釋性)**：提供特徵熱力圖歸因，參閱 [[7. 模型可解釋性與顯著性歸因]]。
4. ** Competence (勝任力與 MSR)**：端到端任務完成率 $MSR \ge 0.95$，參閱 [[3. 任務完成率]]。
5. ** Fairness (公平性與無偏見)**：訓練集無隱性偏見，合規 AIF360。
6. ** Trust Calibration (信任校準)**：ECE 誤差 $\le 0.05$，防止過度依賴，參閱 [[5. 信任校準與過度依賴]]。
7. ** Drift Detection (漂移監控)**：即時捕捉概念漂移，參閱 [[12. 概念與數據漂移監控率]]。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[T&E 四大能力層次]]
- [[AIEC 15 項量化評測指標與 SOP]]
