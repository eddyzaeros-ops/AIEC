---
title: AIEC 國防 AI 評測與認證體系筆記主索引 (MOC)
type: MOC
domain: Defense AI & Cyber Security
tags:
  - AIEC
  - MOC
  - DefenseAI
  - ISO42001
  - MITRE_ATLAS
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🛡️ AIEC 國防 AI 評測與認證體系筆記主索引 (Map of Content)

> [!NOTE]
> 本 MOC 匯集十年國防 AI 評測經驗與《國防領域 AI 應用需要哪些安全、保密與審計機制？ISO42001 及 AIEC 扮演的角色》研析精華，為獨立評測機構 (AIEC) 提供涵蓋**安全 (Security)、保密 (Confidentiality)、審計 (Auditing) 與治理 (Governance)** 的完整雙腦知識圖譜。

---

## 🗂️ 筆記五大主題分區

### 01. 治理、資安與標準 (Governance, Security & Standards)
- [[AIEC 規範與治理雙支柱]] - DAGR 指導原則與 SHIELD 治理循環
- [[SHIELD 治理循環活動]] - Set, Hone, Improve, Evaluate, Log, Detect 全生命週期
- [[ISO 42001 人工智慧管理系統]] - AIMS 國際管理框架與 AI 影響評估 (AIIA)
- [[MITRE ATLAS 人工智慧對抗威脅矩陣]] - 16 大戰術、170 項技術、32 項緩解與 CALDERA Arsenal
- [[RAG 權限控管與資料分級降密]] - RBAC 向量標籤與抗降密洩漏 (Anti-Declassification)
- [[國防 AIEC 核心任務與交戰規則 (RoE)]] - AIEC 5 大任務與人機權能邊界 (HITL/HOTL/HOOTL)

### 02. 矩陣、架構與評測 SOP (Matrices, Frameworks & Evaluation SOPs)
- [[T&E 四大能力層次]] - DoD Level 1~4 (模型、HSI、系統整合、作戰評測)
- [[JATIC 七大共通構面]] - 穩健性、韌性、可解釋性、勝任力、公平性、信任校準、漂移
- [[國防 AI 評測 6 大方法論與 SOP]] - 黑箱、白箱、基準、紅軍測試、專家評估、營運監控
- [[AIEC 15 項量化評測指標與 SOP]] - Q1~Q15 完整量化計算公式、Pass/Fail 門檻與工具鏈
- [[國防 AI 安全保密與審計三維矩陣]] - Security、Confidentiality、Auditing 聯防體系

### 03. 應用系統評測 SOP (System Category Evaluation SOPs)
- [[A類 - 電腦視覺與目標偵測]] - YOLO, Mobile SAM, 對抗貼片, NRTK, XAITK
- [[B類 - 生成式 AI 與大語言模型]] - GenAI, Prompt Injection, garak, NeMo Guardrails
- [[C類 - 檢索增強生成 RAG 系統]] - RAGAS Context Precision, TruLens Triad, Faithfulness
- [[D類 - AI Agent 與多代理協同系統]] - AgentBench, OPA 策略, SPIFFE/SPIRE 零信任軌跡
- [[E類 - 自主系統與人機協同]] - DoDD 3000.09, ToAST, HMT 信任校準, NASA-TLX 認知負荷
- [[F類 - 決策支援與預測分析]] - PyOD, 概念漂移, UQ 不確定性量化, XAI 特徵歸因

### 04. 地端架構、主權算力與邊緣安全 (On-Prem, Sovereign Compute & Edge Security)
- [[主權 AI 平台與四層 LLM 堆疊]] - Tier 1~4 算力堆疊與民雄院區國家級算力韌性
- [[地端 LLM 推論引擎與 Middleware 工具鏈]] - Ollama, vLLM, llama.cpp, GGUF, Gemma 4 LoRA
- [[Lattice 戰術 C2 架構與 Menace 邊緣算力節點]] - JADC2 網狀通訊與零信任 API 閘道
- [[戰術邊緣硬體安全與模型自毀機制]] - 無 GPS Mesh、防篡改 (Tamper-Resistance) 與緊急自毀
- [[聯邦學習 (Federated Learning) 國防保密策略]] - 「模型移動，資料不動」與梯度權重安全傳輸

---

## 🔍 Dataview 動態檢索範例

```dataview
TABLE type, domain, status, last_updated
FROM #AIEC
SORT file.name ASC
```
