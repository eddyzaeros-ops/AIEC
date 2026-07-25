---
title: F類 - 決策支援與預測分析評測 SOP
type: Application System SOP
domain: Predictive Analytics & C2
tags:
  - PredictiveAnalytics
  - PyOD
  - ConceptDrift
  - UQ
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 📈 F類 - 決策支援與預測分析評測 SOP

## 📌 系統範疇與核心威脅
- **範疇**：聲納/雷達特徵預測、後勤需求預測、擊殺鏈 (Kill Chain) 決策輔助。
- **威脅**：戰場概念漂移 (Concept Drift)、OOD 數據高信心誤判、黑盒子缺乏信任。

## 🧮 關鍵評測指標
1. [[Q12. 概念與數據漂移監控率]]：$\mathrm{Drift~Recall} \ge 0.95 \quad \wedge \quad t_{\mathrm{alarm}} \le 5	ext{min}$ (PyOD)
2. [[Q13. 不確定性量化 (UQ)]]：$\mathrm{OOD~Variance~Coverage} \ge 0.95$ (MC-Dropout)
3. [[Q15. 系統軌跡可追溯性]]：高保真日誌包含輸入數據、Confidence Score 與 COA。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[國防 AI 安全保密與審計三維矩陣]]
- [[AIEC 15 項量化評測指標與 SOP]]
