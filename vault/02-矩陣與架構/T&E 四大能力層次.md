---
title: T&E 四大能力層次
type: Framework Note
domain: DoD T&E Hierarchy
tags:
  - TEVV
  - DoD_T_E
  - CapabilityLevels
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 📐 DoD T&E 四大能力層次 (Capability Levels)

美國國防部 (DoD) CDAO 將 AI 系統測試與評估 (T&E) 劃分為四大漸進能力層次：

```
Level 4: 作戰性測試與評估 (Operational T&E / MSR) ──> 終極戰術效能確效
  ▲
Level 3: 系統整合評測 (Systems Integration T&E)   ──> API / C2 / 零信任閘道
  ▲
Level 2: 人機系統整合 (HSI & Cognitive Load T&E)  ──> NASA-TLX / 信任校準
  ▲
Level 1: 基礎模型評測 (Base Model & Algorithm T&E) ──> 準確率 / 對抗韌性
```

| 層次代號 | 層次名稱 | 測試焦點與關鍵指標 | 代表性測試工具/環境 |
| :--- | :--- | :--- | :--- |
| **Level 1** | **基礎模型評測** | 演算法精確度、對抗韌性、自然穩健性 | IBM ART 360, NRTK, ImageNet-C |
| **Level 2** | **人機系統整合 (HSI)** | 認知負荷 (NASA-TLX)、眼動追蹤、信任校準 (ECE) | HMT Suite, EEG 腦電儀, Eye-Tracker |
| **Level 3** | **系統整合評測** | API 閘道零信任、通訊時延、工具調用邊界 | OPA, SPIFFE/SPIRE, AgentBench |
| **Level 4** | **作戰性測試與評估** | 端到端任務完成率 (MSR)、擊殺鏈閉合速度 | VBS 4, EADSIM, LVC 平行戰場 |

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[JATIC 七大共通構面]]
- [[AIEC 15 項量化評測指標與 SOP]]
- [[E類 - 自主系統與人機協同]]
