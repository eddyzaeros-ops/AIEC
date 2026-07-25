---
title: 主權 AI 平台與四層 LLM 堆疊
type: Infrastructure Note
domain: Sovereign AI & Compute
tags:
  - SovereignAI
  - LLMStack
  - MinxiongCampus
  - AirGap
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🏛️ 主權 AI 平台與四層 LLM 堆疊

## 📌 民雄院區與國家級主權算力
國防 AI 核心設施必須建立於 100% 完全實體隔離 (Air-Gapped) 之地端主權算力節點（如民雄院區），具備電力韌性、物理防護與演算法安全機制。

```
┌────────────────────────────────────────────────────────┐
│ Tier 4: 受控雲端閘道 (Gated Cloud API) - 僅非密級開放    │
├────────────────────────────────────────────────────────┤
│ Tier 3: 邊緣輕量化模型 (Edge Quantized) - 7B/3B GGUF     │
├────────────────────────────────────────────────────────┤
│ Tier 2: 專家混合架構 (MoE Model) - 8x7B 戰術專用模型   │
├────────────────────────────────────────────────────────┤
│ Tier 1: 密集型基底模型 (Dense Foundation) - 70B 主權算力 │
└────────────────────────────────────────────────────────┘
```

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[NCSIST AIEC 國防 AI 評測與認證總體架構]]
- [[國防 AIEC 核心任務與交戰規則 (RoE)]]
- [[地端 LLM 推論引擎與 Middleware 工具鏈]]
