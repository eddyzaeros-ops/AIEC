---
title: Lattice 戰術 C2 架構與 Menace 邊緣算力節點
type: Architecture Note
domain: Tactical C2 & Mesh Network
tags:
  - Lattice
  - Menace
  - JADC2
  - ZeroTrustAPI
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 📡 Lattice 戰術 C2 架構與 Menace 邊緣算力節點

## 📌 JADC2 全領域指管與邊界驗證
整合跨軍種與國內外異質指管系統（如將本地飛彈陣地數據與商用 C2 平台對接）時，Menace 邊緣算力節點與 API 閘道必須實施**零信任 (Zero Trust)** 邊界控制。

```
[飛彈陣地傳感器] ──> [Menace 邊緣算力節點] ──(零信任 SPIFFE/OPA 閘道)──> [Lattice 戰術 C2]
```

- **SPIFFE/SPIRE**：跨網段服務數位身份認證。
- **OPA (Open Policy Agent)**：微秒級 API 指令授權策略檢驗。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[國防 AIEC 核心任務與交戰規則 (RoE)]]
- [[D類 - AI Agent 與多代理協同系統]]
- [[戰術邊緣硬體安全與模型自毀機制]]
