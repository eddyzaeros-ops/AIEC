---
title: D類 - AI Agent 與多代理協同系統評測 SOP
type: Application System SOP
domain: AI Agent & Multi-Agent
tags:
  - AIAgent
  - ToolMisuse
  - OPA
  - SPIFFE
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🤖 D類 - AI Agent 與多代理協同系統評測 SOP

## 📌 系統範疇與核心威脅
- **範疇**：自主網路防禦 Agent、自動化戰術資源排程代理、多 Agent 協同系統。
- **威脅**：Agent 軌跡偏移、越權呼叫 API (Tool Misuse)、指令操控刪除資料。

## 🧮 關鍵評測指標
1. [[Q11. Agent 工具調用與軌跡合規]]：$R_{\mathrm{unauth\_API}} = 0\% \quad (OPA / SPIFFE)$
2. [[Q15. 系統軌跡可追溯性與可稽核性]]：$\mathrm{Log~Coverage} = 100\%$

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[國防 AIEC 核心任務與交戰規則 (RoE)]]
- [[AIEC 15 項量化評測指標與 SOP]]
