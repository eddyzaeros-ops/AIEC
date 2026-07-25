---
title: 國防 AIEC 核心任務與交戰規則 (RoE)
type: Core Task Note
domain: Defense Governance & RoE
tags:
  - AIEC
  - DefenseAIEC
  - RoE
  - HITL
  - SovereignCompute
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# ⚔️ 國防 AIEC (Defense AIEC) 核心任務與交戰規則 (RoE)

## 📌 組織定位：動態管制中樞與審查閘門
國防 AIEC (Defense AIEC) 不僅是靜態文書審查單位，更是深諳技術與戰術的**動態管制中樞 (Dynamic Control Center)**。主導國防 AI 系統之技術成熟度 (TRL) 審查與放行管制。

```
                              ┌───────────────────────────┐
                              │   國防 AIEC 動態管制中樞   │
                              └─────────────┬─────────────┘
                                            │
   ┌──────────────────┬─────────────────────┼─────────────────────┬──────────────────┐
   ▼                  ▼                     ▼                     ▼                  ▼
┌──────────────┐ ┌──────────────┐   ┌──────────────┐    ┌──────────────┐   ┌──────────────┐
│ 1. 制定 RoE  │ │2. 主權算力審核│   │3. LVC 紅軍測試│    │4. RAG 降密稽核│   │5. 供應鏈後門 │
│人機授權邊界  │ │三層運算與民雄│   │VBS 4 / EADSIM│    │RBAC 與防洩漏 │   │開源與 SDK 審查│
└──────────────┘ └──────────────┘   └──────────────┘    └──────────────┘   └──────────────┘
```

## 🎯 國防 AIEC 五大核心任務

### 1. 制定交戰規則 (Rules of Engagement, RoE) 與自動化邊界
- 明訂全系統之授權等級：
  - **Human-in-the-loop (HITL / 人在紐中)**：最終火力打擊與目標授權必須由人類指揮官手動執行。
  - **Human-on-the-loop (HOTL / 人在紐上)**：人類具備實時監控與強制中斷權 (Abort Button)。
  - **Human-out-of-the-loop (HOOTL / 完全自主)**：僅限於蜂群無人機航路規劃、環境數據搜集等非致傷性任務。

### 2. 審核跨層級 AI 架構與主權基礎設施
- 審查邊緣 (Edge) - 霧端 (Fog) - 雲端 (Cloud) 三層架構。
- 確保如**民雄院區**等國家級算力節點在電力韌性、物理安全與演算法防禦符合最高軍規標準。

### 3. 策劃與執行 LVC 平行戰場紅軍測試 (Red Teaming)
- 於 VBS 4 / EADSIM 虛實整合 (LVC) 環境中導入對抗性攻擊測試，模擬電戰干擾與偽裝目標。

### 4. 研發與軍事資料集分級與 RAG 稽核
- 審查企業與國軍研發資料集探勘管線，嚴防 RAG 系統發生資訊降密 (Declassification Leakage)。

### 5. 供應鏈安全與模型授權審查
- 審查開源模型 (如 Gemma 4, Llama 3) 與第三方 SDK，確保無後門 (Backdoor) 且符合資料本地化要求。

## 🔗 关聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[AIEC 規範與治理雙支柱]]
- [[ISO 42001 人工智慧管理系統]]
- [[E類 - 自主系統與人機協同]]
- [[主權 AI 平台與四層 LLM 堆疊]]
