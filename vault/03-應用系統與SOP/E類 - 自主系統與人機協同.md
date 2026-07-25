---
title: E類 - 自主系統與人機協同評測 SOP
type: Application System SOP
domain: Autonomous Systems & HMT
tags:
  - AutonomousSystems
  - HMT
  - DoDD3000_09
  - NASATLX
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🚁 E類 - 自主系統與人機協同評測 SOP

## 📌 系統範疇與核心威脅
- **範疇**：無人機蜂群、自主武器系統、指管人機協同團隊 (HMT)。
- **威脅**：系統死鎖失控、盲目過度信任 (Over-reliance)、指揮官認知過載。

## 🧮 關鍵評測指標
1. [[Q3. 任務完成率]]：$\mathrm{MSR} \ge 0.95$ (VBS 4 / EADSIM LVC 100 次模擬)
2. [[Q4. 可中止性與失效安全]]：$	au_{\mathrm{abort}} \le 100	ext{ms} \quad \wedge \quad \mathrm{FailSafe} = 100\%$ (DoDD 3000.09)
3. [[Q5. 信任校準與過度依賴]]：$\mathrm{ECE} \le 0.05 \quad \wedge \quad R_{\mathrm{overreliance}} \le 0.05$
4. [[Q6. 認知負荷與適應性]]：$\Delta \mathrm{TLX} \ge 0.30 \quad \wedge \quad \Delta t_{\mathrm{decision}} \le 2.0	ext{s}$

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[國防 AIEC 核心任務與交戰規則 (RoE)]]
- [[AIEC 15 項量化評測指標與 SOP]]
