# -*- coding: utf-8 -*-
import os

base = r'G:\我的雲端硬碟\secondbrain\AIEC'

dirs = [
    os.path.join(base, '00-Index_and_Templates'),
    os.path.join(base, '01-治理與規範'),
    os.path.join(base, '02-評測矩陣與構面'),
    os.path.join(base, '03-應用系統評測'),
    os.path.join(base, '04-地端架構與邊緣算力')
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

files = {}

# 1. MOC
files[os.path.join(base, '00-Index_and_Templates', 'AIEC 知識庫主索引 (MOC).md')] = '''---
title: AIEC 知識庫主索引 (MOC)
date: 2026-07-25
type: MOC
tags:
  - AIEC/MOC
  - AIEC/總覽
status: 穩定
---

# 🛡️ AIEC 國防與企業級 AI 評測與治理知識庫 (Map of Content)

歡迎來到 **AIEC (Artificial Intelligence Evaluation & Certification)** 雙腦知識庫！本知識庫整合國防級 AI 評測標準、JATIC 測試框架、SHIELD 治理引擎、ISO 42001 AIMS、MITRE ATLAS AI 威脅矩陣，以及主權 AI 地端部署與戰術 C2 架構。

---

## 🏛️ 1. 治理、安全與合規 (Governance & Security)
本區塊涵蓋 AIEC 的核心治理精神、風險評估指南與合規要求：
- [[AIEC 雙支柱與治理引擎]]：DAGR 風險指南與 SHIELD 六大循環
- [[SHIELD 六項治理循環活動]]：S-H-I-E-L-D 評估與偵測流程
- [[ISO 42001 人工智慧管理系統]]：AIMS 國際標準與 Annex A 控制項
- [[MITRE ATLAS 人工智慧威脅矩陣]]：對抗 ML 攻擊手段與防範
- [[RAG 權限控管與資料分級稽核]]：軍事技術資料防降密與 RBAC

---

## 📐 2. 評測矩陣與能力構面 (T&E Framework & Matrix)
跨系統的通用能力層級劃分與評測方法論：
- [[T&E 四大能力層次]]：Model、HSI、Systems、Operational 四層測試
- [[JATIC 七大共通評測構面]]：穩健性、韌性、可解釋性、勝任度、公平性、校準、漂移監控
- [[國防 AI 評測方法論與 SOP]]：黑箱、白箱、基準測試、紅隊演練、持續監控

---

## 🔬 3. 六大應用系統專屬評測 (Application System T&E)
針對不同 AI 系統型態的專用測試工具與風險評估 SOP：
- [[A類 - 電腦視覺與目標偵測評測]]：對抗貼片、NRTK、XAITK、IBM ART 360
- [[B類 - 生成式 AI 與大語言模型評測]]：越獄/注入防禦、garak、NeMo Guardrails
- [[C類 - 檢索增強生成 RAG 評測]]：脈絡忠實度、RAGAS、TruLens、Arize Phoenix
- [[D類 - AI Agent 與多代理系統評測]]：工具誤用、串接軌跡稽核、AgentBench、OPA 閘門
- [[E類 - 自主系統與人機協同評測]]：人機信任度、脱離停用、DoDD 3000.09、IDA HMT
- [[F類 - 決策支援與預測分析評測]]：概念漂移、不確定性量化、AIF360、SHAP/LIME

---

## 💻 4. 主權 AI 地端架構與邊緣算力 (Sovereign AI & Edge)
地端模型推論、多層堆疊與戰術 C2 平行戰場整合：
- [[主權 AI 平台與四層 LLM 堆疊]]：Tier 1~Tier 4 模型配置與白箱/黑箱測試劃分
- [[地端 LLM 推論引擎與工具鏈]]：Ollama、LM Studio、llama.cpp、vLLM、Hugging Face
- [[Lattice 戰術 C2 架構與 Menace 邊緣節點]]：雲邊端三層協同、Menace 加固節點與擊殺鏈自動化

---

## 📝 5. 筆記範本 (Templates)
- [[Template - 核心概念與治理筆記]]
- [[Template - 應用系統評測筆記]]
- [[Template - 部署與架構筆記]]
'''

# Templates
files[os.path.join(base, '00-Index_and_Templates', 'Template - 核心概念與治理筆記.md')] = '''---
title: "{{title}}"
date: {{date}}
type: 核心概念/治理規範
tags:
  - AIEC/治理
  - AIEC/安全
status: 穩定
---

# {{title}}

## 📌 概念定義與背景
> 簡述本概念或規範在國防/企業級 AIEC 評測體系中的定位與核心價值。

## ⚙️ 核心機制與運作流程
- 

## 🛡️ 關聯規範與標準 (Standards & Frameworks)
- [[ISO 42001 人工智慧管理系統]]
- [[MITRE ATLAS 人工智慧威脅矩陣]]

## 🔗 雙向鏈結與延伸考點
- **上層領域**：[[AIEC 雙支柱與治理引擎]]
- **評測對應**：[[JATIC 七大共通評測構面]]
- **下層應用**：
'''

files[os.path.join(base, '00-Index_and_Templates', 'Template - 應用系統評測筆記.md')] = '''---
title: "{{title}}"
date: {{date}}
type: 應用系統評測
tags:
  - AIEC/系統評測
status: 實測定案
---

# {{title}}

## 🎯 系統定位與主要威脅風險
- **系統類別**：
- **主要風險**：

## 🧪 評測方式與實施 SOP (T&E Methodology)
1. **測試類型**：（黑箱 / 白箱 / 對抗測試 / 基準測試）
2. **評測步驟**：

## 🛠️ 代表性評測工具鏈 (Testing Tools)
- 

## 🔗 雙向鏈結與矩陣對照
- **能力層次**：[[T&E 四大能力層次]]
- **共通構面**：[[JATIC 七大共通評測構面]]
- **架構搭配**：[[主權 AI 平台與四層 LLM 堆疊]]
'''

files[os.path.join(base, '00-Index_and_Templates', 'Template - 部署與架構筆記.md')] = '''---
title: "{{title}}"
date: {{date}}
type: 技術架構/地端部署
tags:
  - AIEC/地端架構
  - AIEC/邊緣算力
status: 實測定案
---

# {{title}}

## 🏗️ 架構概覽與實體載體
> 說明本架構/工具地端部署模式、硬體要求與傳輸邊界。

## 🔑 技術特徵與能力指標
- 

## 🛡️ 安全與審計防線 (Security & Audit)
- 

## 🔗 雙向鏈結 (Bidirectional Links)
- **治理連結**：[[RAG 權限控管與資料分級稽核]]
- **系統對接**：[[Lattice 戰術 C2 架構與 Menace 邊緣節點]]
'''

# 01-治理與規範
files[os.path.join(base, '01-治理與規範', 'AIEC 雙支柱與治理引擎.md')] = '''---
title: AIEC 雙支柱與治理引擎
date: 2026-07-25
type: 核心概念/治理規範
tags:
  - AIEC/治理
  - AIEC/雙支柱
status: 穩定
---

# 🛡️ AIEC 雙支柱與治理引擎

## 📌 概念定義與背景
AIEC (Artificial Intelligence Evaluation & Certification) 國防與企業級 AI 治理體系以 **DAGR Risk Guidelines**（風險指南）與 **SHIELD 治理引擎** 作為整體治理的核心雙支柱。旨在確保人工智慧系統具備 Responsible（治理正當性）與 Trustworthy（技術可驗證性）。

---

## ⚙️ 核心雙支柱結構

### 1. DAGR 風險指南 (DAGR Risk Guidelines)
- 提供 AI 生命週期中的風險識別矩陣與危害防範指引。
- 定義高風險與安全關鍵 (Safety-Critical) AI 任務的審查門檻。
- 連結 [[ISO 42001 人工智慧管理系統]] 之風險控制規範與偏護稽核。

### 2. SHIELD 治理引擎 (Governance Engine)
SHIELD 是引導 AI 系統全生命週期的 6 項循環活動：
- **S** - Set Foundations（設定基礎）
- **H** - Hone Operationalizations（精煉操作化）
- **I** - Improve & Innovate（改進與創新）
- **E** - Evaluate Status（評估狀態）
- **L** - Log for Traceability（記錄可追溯性）
- **D** - Detect via Monitoring（持續監控偵測）

詳細每項活動請見 [[SHIELD 六項治理循環活動]]。

---

## 🛡️ 關聯規範與標準
- **國際標準**：[[ISO 42001 人工智慧管理系統]]
- **威脅防範**：[[MITRE ATLAS 人工智慧威脅矩陣]]

## 🔗 雙向鏈結與延伸考點
- **上層總覽**：[[AIEC 知識庫主索引 (MOC)]]
- **細節活動**：[[SHIELD 六項治理循環活動]]
- **評測貫穿**：[[JATIC 七大共通評測構面]]
- **資料稽核**：[[RAG 權限控管與資料分級稽核]]
'''

files[os.path.join(base, '01-治理與規範', 'SHIELD 六項治理循環活動.md')] = '''---
title: SHIELD 六項治理循環活動
date: 2026-07-25
type: 核心概念/治理規範
tags:
  - AIEC/治理
  - AIEC/SHIELD
status: 穩定
---

# 🔄 SHIELD 六項治理循環活動

## 📌 概念定義與背景
SHIELD 是 [[AIEC 雙支柱與治理引擎]] 中的動態治理引擎，透過 6 個連續階段確保 AI 系統從研發、營運到退役過程皆具備可追溯性與可檢驗性。

---

## ⚙️ SHIELD 六大活動拆解

| 代碼 | 活動名稱 | 核心內容與產出 | 關聯規範/工具 |
|---|---|---|---|
| **S** | Set Foundations (設定基礎) | 辨識 Responsible AI (RAI)、法律、政策基礎與 SOC | [[ISO 42001 人工智慧管理系統]] |
| **H** | Hone Operationalizations (精煉操作化) | 將政策轉化為具體的評估計畫與量化指標 | [[T&E 四大能力層次]] |
| **I** | Improve & Innovate (改進與創新) | 運用風險緩解工具 (Mitigation Tools) 處理 SOC 關切事項 | [[國防 AI 評測方法論與 SOP]] |
| **E** | Evaluate Status (評估狀態) | 綜合評估基礎滿足度與危害解決程度 | [[JATIC 七大共通評測構面]] |
| **L** | Log for Traceability (記錄可追溯性) | 全程文件化，記錄數據與模型權重演進歷史 | CMMC L2 稽核 / [[RAG 權限控管與資料分級稽核]] |
| **D** | Detect via Monitoring (持續監控偵測) | 上線後監控效能衰減與數據漂移 (Data Drift) | [[F類 - 決策支援與預測分析評測]] |

---

## 🔗 雙向鏈結
- **核心架構**：[[AIEC 雙支柱與治理引擎]]
- **國際合規**：[[ISO 42001 人工智慧管理系統]]
- **評測方法**：[[國防 AI 評測方法論與 SOP]]
'''

files[os.path.join(base, '01-治理與規範', 'ISO 42001 人工智慧管理系統.md')] = '''---
title: ISO 42001 人工智慧管理系統
date: 2026-07-25
type: 核心概念/治理規範
tags:
  - AIEC/治理
  - AIEC/ISO42001
status: 穩定
---

# 📜 ISO 42001 人工智慧管理系統 (AIMS)

## 📌 概念定義與背景
ISO/IEC 42001 是全球第一個針對人工智慧管理系統 (Artificial Intelligence Management System, AIMS) 的國際可驗證標準。在 AIEC 體系中，ISO 42001 為組織提供了內部控制、風險管理與倫理治理的制度化框架。

---

## ⚙️ 核心控制項與 AIEC 對照

1. **AI 風險評估與處置 (Clause 6.1.2)**：
   - 強調對 AI 系統的全生命週期進行威脅建模。
   - 對接 [[MITRE ATLAS 人工智慧威脅矩陣]] 進行對抗攻擊評估。

2. **公平性與偏見稽核 (Annex A Control)**：
   - 審查訓練數據與模型輸出，防止隱性偏見與過度擬合。
   - 結合 ISO 22989 AI 概念與術語標準。

3. **透明度與可解釋性 (Clause 8.4)**：
   - 要求 AI 決策過程可被審計與追溯。
   - 搭配 [[A類 - 電腦視覺與目標偵測評測]] 之 XAITK 顯核演算法與 [[F類 - 決策支援與預測分析評測]] 之 SHAP/LIME 工具。

4. **持續監控與績效評估 (Clause 9)**：
   - 對應 [[SHIELD 六項治理循環活動]] 中的 Detect via Monitoring 階段。

---

## 🔗 雙向鏈結
- **治理引擎**：[[AIEC 雙支柱與治理引擎]]
- **威脅對照**：[[MITRE ATLAS 人工智慧威脅矩陣]]
- **資料稽核**：[[RAG 權限控管與資料分級稽核]]
'''

files[os.path.join(base, '01-治理與規範', 'MITRE ATLAS 人工智慧威脅矩陣.md')] = '''---
title: MITRE ATLAS 人工智慧威脅矩陣
date: 2026-07-25
type: 核心概念/治理規範
tags:
  - AIEC/安全
  - AIEC/ATLAS
status: 穩定
---

# ⚔️ MITRE ATLAS 人工智慧威脅矩陣

## 📌 概念定義與背景
MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) 是專為 AI/ML 系統打造的資安威脅框架，與傳統 IT 的 MITRE ATT&CK 形成補強與比較。

---

## 📊 ATT&CK vs. ATLAS 對比矩陣

| 構面 | MITRE ATT&CK | MITRE ATLAS |
|---|---|---|
| **關注對象** | 傳統 IT 系統與網絡 | AI/ML 模型、管道與推論系統 |
| **攻擊面** | 網路、端點、雲端主機 | ML 模型權重、訓練數據、Prompt、RAG 向量庫 |
| **典型攻擊** | Privilege Escalation, Lateral Movement | Data Poisoning, Jailbreak, Model Inversion, Adversarial Patch |
| **定位** | 網路安全威脅框架 | AI 安全與對抗攻防威脅框架 |

---

## 🎯 國防 AI 主要 ATLAS 戰術與攻擊範例

1. **對抗干擾 (Adversarial Perturbation)**：
   - 敵方在裝甲車或誘餌上貼附特殊對抗圖樣（Adversarial Patch），使 AI 目標辨識失效。
   - 對應處置見 [[A類 - 電腦視覺與目標偵測評測]]。

2. **提示越獄與注入 (Prompt Injection)**：
   - 敵方透過自然語言輸入繞過 LLM 安全護欄。
   - 對應處置見 [[B類 - 生成式 AI 與大語言模型評測]]（garak / NeMo Guardrails）。

3. **經檢索注入 (Direct/Indirect RAG Injection)**：
   - 在檢索數據庫中植入對抗指令，操控 RAG 產出。
   - 對應處置見 [[C類 - 檢索增強生成 RAG 評測]] 與 [[RAG 權限控管與資料分級稽核]]。

---

## 🔗 雙向鏈結
- **國際標準**：[[ISO 42001 人工智慧管理系統]]
- **視覺防禦**：[[A類 - 電腦視覺與目標偵測評測]]
- **LLM 防禦**：[[B類 - 生成式 AI 與大語言模型評測]]
- **RAG 資安**：[[RAG 權限控管與資料分級稽核]]
'''

files[os.path.join(base, '01-治理與規範', 'RAG 權限控管與資料分級稽核.md')] = '''---
title: RAG 權限控管與資料分級稽核
date: 2026-07-25
type: 核心概念/治理規範
tags:
  - AIEC/治理
  - AIEC/RAG權限
status: 穩定
---

# 🔐 RAG 權限控管與資料分級稽核

## 📌 概念定義與背景
在國防與企業級 AI 應用中，針對研發技術文件與機密數據的自動化檢索增強生成 (RAG) 系統，AIEC 要求嚴格審查檢索管道與 LLM 權限，防止出現「數據降密」或越權檢索漏洞。

---

## ⚙️ 核心審計機制

1. **基於角色的存取控制 (RBAC) 於向量資料庫**：
   - 在 Embedding Vector 存儲層附加密級 Tag（機密、極機密、限制級）。
   - 確保 Query 執行時，檢索管道強制查驗用戶與 Agent 證書。

2. **防止 LLM 摘要引發降密 (De-classification Leakage)**：
   - 雖然單一句子可能未達密級，但 LLM 將多篇限制級文件統整後可能形成機密內容，需設定輸出遮罩 (Output Masking)。

3. **供應鏈安全與模型授權審查**：
   - 審查開源 Embedder 模型與向量庫（如 Milvus, Qdrant）無後門風險。

---

## 🔗 雙向鏈結
- **RAG評測**：[[C類 - 檢索增強生成 RAG 評測]]
- **Agent控管**：[[D類 - AI Agent 與多代理系統評測]]
- **合規稽核**：[[ISO 42001 人工智慧管理系統]]
- **地端部署**：[[主權 AI 平台與四層 LLM 堆疊]]
'''

# 02-評測矩陣與構面
files[os.path.join(base, '02-評測矩陣與構面', 'T&E 四大能力層次.md')] = '''---
title: T&E 四大能力層次
date: 2026-07-25
type: 評測矩陣與構面
tags:
  - AIEC/評測矩陣
  - AIEC/TEVV
status: 穩定
---

# 📐 T&E 四大能力層次 (Capability Axes)

## 📌 概念定義與背景
國防 AI 評測 (T&E / TEVV) 框架將評測能力分為由底層至頂層的四個構面，確保 AI 系統不僅單體演算法精確，在人機協同與實戰環境中亦能穩定運作。

---

## 📊 四大能力層次架構

| 層次 | 名稱 | 測試焦點 | 核心評測內容 | 對應系統 |
|---|---|---|---|---|
| **Level 1** | **Model T&E (模型測評)** | 單體模型演算法 | 效能、對抗攻防、校準度、可解釋性、偏見分析 | A類 CV、B類 LLM、F類 預測 |
| **Level 2** | **HSI T&E (人機整合測評)** | Human-Systems Integration | 介面適配、認知負荷 (Cognitive Load)、信任度、過度依賴 | C類 RAG、E類 人機協同 |
| **Level 3** | **Systems Integration T&E (系統整合測評)** | 端到端系統交互 | 數據鏈串接、元件交互、API 閘道穩定度、異常中斷 | D類 Agent、F類 決策支援 |
| **Level 4** | **Operational T&E (作戰測評)** | 實戰與複雜動態環境 | 電戰干擾適應力、環境漂移韌性、緊急脱離與停用機制 | E類 自主系統、Lattice 戰術 C2 |

---

## 🔗 雙向鏈結
- **共通構面**：[[JATIC 七大共通評測構面]]
- **方法論**：[[國防 AI 評測方法論與 SOP]]
- **應用對應**：[[A類 - 電腦視覺與目標偵測評測]] 至 [[F類 - 決策支援與預測分析評測]]
'''

files[os.path.join(base, '02-評測矩陣與構面', 'JATIC 七大共通評測構面.md')] = '''---
title: JATIC 七大共通評測構面
date: 2026-07-25
type: 評測矩陣與構面
tags:
  - AIEC/評測矩陣
  - AIEC/JATIC
status: 穩定
---

# 🎯 JATIC 七大共通評測構面

## 📌 概念定義與背景
由 JATIC (Joint AI Test Center) 與 AIEC 共同確立的 7 項跨系統共通評測指標，是所有 AI 應用系統在進行測試與認證時的通用維度。

---

## ⚙️ 七大構面詳解

1. **穩健性 (Robustness)**：
   - 系統在面對噪聲、分布外 (OOD) 輸入與對抗樣本時維持效能的能力。

2. **韌性 (Resiliency)**：
   - 系統受到網路攻擊或電戰干擾時，能否自動降級或安全復原。

3. **可解釋性 (Explainability)**：
   - 提供特徵歸因 (Feature Attribution) 與顯著圖，防止「黑盒子」效應。

4. **勝任度 (Competence)**：
   - 系統在其指定作戰邊界內的任務完成率與精度。

5. **公平性 (Fairness)**：
   - 防範訓練數據中的隱性偏見與群體偏差。

6. **校準 (Calibration)**：
   - 信心度 (Confidence Score) 與實際正確率的符合程度，防止高信心低精確度錯誤。

7. **漂移監控 (Drift Monitoring)**：
   - 上線後持續追蹤概念漂移 (Concept Drift) 與數據漂移。

---

## 🔗 雙向鏈結
- **能力層級**：[[T&E 四大能力層次]]
- **方法論**：[[國防 AI 評測方法論與 SOP]]
- **決策應用**：[[F類 - 決策支援與預測分析評測]]
'''

files[os.path.join(base, '02-評測矩陣與構面', '國防 AI 評測方法論與 SOP.md')] = '''---
title: 國防 AI 評測方法論與 SOP
date: 2026-07-25
type: 評測矩陣與構面
tags:
  - AIEC/方法論
  - AIEC/SOP
status: 穩定
---

# 🧪 國防 AI 評測方法論與 SOP

## 📌 概念定義與背景
AIEC 規範了 6 種互補的評測方法，對應不同的系統層級與模型開源狀態（地端白箱 vs 雲端黑箱）。

---

## ⚙️ 6 大評測方式與匹配矩陣

| 方法 | 運作邏輯 | 適用場景/系統 | 代表工具 |
|---|---|---|---|
| **黑箱測試 (Black-box)** | 不存取內部權重，評測輸入與輸出 | 雲端 Tier-4 API 模型 (Gated Claude) | garak, PromptBench |
| **白箱測試 (White-box)** | 存取梯度、中間特徵圖與特徵歸因 | 地端 Gemma 4 各層模型 | XAITK, SHAP |
| **基準測試 (Benchmarking)** | 使用標準化數據集進行量化比對 | 評估基礎能力與可重現性 | AgentBench, TrustLLM |
| **對抗/紅隊 (Red Teaming)** | 模擬敵方進行干擾、越獄與模糊測試 | 安全關鍵系統 (Safety-critical) | IBM ART 360, HEART |
| **人工評估 (Human Eval)** | 無明確真相 (Ground Truth) 時的評估 | 生成式 AI、人機協同 Trust | HMT Guidebook |
| **持續監控 (Continuous)** | 上線後自動偵測數據漂移與性能下降 | SHIELD Detect 階段 | Arize Phoenix, PyOD |

---

## 🔗 雙向鏈結
- **能力劃分**：[[T&E 四大能力層次]]
- **治理階段**：[[SHIELD 六項治理循環活動]]
- **模型對應**：[[主權 AI 平台與四層 LLM 堆疊]]
'''

# 03-應用系統評測
files[os.path.join(base, '03-應用系統評測', 'A類 - 電腦視覺與目標偵測評測.md')] = '''---
title: A類 - 電腦視覺與目標偵測評測
date: 2026-07-25
type: 應用系統評測
tags:
  - AIEC/系統評測
  - AIEC/ComputerVision
status: 實測定案
---

# 👁️ A類 - 電腦視覺與目標偵測評測 (CV & Target Detection)

## 🎯 系統定位與主要威脅風險
- **系統類別**：邊緣視覺辨識、戰術無人機目標偵測、衛星圖像分割。
- **主要風險**：
  1. 對抗貼片 (Adversarial Patch) 干擾。
  2. 自然穩健性下降 (雨雪、煙霧、電戰雜訊導致 mAP 暴降)。
  3. 分布外 (OOD) 偽裝目標誤判。

---

## 🧪 評測 SOP 與工具鏈

### 評測方式
- **白箱/黑箱對抗攻防**：測試對抗干擾下目標框 (Bounding Box) 穩定度。
- **顯著性可解釋性**：產出 Heatmap 確保模型專注於目標本體而非背景特徵。

### 代表性工具鏈
- **HEART** (High-Explosive Adversarial Red Teaming)
- **NRTK** (Natural Robustness Toolkit)
- **XAITK** (Explainable AI Toolkit)
- **IBM ART 360** (Adversarial Robustness Toolbox)

---

## 🔗 雙向鏈結
- **能力層級**：[[T&E 四大能力層次]] (Model T&E Focus)
- **威脅對映**：[[MITRE ATLAS 人工智慧威脅矩陣]]
- **邊緣硬體**：[[Lattice 戰術 C2 架構與 Menace 邊緣節點]]
'''

files[os.path.join(base, '03-應用系統評測', 'B類 - 生成式 AI 與大語言模型評測.md')] = '''---
title: B類 - 生成式 AI 與大語言模型評測
date: 2026-07-25
type: 應用系統評測
tags:
  - AIEC/系統評測
  - AIEC/LLM
status: 實測定案
---

# 💬 B類 - 生成式 AI 與大語言模型評測 (GenAI & LLM)

## 🎯 系統定位與主要威脅風險
- **系統類別**：情報摘要生成、指管輔助對答、軍事文案草擬。
- **主要風險**：
  1. 幻覺 (Hallucination) 與虛構數據。
  2. 越獄 (Jailbreak) 與 Prompt 注入攻擊。
  3. 毒性偏見與敏感資料洩露。

---

## 🧪 評測 SOP 與工具鏈

### 評測方式
- **紅隊模糊測試 (Red-teaming Fuzzing)**：自動發送萬筆越獄 Payload。
- **護欄驗證 (Guardrails Verification)**：測試 NeMo 護欄拦截成功率。

### 代表性工具鏈
- **garak** (LLM Vulnerability Scanner)
- **NeMo Guardrails** (NVIDIA 輸出入護欄)
- **PromptBench** & **TrustLLM**

---

## 🔗 雙向鏈結
- **能力層級**：[[T&E 四大能力層次]]
- **地端堆疊**：[[主權 AI 平台與四層 LLM 堆疊]]
- **推論工具**：[[地端 LLM 推論引擎與工具鏈]]
'''

files[os.path.join(base, '03-應用系統評測', 'C類 - 檢索增強生成 RAG 評測.md')] = '''---
title: C類 - 檢索增強生成 RAG 評測
date: 2026-07-25
type: 應用系統評測
tags:
  - AIEC/系統評測
  - AIEC/RAG
status: 實測定案
---

# 📚 C類 - 檢索增強生成 RAG 評測 (Retrieval-Augmented Generation)

## 🎯 系統定位與主要威脅風險
- **系統類別**：軍規技術手冊檢索、準則庫對答、後勤料號查詢。
- **主要風險**：
  1. 知識衝突 (Knowledge Conflict) 與檢索不相關內容。
  2. 經檢索注入 (Retrieved Injection)。
  3. 來源歸屬錯誤 (Source Attribution Error)。

---

## 🧪 評測 SOP 與工具鏈

### 評測指標 (RAG Triad)
- **脈絡精確度 (Context Precision)**
- **忠實度 (Faithfulness)**
- **答案相關度 (Answer Relevance)**

### 代表性工具鏈
- **RAGAS** (RAG Assessment)
- **TruLens**
- **Arize Phoenix** (Tracing & Evaluation)

---

## 🔗 雙向鏈結
- **資料稽核**：[[RAG 權限控管與資料分級稽核]]
- **合規要求**：[[ISO 42001 人工智慧管理系統]]
- **下階段 Agent**：[[D類 - AI Agent 與多代理系統評測]]
'''

files[os.path.join(base, '03-應用系統評測', 'D類 - AI Agent 與多代理系統評測.md')] = '''---
title: D類 - AI Agent 與多代理系統評測
date: 2026-07-25
type: 應用系統評測
tags:
  - AIEC/系統評測
  - AIEC/Agent
status: 實測定案
---

# 🤖 D類 - AI Agent 與多代理系統評測 (Multi-Agent System)

## 🎯 系統定位與主要威脅風險
- **系統類別**：自主任務規劃 Agent、跨系統 API 呼叫代理、多 Agent 協同攻擊防禦。
- **主要風險**：
  1. 工具誤用 (Tool Misuse) 與非法 API 調用。
  2. 目標偏移 (Goal Drift) 與死迴圈。
  3. 串接軌跡錯誤累積與 Agent 間衝突。

---

## 🧪 評測 SOP 與工具鏈

### 評測方式
- **軌跡稽核 (Trajectory Auditing)**：記錄 API 呼叫鏈。
- **HITL (Human-in-the-Loop) 閘門測試**：驗證關鍵授權點。

### 代表性工具鏈
- **AgentBench**
- **SPIFFE/SPIRE** (Agent 身份驗證)
- **Open Policy Agent (OPA)** 策略閘門

---

## 🔗 雙向鏈結
- **能力層級**：[[T&E 四大能力層次]] (Systems Integration Focus)
- **戰術 C2**：[[Lattice 戰術 C2 架構與 Menace 邊緣節點]]
- **RAG基礎**：[[C類 - 檢索增強生成 RAG 評測]]
'''

files[os.path.join(base, '03-應用系統評測', 'E類 - 自主系統與人機協同評測.md')] = '''---
title: E類 - 自主系統與人機協同評測
date: 2026-07-25
type: 應用系統評測
tags:
  - AIEC/系統評測
  - AIEC/HMT
status: 實測定案
---

# 🚁 E類 - 自主系統與人機協同評測 (Human-Autonomy Teaming / HMT)

## 🎯 系統定位與主要威脅風險
- **系統類別**：無人機蜂群人機協同、自主車輛、戰略開火授權。
- **主要風險**：
  1. 非預期自主行為與無法緊急脱離/停用 (Emergency Abort Failure)。
  2. 操作員過度依賴 (Over-reliance) 或信任不足。
  3. 認知負荷過載。

---

## 🧪 評測 SOP 與工具鏈

### 評測規範
- 遵循 **DoDD 3000.09** (Autonomy in Weapon Systems) 美軍自主武器指令。

### 代表性工具鏈
- **ToAST** (Testing of Autonomous Systems Tool)
- **IDA HMT Guidebook**
- **MIT-LL HMT Testing Guide**

---

## 🔗 雙向鏈結
- **能力層級**：[[T&E 四大能力層次]] (Operational & HSI Focus)
- **Agent協同**：[[D類 - AI Agent 與多代理系統評測]]
- **C2整合**：[[Lattice 戰術 C2 架構與 Menace 邊緣節點]]
'''

files[os.path.join(base, '03-應用系統評測', 'F類 - 決策支援與預測分析評測.md')] = '''---
title: F類 - 決策支援與預測分析評測
date: 2026-07-25
type: 應用系統評測
tags:
  - AIEC/系統評測
  - AIEC/DecisionSupport
status: 實測定案
---

# 📈 F類 - 決策支援與預測分析評測 (Predictive Analytics)

## 🎯 系統定位與主要威脅風險
- **系統類別**：後勤供應鏈預測、威脅等級排序、兵棋推演勝率分析。
- **主要風險**：
  1. 數據與概念漂移 (Concept Drift)。
  2. 不確定性未量化 (Unquantified Uncertainty)。
  3. 隱性群體偏見。

---

## 🧪 評測 SOP 與工具鏈

### 評測方式
- **漂移偵測與 OOD 測試**
- **不確定性量化 (UQ)**

### 代表性工具鏈
- **AIF360** (AI Fairness 360)
- **PyOD** / **Alibi Detect**
- **SHAP** / **LIME** (特徵歸因)

---

## 🔗 雙向鏈結
- **共通構面**：[[JATIC 七大共通評測構面]]
- **監控階段**：[[SHIELD 六項治理循環活動]]
- **CV對照**：[[A類 - 電腦視覺與目標偵測評測]]
'''

# 04-地端架構與邊緣算力
files[os.path.join(base, '04-地端架構與邊緣算力', '主權 AI 平台與四層 LLM 堆疊.md')] = '''---
title: 主權 AI 平台與四層 LLM 堆疊
date: 2026-07-25
type: 技術架構/地端部署
tags:
  - AIEC/地端架構
  - AIEC/LLMStack
status: 實測定案
---

# 🏰 主權 AI 平台與四層 LLM 堆疊

## 📌 概念定義與背景
為確保國防安全與數據本地化，主權 AI 平台部署採用四層 LLM 軟硬體堆疊，並明確劃分白箱對抗測試與黑箱基準測試的適用範圍。

---

## 🧱 四層 LLM 堆疊架構

| 層級 | 模型規格 | 運算硬體環境 | 評測方式配置 |
|---|---|---|---|
| **Tier 1** | Gemma 4 31B Dense | NVIDIA H200 / CUDA | **白箱測試** + 對抗紅隊 |
| **Tier 2** | Gemma 4 26B MoE | AMD MI325X / ROCm | **白箱測試** + 對抗紅隊 |
| **Tier 3** | Gemma 4 E4B (邊緣端) | 本地推論 (Menace 節點) | **白箱測試** + 基準測試 |
| **Tier 4** | 雲端 Gated Claude API | HITL 核准閘門 | **黑箱測試** + 基準測試 |

---

## 🔗 雙向鏈結
- **推論工具**：[[地端 LLM 推論引擎與工具鏈]]
- **戰術節點**：[[Lattice 戰術 C2 架構與 Menace 邊緣節點]]
- **評測對應**：[[國防 AI 評測方法論與 SOP]]
'''

files[os.path.join(base, '04-地端架構與邊緣算力', '地端 LLM 推論引擎與工具鏈.md')] = '''---
title: 地端 LLM 推論引擎與工具鏈
date: 2026-07-25
type: 技術架構/地端部署
tags:
  - AIEC/地端架構
  - AIEC/InferenceEngine
status: 實測定案
---

# ⚙️ 地端 LLM 推論引擎與工具鏈

## 📌 概念定義與背景
地端模型推論工具鏈是連接底層硬體 (GPU/NPU) 與上層大語言模型的關鍵 Middleware，提供離線推論、GGUF 量化與 API Gateway 服務。

---

## 🛠️ 地端工具對比與定位

- **Ollama**：極簡指令集，專為開發者與 Docker 容器化設計，支援 Modelfile 自訂。
- **LM Studio**：精美桌面視窗 GUI，適合快速搜尋下載 Hugging Face GGUF 模型進行測試。
- **llama.cpp**：地端 LLM 推論底層核心 C++ 引擎，效能最高。
- **vLLM**：企業生產環境 High-Throughput 推論框架，支援 PagedAttention。
- **Hugging Face Hub**：模型圖書館，權重來源。

---

## 🔗 雙向鏈結
- **主權堆疊**：[[主權 AI 平台與四層 LLM 堆疊]]
- **RAG整合**：[[C類 - 檢索增強生成 RAG 評測]]
'''

files[os.path.join(base, '04-地端架構與邊緣算力', 'Lattice 戰術 C2 架構與 Menace 邊緣節點.md')] = '''---
title: Lattice 戰術 C2 架構與 Menace 邊緣節點
date: 2026-07-25
type: 技術架構/地端部署
tags:
  - AIEC/邊緣算力
  - AIEC/LatticeC2
status: 實測定案
---

# ⚡ Lattice 戰術 C2 架構與 Menace 邊緣節點

## 📌 概念定義與背景
Lattice 是軟體定義的戰術指揮管制 (C2) 架構，結合 **Menace 戰術加固邊緣硬體節點**，實現雲-邊-端三層協同與擊殺鏈 (Kill Chain) 自動化。

---

## 🏛️ 雲-邊-端三層協同架構

1. **雲端 (Cloud Hub)**：
   - 負責大模型訓練、知識蒸餾與全球情報融合。
2. **邊端 (Menace Edge Node)**：
   - 全地形戰術加固硬體，支援 Mesh 無線網絡，運行 Tier-3 輕量化模型 (如 Gemma 4 E4B)，進行實時目標識別與威脅排序。
3. **端端 (Terminal Sensors/Shooters)**：
   - 無人機、感測器與火器載具。

---

## 🔗 雙向鏈結
- **主權堆疊**：[[主權 AI 平台與四層 LLM 堆疊]]
- **視覺評測**：[[A類 - 電腦視覺與目標偵測評測]]
- **Agent協同**：[[D類 - AI Agent 與多代理系統評測]]
- **自主評測**：[[E類 - 自主系統與人機協同評測]]
'''

written_count = 0
for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    written_count += 1

print(f'Successfully created all {written_count} Markdown notes!')
