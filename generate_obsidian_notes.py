# -*- coding: utf-8 -*-
import os, sys

VAULT_PRIMARY = r'G:\我的雲端硬碟\secondbrain\AIEC'
VAULT_WORKSPACE = r'c:\Users\administartor\Downloads\AIEC\vault'

def ensure_dirs():
    subdirs = [
        '00-Index_and_Templates',
        '01-治理與標準',
        '02-矩陣與架構',
        '03-應用系統與SOP',
        '04-地端架構與工具'
    ]
    for root in [VAULT_PRIMARY, VAULT_WORKSPACE]:
        for sd in subdirs:
            os.makedirs(os.path.join(root, sd), exist_ok=True)

def write_note(folder, filename, content):
    p1 = os.path.join(VAULT_PRIMARY, folder, filename)
    p2 = os.path.join(VAULT_WORKSPACE, folder, filename)
    with open(p1, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    with open(p2, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Written: [{folder}] {filename}")

def build_all_notes():
    ensure_dirs()

    # ---------------------------------------------------------
    # 00-Index_and_Templates / AIEC 筆記主索引 (MOC).md
    # ---------------------------------------------------------
    write_note('00-Index_and_Templates', 'AIEC 筆記主索引 (MOC).md', """---
title: AIEC 國防 AI 評測與認證體系筆記主索引 (MOC)
type: MOC
domain: Defense AI & Cyber Security
tags:
  - AIEC
  - MOC
  - DefenseAI
  - ISO42001
  - MITRE_ATLAS
  - NCSIST
author: AIEC Defense Expert Team
version: 3.0
last_updated: 2026-07-26
status: Complete
---

# 🛡️ AIEC 國防 AI 評測與認證體系筆記主索引 (Map of Content)

> [!NOTE]
> 本 MOC 匯集十年國防 AI 評測經驗、NCSIST AIEC 總體架構圖 (`AIEC_1.pptx`) 與《國防領域 AI 應用需要哪些安全、保密與審計機制？ISO42001 及 AIEC 扮演的角色》研析精華，為國家中山科學研究院 (NCSIST) 與獨立評測機構 (AIEC) 提供涵蓋**安全 (Security)、保密 (Confidentiality)、審計 (Auditing) 與治理 (Governance)** 的完整雙腦知識圖譜。

---

## 🗂️ 筆記五大主題分區

### 01. 治理、資安與標準 (Governance, Security & Standards)
- [[NCSIST AIEC 國防 AI 評測與認證總體架構]] - **[主圖解析]** 剖析 NCSIST AIEC 總藍圖、代碼注入/數據污染防禦與 5 大底層戰術柱石
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
- [[聯邦學習 (Federated Learning) 國防保密策略]] - **[主圖元素]**「模型移動，資料不動」與參數融合在地
- [[地端模型蒸餾、資料與模型溯源 SOP]] - **[主圖元素]** Edge 端模型蒸餾、清洗規則、Data & Model Provenance 追溯與 Confidence Score

---

## 🔍 Dataview 動態檢索範例

```dataview
TABLE type, domain, status, last_updated
FROM #AIEC
SORT file.name ASC
```
""")

    # ---------------------------------------------------------
    # 00-Index_and_Templates / Templates
    # ---------------------------------------------------------
    write_note('00-Index_and_Templates', 'Template - 核心觀念與治理筆記.md', """---
title: "{{title}}"
type: Governance Note
domain: Defense AI & Governance
tags:
  - AIEC
  - Governance
author: AIEC Team
version: 1.0
last_updated: "{{date}}"
status: Draft
---

# {{title}}

## 📌 核心定義與國防範疇

## 🛡️ 治理規範與條款對齊

## 🧪 審計機制與資安控制點

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[AIEC 規範與治理雙支柱]]
""")

    write_note('00-Index_and_Templates', 'Template - 矩陣與架構筆記.md', """---
title: "{{title}}"
type: Architecture Note
domain: Defense AI & Frameworks
tags:
  - AIEC
  - Architecture
author: AIEC Team
version: 1.0
last_updated: "{{date}}"
status: Draft
---

# {{title}}

## 📐 矩陣結構與架構圖解

## 📊 評測構面與量化指標

## 🛡️ 國防實施作業程序 (SOP)

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[AIEC 15 項量化評測指標與 SOP]]
""")

    write_note('00-Index_and_Templates', 'Template - 應用系統與對抗攻防筆記.md', """---
title: "{{title}}"
type: Application System SOP
domain: Defense System SOP
tags:
  - AIEC
  - SystemSOP
  - RedTeaming
author: AIEC Team
version: 1.0
last_updated: "{{date}}"
status: Draft
---

# {{title}}

## 📌 系統範疇與核心威脅 (ATLAS / OWASP)

## 🧮 代表性量化指標與數學公式

## 🧪 紅軍測試 (Red Teaming) 與驗測工具鏈

## 🛡️ 合格判定門檻與審計日誌

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[MITRE ATLAS 人工智慧對抗威脅矩陣]]
""")

    # ---------------------------------------------------------
    # 01-治理與標準 (7 Notes)
    # ---------------------------------------------------------
    write_note('01-治理與標準', 'NCSIST AIEC 國防 AI 評測與認證總體架構.md', """---
title: NCSIST AIEC 國防 AI 評測與認證總體架構
type: Core Blueprint Note
domain: NCSIST Defense Architecture
tags:
  - AIEC
  - NCSIST
  - Architecture
  - ISO42001
  - ActiveDefense
author: AIEC Defense Expert Team
version: 1.0
last_updated: 2026-07-26
status: Complete
---

# 🏛️ NCSIST AIEC 國防 AI 評測與認證總體架構藍圖

> [!IMPORTANT]
> 本筆記專門研析 **NCSIST (國家中山科學研究院)** AIEC 總體架構圖 (`AIEC_1.pptx`)，解構國家級國防 AI 評測體系運作模式。

```
                  ┌──────────────────────────────────────────────┐
                  │    NCSIST 國防 AI 評測與認證總體架構 (AIEC)  │
                  └──────────────────────┬───────────────────────┘
                                         │
 ┌───────────────────────┬───────────────┴───────────────┬───────────────────────┐
 ▼                       ▼                               ▼                       ▼
┌──────────────────┐  ┌──────────────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  一、威脅與防禦  │  │  二、底層五大戰術 SOP 柱石  │  │  三、地端與邊緣  │  │  四、規範與標準  │
├──────────────────┤  ├──────────────────────────┤  ├──────────────────┤  ├──────────────────┤
│ • 代碼注入 (Code)│  │ 1. 擬定 ROE 交戰規則      │  │ • 地端模型蒸餾   │  │ • ISO 42001 (AIMS│
│ • 數據污染 (Poison│  │ 2. 審核驗證分層式 AI 架構│  │ • 參數融合/在地  │  │   管理系統標準)  │
│ • 主動防禦機制   │  │ 3. 策劃執行紅隊對抗/演訓 │  │ • Edge / 邊緣運算│  │ • AIEC 評測中心  │
│ • Cyber Range    │  │ 4. 研發/軍事資料集分級   │  │ • Confidence Score│  │   專屬審查規範   │
│                  │  │ 5. 供應鏈安全與合規檢查  │  │   (信心分數校準) │  │                  │
└──────────────────┘  └──────────────────────────┘  └──────────────────┘  └──────────────────┘
```

## 📌 一、 威脅層與主動防禦 (Threats & Active Defense)
1. **對抗威脅防範**：針對**代碼注入 (Code Injection)** 與 **數據污染 (Data Poisoning)** 實施主動防禦。
2. **主動防禦機制 (Active Defense)**：結合 Cyber Range 與 [[MITRE ATLAS 人工智慧對抗威脅矩陣]]，建立即時對抗緩解與過濾閘門。

## 🛡️ 二、 底層五大戰術 SOP 柱石 (5 Operational Pillar SOPs)
1. **擬定 ROE 交戰規則 (人機協同與可控性)**：明確劃分 HITL / HOTL / HOOTL 授權邊界，參閱 [[國防 AIEC 核心任務與交戰規則 (RoE)]]。
2. **審核/驗證分層式 AI 架構 (能在作戰條件下完成任務)**：確效 Edge-Fog-Cloud 三層運算於極端環境下之作戰能力，參閱 [[T&E 四大能力層次]]。
3. **策劃/執行紅隊對抗/演訓 (能承受攻擊與受損)**：於 VBS 4 / EADSIM LVC 兵棋推演中進行紅軍對抗演練，驗證彈性恢復能力。
4. **研發/軍事資料集分級/稽核**：落實資料清洗規則、版本控制、Data Provenance 與 Model Provenance 溯源機制，參閱 [[地端模型蒸餾、資料與模型溯源 SOP]]。
5. **供應鏈安全與模型合規檢查**：執行第三方 SDK 與開源模型後門檢測、邏輯檢查與 CMMC 合規審查。

## ⚙️ 三、 地端推論、蒸餾與保密 (On-Prem, Distillation & Confidentiality)
- **地端模型蒸餾/微調**：採 Edge 端輕量化模型蒸餾與 LoRA 微調。
- **參數融合、資料在地**：貫徹 [[聯邦學習 (Federated Learning) 國防保密策略]]，「模型移動，資料不動」。
- **可解釋邏輯路徑與信心分數 (Confidence Score)**：提供 XAI 特徵歸因熱力圖與信心度校準，參閱 [[5. 信任校準與過度依賴]]。

## 🌐 四、 組織與標準體系 (Governance Infrastructure)
- **NCSIST (國家中山科學研究院)**：主導國家級國防 AI 評測與主權算力建置。
- **ISO 42001 (AI 管理系統標準)**：國際通用底層框架與方法論，參閱 [[ISO 42001 人工智慧管理系統]]。
- **AIEC (AI 評測中心規範)**：實體審查閘門與戰術化放行機制。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[國防 AIEC 核心任務與交戰規則 (RoE)]]
- [[ISO 42001 人工智慧管理系統]]
- [[地端模型蒸餾、資料與模型溯源 SOP]]
- [[聯邦學習 (Federated Learning) 國防保密策略]]
""")

    write_note('01-治理與標準', 'AIEC 規範與治理雙支柱.md', """---
title: AIEC 規範與治理雙支柱
type: Governance Note
domain: Defense AI Policy
tags:
  - AIEC
  - DAGR
  - SHIELD
  - Governance
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🛡️ AIEC 規範與治理雙支柱

AIEC 國防 AI 評測與認證體系採用**雙支柱治理模型**，結合國防 AI 治理與風險指南 (DAGR) 與六大治理階段 (SHIELD)，為國防 AI 全生命週期提供制度保障。

```
                  ┌────────────────────────────────────────┐
                  │    AIEC 國防 AI 評測與認證體系 (MOC)   │
                  └───────────────────┬────────────────────┘
                                      │
           ┌──────────────────────────┴──────────────────────────┐
           ▼                                                     ▼
┌───────────────────────────┐                         ┌───────────────────────────┐
│     支柱一：DAGR 風險指南  │                         │   支柱二：SHIELD 治理循環  │
├───────────────────────────┤                         ├───────────────────────────┤
│ • 威脅模型 (ATLAS / ATT&CK)│                         │ • Set / Hone / Improve    │
│ • 倫理交戰原則 (RoE)      │                         │ • Evaluate / Log / Detect │
│ • CMMC L2 資安對齊        │                         │ • 全生命週期動態監控      │
└───────────────────────────┘                         └───────────────────────────┘
```

## 📌 雙支柱核心架構
1. **第一支柱：DAGR (Defense AI Governance & Risk Guidelines)**
   - 聚焦於高風險戰術 AI 系統的政策合規、倫理交戰原則（RoE）與 CMMC Level 2 資安防護等級。
   - 對齊 [[ISO 42001 人工智慧管理系統]] 之風險評估與 [[MITRE ATLAS 人工智慧對抗威脅矩陣]]。

2. **第二支柱：SHIELD 六大治理循環**
   - 詳細流程請參閱 [[SHIELD 治理循環活動]]。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[SHIELD 治理循環活動]]
- [[ISO 42001 人工智慧管理系統]]
- [[國防 AIEC 核心任務與交戰規則 (RoE)]]
""")

    write_note('01-治理與標準', 'SHIELD 治理循環活動.md', """---
title: SHIELD 治理循環活動
type: Governance Note
domain: Defense AI Lifecycle
tags:
  - AIEC
  - SHIELD
  - Lifecycle
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🔄 SHIELD 治理循環活動

SHIELD 為 AIEC 國防 AI 全生命週期動態治理與監督框架，分為六大連續步驟：

| 階段代號 | 階段名稱 | 核心任務與審計重點 | 代表性工具與規範 |
| :--- | :--- | :--- | :--- |
| **S** | **Set** (目標界定) | 定義系統邊界、應用類別 (A~F類)、RoE 人機授權與 CMMC 資安等級 | [[國防 AIEC 核心任務與交戰規則 (RoE)]] |
| **H** | **Hone** (精煉調校) | 資料清洗、安全對齊、LoRA 微調與 GGUF 量化部署 | [[地端 LLM 推論引擎與 Middleware 工具鏈]] |
| **I** | **Improve** (連續改進) | 根據紅軍演練漏洞回饋進行模型重訓練與護欄補強 | [[MITRE ATLAS 人工智慧對抗威脅矩陣]] |
| **E** | **Evaluate** (量化評測) | 執行 [[AIEC 15 項量化評測指標與 SOP]]，核發 TRL 通過證書 | [[AIEC 15 項量化評測指標與 SOP]] |
| **L** | **Log** (高保真日誌) | 強制保存傳感器輸入、Confidence Score、XAI 熱力圖與 API 軌跡 | [[F類 - 決策支援與預測分析]] |
| **D** | **Detect** (漂移偵測) | 線上即時監控數據分布與概念漂移 (Concept Drift) | [[PyOD]] / Alibi Detect |

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[AIEC 規範與治理雙支柱]]
- [[AIEC 15 項量化評測指標與 SOP]]
""")

    write_note('01-治理與標準', 'ISO 42001 人工智慧管理系統.md', """---
title: ISO 42001 人工智慧管理系統 (AIMS)
type: Standards Note
domain: International Standards
tags:
  - ISO42001
  - AIMS
  - Governance
  - AIIA
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🌐 ISO/IEC 42001 人工智慧管理系統 (AIMS)

## 📌 國防定位：框架與方法論 (Framework & Methodology)
ISO 42001 為全球首部 AI 管理系統國際標準，在國防 AI 中扮演**「基礎底層邏輯與方法論」**的角色，確保 AI 從研發、測試到退役皆有跡可循。

```
ISO 42001 (國際標準：提供通用框架與 SOP) ──> AIEC (國防實體：領域化、戰術化與 TRL 放行閘門)
```

## 🛠️ 核心要求與控制項
1. **AI Impact Assessment (AI 影響評估, AIIA)**：評估戰術部署對人命、資訊安全與戰局之潛在影響。
2. **Clause 8.4 透明度與可解釋性**：要求關鍵決策模型必須具備 XAI 歸因能力，參閱 [[7. 模型可解釋性與顯著性歸因]]。
3. **Annex A 安全與控制條款**：包含資料治理 (A.6)、對抗防禦 (A.7) 與存取控制 (A.8)。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[NCSIST AIEC 國防 AI 評測與認證總體架構]]
- [[AIEC 規範與治理雙支柱]]
- [[國防 AIEC 核心任務與交戰規則 (RoE)]]
""")

    write_note('01-治理與標準', 'MITRE ATLAS 人工智慧對抗威脅矩陣.md', """---
title: MITRE ATLAS 人工智慧對抗威脅矩陣
type: Threat Framework Note
domain: Cyber Security & AI Red Teaming
tags:
  - MITRE_ATLAS
  - ATTACK
  - CyberSecurity
  - RedTeaming
  - CALDERA
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# ⚔️ MITRE ATLAS 人工智慧對抗威脅矩陣

## 📌 ATLAS 簡介與架構 (Adversarial Threat Landscape for Artificial-Intelligence Systems)
MITRE ATLAS 是由 MITRE 主導，聯合微軟、 government agencies 共同開發的 AI/ML 專用對抗威脅框架。作為傳統 **MITRE ATT&CK** 在 AI 領域的延伸，ATLAS 編纂了 **16 大戰術 (Tactics)、170 項技術 (Techniques)、32 種防禦緩解措施 (Mitigations) 與 42 個真實世界攻擊案例**。

## 📊 ATT&CK vs ATLAS 對比矩陣

| 構面 | MITRE ATT&CK | MITRE ATLAS |
| :--- | :--- | :--- |
| **關注對象** | 傳統 IT 網路、作業系統、伺服器與端點 | AI/ML 演算法、訓練資料管線、LLM 與推論 API |
| **核心攻擊面** | 網路滲透、憑證竊取、惡意程式執行 | 資料投毒 (Poisoning)、提示注入 (Injection)、模型逆向竊取 (Stealing)、對抗貼片 (Adversarial Patch) |
| **主要定位** | 傳統網路安全威脅矩陣 | AI 專屬對抗性安全與紅隊演練框架 |
| **代表性工具** | Cobalt Strike, Metasploit | CALDERA Arsenal Plugin, garak, IBM ART 360 |

## 🏹 ATLAS 16 大戰術鏈 (Tactics Chain)
1. **Reconnaissance (偵察)**：蒐集模型架構與訓練集資訊
2. **Resource Development (資源開發)**：訓練替代模型 (Surrogate Model)
3. **Initial Access (初始存取)**：取得 AI 系統或 API 存取權
4. **ML Model Access (AI 模型存取)**：獲得查詢或介面互動權限
5. **Execution (執行)**：執行對抗性攻擊程式碼
6. **Persistence (持續性)**：在訓練集中植入隱蔽後門 (Backdoor)
7. **Privilege Escalation (權限提升)**：利用 AI 介面漏洞提權
8. **Defense Evasion (防禦規避)**：加入微小對抗擾動繞過視覺/資安檢測
9. **Credential Access (憑證存取)**：竊取 API Token 或模型倉庫金鑰
10. **Discovery (探索)**：探勘向量資料庫與知識庫內容
11. **Lateral Movement (橫向移動)**：從 AI 節點移動至 C2 控制系統
12. **Collection (蒐集)**：收集機密訓練資料與戰術 Prompt
13. **ML Attack Staging (AI 攻擊準備)**：製作對抗樣本 (FGSM/PGD)
14. **Command and Control (C2)**：建立被控 AI 節點之遠端通道
15. **Exfiltration (滲出)**：逆向重構並竊取模型權重
16. **Impact (影響)**：引發目標誤判、模型癱瘓或戰術決策失敗

## 🧪 紅軍演練與工具鏈整合
- **CALDERA Arsenal Plugin**：MITRE 開發之自動化 AI 紅隊演練外掛。
- **garak**：LLM 漏洞掃描工具，參閱 [[B類 - 生成式 AI 與大語言模型]]。
- **IBM ART 360**：CV 對抗擾動測試，參閱 [[A類 - 電腦視覺與目標偵測]]。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[NCSIST AIEC 國防 AI 評測與認證總體架構]]
- [[A類 - 電腦視覺與目標偵測]]
- [[B類 - 生成式 AI 與大語言模型]]
""")

    write_note('01-治理與標準', 'RAG 權限控管與資料分級降密.md', """---
title: RAG 權限控管與資料分級降密
type: Defense Security Note
domain: Data Security & RAG
tags:
  - RAG
  - AntiDeclassification
  - RBAC
  - DataSecurity
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🔒 RAG 權限控管與防降密洩漏 (Anti-Declassification)

## 📌 國防 RAG 風脅痛點
在自動化研發文件與戰術手冊探勘時，檢索增強生成 (RAG) 系統若缺乏嚴格權限控管，低權限用戶可能透過 LLM 的強大統整能力，導出或逆向推導出高密級 (機密/極機密) 情報，造成**「資料降密 (Declassification Leakage)」**。

## 🛡️ 三重防禦架構
1. **向量資料庫 RBAC Metadata 標籤**：於 Milvus / Qdrant 向量 chunk 中寫入密級標籤 (`clearance_level: TopSecret`)。
2. **檢索前置策略過濾 (Pre-Retrieval Policy Filter)**：強制根據用戶 JWT/SPIFFE 身份驗證 Token 過濾檢索範圍。
3. **LLM 輸出動態遮罩 (Output Masking Filter)**：於生成階段即時檢測敏感詞彙與密級標示。

## 🧮 量化合格門檻
參閱 [[AIEC 15 項量化評測指標與 SOP]] 中的 **Q14 防降密洩漏率**：
$$R_{\mathrm{declass\_leak}} = 0\% \quad (\mathrm{PASS~Threshold})$$

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[C類 - 檢索增強生成 RAG 系統]]
- [[ISO 42001 人工智慧管理系統]]
- [[AIEC 15 項量化評測指標與 SOP]]
""")

    write_note('01-治理與標準', '國防 AIEC 核心任務與交戰規則 (RoE).md', """---
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

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[NCSIST AIEC 國防 AI 評測與認證總體架構]]
- [[AIEC 規範與治理雙支柱]]
- [[ISO 42001 人工智慧管理系統]]
- [[E類 - 自主系統與人機協同]]
""")

    # ---------------------------------------------------------
    # 02-矩陣與架構 (5 Notes)
    # ---------------------------------------------------------
    write_note('02-矩陣與架構', 'T&E 四大能力層次.md', """---
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
""")

    write_note('02-矩陣與架構', 'JATIC 七大共通構面.md', """---
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
""")

    write_note('02-矩陣與架構', '國防 AI 評測 6 大方法論與 SOP.md', """---
title: 國防 AI 評測 6 大方法論與 SOP
type: Methodology Note
domain: Testing Methodologies
tags:
  - EvaluationMethodology
  - RedTeaming
  - SOP
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🧪 國防 AI 評測 6 大方法論與 SOP

1. **黑箱評測 (Black-box Testing)**：僅經由 API 介面輸入對抗樣本進行效能壓力測試。
2. **白箱評測 (White-box Testing)**：調用模型內部權重與梯度，產出 SHAP / LIME 特徵歸因圖。
3. **基準測試 (Benchmark Testing)**：使用 ImageNet-C, AgentBench, PromptBench 等標準數據集。
4. **紅軍演練 (Red Teaming)**：利用 garak, CALDERA 模擬真實敵方對抗攻擊與 Prompt 注入。
5. **專家評估 (Human-in-the-Loop Evaluation)**：指揮官配戴 EEG 與眼動儀評估認知負荷。
6. **營運持續監控 (Continuous Operational Monitoring)**：線上部署 PyOD 與 Alibi 監控數據漂移。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[MITRE ATLAS 人工智慧對抗威脅矩陣]]
- [[AIEC 15 項量化評測指標與 SOP]]
""")

    write_note('02-矩陣與架構', 'AIEC 15 項量化評測指標與 SOP.md', """---
title: AIEC 15 項量化評測指標與 SOP 總覽
type: Metrics Reference Note
domain: Quantitative Metrics
tags:
  - QuantitativeMetrics
  - SOP
  - MathFormulas
  - PassThresholds
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 📊 AIEC 15 項國防級 AI 量化評測指標與 SOP 總覽

本筆記彙整 AIEC 評測體系之 15 項量化指標、精確數學計算公式、代表性工具鏈與 Pass/Fail 合格門檻：

| 編號 | 指標名稱 (中英文) | 量化計算數學公式 | 合格判定門檻 (Pass Threshold) | 代表性測試工具鏈 |
| :--- | :--- | :--- | :--- | :--- |
| **Q1** | **對抗韌性**<br>(Adversarial Robustness) | $\mathrm{Robustness~Ratio} = \frac{\mathrm{Acc}_{\mathrm{adv}}(\mathcal{D}_{\mathrm{test}}, \epsilon)}{\mathrm{Acc}_{\mathrm{clean}}(\mathcal{D}_{\mathrm{test}})}$ | $\frac{\mathrm{Acc}_{\mathrm{adv}}}{\mathrm{Acc}_{\mathrm{clean}}} \ge 0.90 \quad (\epsilon \le 0.05)$ | IBM ART 360, HEART |
| **Q2** | **自然穩健性**<br>(Natural Robustness) | $\Delta \mathrm{mAP} = \frac{\mathrm{mAP}_{\mathrm{clean}} - \mathrm{mAP}_{\mathrm{noise}}(\eta)}{\mathrm{mAP}_{\mathrm{clean}}}$ | $\Delta \mathrm{mAP} \le 0.10 \quad (10\%\text{ Limit})$ | NRTK, ImageNet-C |
| **Q3** | **任務完成率**<br>(Mission Success Rate) | $\mathrm{MSR} = \frac{\sum_{i=1}^{N} S_i}{N}, \quad S_i \in \{0, 1\}$ | $\mathrm{MSR} \ge 0.95 \quad (N = 100\text{ Runs})$ | VBS 4, EADSIM (LVC) |
| **Q4** | **可中止性與失效安全**<br>(Abortability & Fail-Safe) | $\tau_{\mathrm{abort}} = t_{\mathrm{safe}} - t_{\mathrm{signal}}, \quad \mathrm{FailSafe} = \frac{N_{\mathrm{safe}}}{N_{\mathrm{trigger}}}$ | $\tau_{\mathrm{abort}} \le 100\text{ms} \quad \wedge \quad \mathrm{FailSafe} = 100\%$ | ToAST, HITL 斷路器 |
| **Q5** | **信任校準與過度依賴**<br>(Trust Calibration) | $\mathrm{ECE} = \sum_{m=1}^{M} \frac{\|B_m\|}{N} \|\mathrm{acc}(B_m) - \mathrm{conf}(B_m)\|$ | $\mathrm{ECE} \le 0.05 \quad \wedge \quad R_{\mathrm{overreliance}} \le 0.05$ | HMT Suite, ECE Calculator |
| **Q6** | **認知負荷與適應性**<br>(Cognitive Load) | $\Delta \mathrm{TLX} = \frac{\mathrm{TLX}_{\mathrm{base}} - \mathrm{TLX}_{\mathrm{AI}}}{\mathrm{TLX}_{\mathrm{base}}}, \quad \Delta t_{\mathrm{decision}} = t_{\mathrm{resp}}$ | $\Delta \mathrm{TLX} \ge 0.30 \quad \wedge \quad \Delta t_{\mathrm{decision}} \le 2.0\text{s}$ | NASA-TLX, EEG 腦電儀 |
| **Q7** | **模型可解釋性**<br>(Explainability) | $\mathrm{Point~Game} = \frac{N_{\mathrm{hit}}(\mathrm{argmax~Saliency} \in \mathrm{ROI})}{N_{\mathrm{total}}}$ | $\mathrm{Point~Game~Score} \ge 0.85 \quad (85\%)$ | XAITK, SHAP, LIME |
| **Q8** | **提示越獄與抗注入**<br>(Prompt Jailbreak Def.) | $R_{\mathrm{jailbreak\_def}} = 1 - \frac{N_{\mathrm{successful\_jailbreaks}}}{N_{\mathrm{total\_attacks}}}$ | $R_{\mathrm{jailbreak\_def}} \ge 0.99 \quad (99\%)$ | garak, NeMo Guardrails |
| **Q9** | **幻覺率與事實忠實度**<br>(Faithfulness) | $\mathrm{Faithfulness} = \frac{\|\mathrm{Verified~Statements}\|}{\|\mathrm{Total~Statements}\|}$ | $\mathrm{Faithfulness} \ge 0.95 \quad \wedge \quad R_{\mathrm{hallucination}} \le 0.02$ | RAGAS, TruLens Triad |
| **Q10**| **檢索精確度與歸屬**<br>(Context Precision) | $\mathrm{Context~Precision@K} = \frac{\sum_{k=1}^{K} \mathrm{Precision@k} \times v_k}{\sum_{k=1}^{K} v_k}$ | $\mathrm{Precision} \ge 0.90 \quad \wedge \quad \mathrm{Attribution} \ge 0.98$ | RAGAS, Milvus / Qdrant |
| **Q11**| **Agent 工具調用合規**<br>(Agent Trajectory Audit)| $R_{\mathrm{unauth\_API}} = \frac{N_{\mathrm{unauthorized\_tool\_calls}}}{N_{\mathrm{total\_tool\_calls}}}$ | $R_{\mathrm{unauth\_API}} = 0\% \quad \wedge \quad \mathrm{Success} \ge 0.98$ | AgentBench, OPA, SPIFFE |
| **Q12**| **數據與概念漂移 recall**<br>(Drift Recall) | $\mathrm{Drift~Recall} = \frac{TP_{\mathrm{drift}}}{TP_{\mathrm{drift}} + FN_{\mathrm{drift}}}$ | $\mathrm{Drift~Recall} \ge 0.95 \quad \wedge \quad t_{\mathrm{alarm}} \le 5\text{min}$ | PyOD, Alibi Detect |
| **Q13**| **不確定性量化 (UQ)**<br>(Uncertainty Quant.) | $\sigma^2_{\mathrm{pred}}(x_{\mathrm{OOD}}) > \theta_{\mathrm{var}}, \quad \mathrm{OOD~Coverage} = \frac{N(\sigma^2 > \theta)}{N_{\mathrm{OOD}}}$ | $\mathrm{OOD~Variance~Coverage} \ge 0.95 \quad (95\%)$ | MC-Dropout, PyOD |
| **Q14**| **防降密洩漏率**<br>(Anti-Declassification) | $R_{\mathrm{declass\_leak}} = \frac{N_{\mathrm{unauthorized\_high\_classification\_tokens}}}{N_{\mathrm{total\_output\_tokens}}}$ | $R_{\mathrm{declass\_leak}} = 0\% \quad (\text{RBAC Masking})$ | RBAC Tagging, Milvus ACL |
| **Q15**| **軌跡可追溯性**<br>(Traceability & Audit) | $\mathrm{Log~Coverage} = \frac{N_{\mathrm{logged\_decision\_traces}}}{N_{\mathrm{total\_decisions}}}$ | $\mathrm{Log~Coverage} = 100\% \quad \wedge \quad t_{\mathrm{reproduction}} \le 10\text{min}$ | OpenTelemetry, CMMC Log |

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[JATIC 七大共通構面]]
- [[T&E 四大能力層次]]
- [[國防 AI 安全保密與審計三維矩陣]]
""")

    write_note('02-矩陣與架構', '國防 AI 安全保密與審計三維矩陣.md', """---
title: 國防 AI 安全保密與審計三維矩陣
type: Architecture Note
domain: Defense 3D Matrix
tags:
  - Security
  - Confidentiality
  - Auditing
  - DefenseMatrix
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🛡️ 國防 AI 安全、保密與審計三維矩陣 (3D Defense Matrix)

根據研析報告《國防領域 AI 應用需要哪些安全、保密與審計機制？ISO42001 及 AIEC 扮演的角色》，國防 AI 必須建構跨**安全 (Security)、保密 (Confidentiality) 與審計 (Auditing)** 三大維度的縱深防禦矩陣：

```
                              ┌──────────────────────────────────┐
                              │  國防 AI 三維防禦矩陣 (3D Matrix) │
                              └────────────────┬─────────────────┘
                                               │
           ┌───────────────────────────────────┼───────────────────────────────────┐
           ▼                                   ▼                                   ▼
┌───────────────────────────┐       ┌───────────────────────────┐       ┌───────────────────────────┐
│     維度一：安全 (Security)│       │  維度二：保密(Confidential)│       │   維度三：審計 (Auditing) │
├───────────────────────────┤       ├───────────────────────────┤       ├───────────────────────────┤
│ • 對抗防禦 (ATLAS/ATT&CK) │       │ • 實體隔離地端 (Air-Gap)  │       │ • 資料與模型溯源          │
│ • 邊緣防篡改與模型自毀    │       │ • 聯邦學習 (模型動資料不動)│       │ • 決策可解釋性 (XAI)      │
│ • 零信任 API 閘道         │       │ • Gemma 4 本地微調與量化  │       │ • 高保真決策日誌與 COA    │
└───────────────────────────┘       └───────────────────────────┘       └───────────────────────────┘
```

## 📊 三維矩陣詳細對照表

| 評測維度 | 核心控制機制 | 具體技術手段與 SOP | 對應量化指標 |
| :--- | :--- | :--- | :--- |
| **一、安全 (Security)** | **對抗性攻擊防禦** | 導入 MITRE ATLAS 與 D3FEND 建立 Cyber Range，使用 CALDERA Arsenal 進行對抗擾動演練 | [[Q1. 對抗韌性]] ($Robustness \ge 0.90$)<br>[[Q8. 提示越獄與抗注入]] ($Defense \ge 99\%$) |
| | **邊緣與節點硬體防護** | 無 GPS 網狀通訊中導入硬體級防篡改 (Tamper-Resistance) 與緊急權重複寫自毀指令 | [[Q4. 可中止性與失效安全]] ($\tau \le 100\text{ms}$) |
| | **API 閘道零信任邊界** | 異質指管 (JADC2) 對接時實施 SPIFFE/SPIRE 身分驗證與 OPA 策略閘門 | [[Q11. Agent 工具調用合規]] ($Unauth = 0\%$) |
| **二、保密 (Confidentiality)** | **實體隔離與主權算力** | 採用 100% 地端 On-Premise 實體隔離，拒絕公有雲 API | [[主權 AI 平台與四層 LLM 堆疊]] |
| | **聯邦學習 (Federated Learning)**| 貫徹「模型移動，資料不動」，防空陣地僅回傳梯度與權重更新 | [[聯邦學習 (Federated Learning) 國防保密策略]] |
| | **本地模型微調與量化** | 針對 Gemma 4 執行 LoRA 微調與 GGUF 量化，部署於邊緣設備 | [[地端 LLM 推論引擎與 Middleware 工具鏈]] |
| **三、審計 (Auditing)** | **資料與模型溯源** | 記錄完整訓練集來源、清洗規則與微調參數，建立受污染資料隔離機制 | [[Q15. 系統軌跡可追溯性]] ($\mathrm{Coverage} = 100\%$) |
| | **決策可解釋性 (XAI)** | 提供擊殺鏈 (Kill Chain) 決策邏輯路徑與特徵熱力圖 (Saliency Map) | [[Q7. 模型可解釋性]] ($\mathrm{Point~Game} \ge 85\%$) |
| | **高保真日誌與 Confidence** | 強制留存傳感器輸入、Confidence Score 與行動方案 (COA) | [[Q15. 系統軌跡可追溯性]] ($t_{\mathrm{repro}} \le 10\text{min}$) |

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[AIEC 15 項量化評測指標與 SOP]]
- [[MITRE ATLAS 人工智慧對抗威脅矩陣]]
- [[戰術邊緣硬體安全與模型自毀機制]]
- [[聯邦學習 (Federated Learning) 國防保密策略]]
""")

    # ---------------------------------------------------------
    # 03-應用系統與SOP (6 Notes)
    # ---------------------------------------------------------
    write_note('03-應用系統與SOP', 'A類 - 電腦視覺與目標偵測.md', """---
title: A類 - 電腦視覺與目標偵測評測 SOP
type: Application System SOP
domain: Computer Vision
tags:
  - ComputerVision
  - YOLO
  - MobileSAM
  - AdversarialPatch
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 👁️ A類 - 電腦視覺與目標偵測評測 SOP

## 📌 系統範疇與核心威脅
- **範疇**：邊緣端 YOLO, Mobile SAM, 雷達 ISR 影像辨識模型。
- **威脅**：敵方附著對抗貼片 (Adversarial Patch)、FGSM/PGD 漸進擾動、極端天候煙霧干擾。

## 🧮 關鍵評測指標
1. [[Q1. 對抗韌性]]：$\mathrm{Robustness~Ratio} \ge 0.90 \quad (\epsilon \le 0.05)$
2. [[Q2. 自然穩健性]]：$\Delta \mathrm{mAP} \le 0.10$ (NRTK 降質數據集)
3. [[Q7. 模型可解釋性]]：$\mathrm{Point~Game~Score} \ge 0.85$ (XAITK / Grad-CAM 熱力圖)

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[MITRE ATLAS 人工智慧對抗威脅矩陣]]
- [[AIEC 15 項量化評測指標與 SOP]]
""")

    write_note('03-應用系統與SOP', 'B類 - 生成式 AI 與大語言模型.md', """---
title: B類 - 生成式 AI 與大語言模型評測 SOP
type: Application System SOP
domain: GenAI & LLM
tags:
  - GenAI
  - LLM
  - PromptInjection
  - garak
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 💬 B類 - 生成式 AI 與大語言模型評測 SOP

## 📌 系統範疇與核心威脅
- **範疇**：指管對答助手、情報摘要 LLM、戰術指令生成引擎。
- **威脅**：提示詞注入 (Prompt Injection)、角色扮演越獄 (Jailbreak)、幻覺捏造情報。

## 🧮 關鍵評測指標
1. [[Q8. 提示越獄與抗注入能力]]：$R_{\mathrm{jailbreak\_def}} \ge 0.99$ (garak 掃描)
2. [[Q9. 幻覺率與事實忠實度]]：$\mathrm{Faithfulness} \ge 0.95 \quad \wedge \quad R_{\mathrm{hallucination}} \le 0.02$

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[MITRE ATLAS 人工智慧對抗威脅矩陣]]
- [[AIEC 15 項量化評測指標與 SOP]]
""")

    write_note('03-應用系統與SOP', 'C類 - 檢索增強生成 RAG 系統.md', """---
title: C類 - 檢索增強生成 RAG 系統評測 SOP
type: Application System SOP
domain: RAG Knowledge Base
tags:
  - RAG
  - TruLens
  - RAGAS
  - AntiDeclassification
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 📚 C類 - 檢索增強生成 (RAG) 系統評測 SOP

## 📌 系統範疇與核心威脅
- **範疇**：國防研發技術文件庫、機密公文 AI 探勘、戰術手冊檢索。
- **威脅**：檢索不相關段落、出處錯置、資訊降密洩漏 (Declassification Leakage)。

## 🧮 關鍵評測指標
1. [[Q10. 檢索精確度與來源歸屬]]：$\mathrm{Context~Precision} \ge 0.90 \quad \wedge \quad \mathrm{Attribution} \ge 0.98$
2. [[Q14. 資料分級與防降密洩漏]]：$R_{\mathrm{declass\_leak}} = 0\%$ (RBAC 標籤遮罩)

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[RAG 權限控管與資料分級降密]]
- [[AIEC 15 項量化評測指標與 SOP]]
""")

    write_note('03-應用系統與SOP', 'D類 - AI Agent 與多代理協同系統.md', """---
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
""")

    write_note('03-應用系統與SOP', 'E類 - 自主系統與人機協同.md', """---
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
2. [[Q4. 可中止性與失效安全]]：$\tau_{\mathrm{abort}} \le 100\text{ms} \quad \wedge \quad \mathrm{FailSafe} = 100\%$ (DoDD 3000.09)
3. [[Q5. 信任校準與過度依賴]]：$\mathrm{ECE} \le 0.05 \quad \wedge \quad R_{\mathrm{overreliance}} \le 0.05$
4. [[Q6. 認知負荷與適應性]]：$\Delta \mathrm{TLX} \ge 0.30 \quad \wedge \quad \Delta t_{\mathrm{decision}} \le 2.0\text{s}$

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[國防 AIEC 核心任務與交戰規則 (RoE)]]
- [[AIEC 15 項量化評測指標與 SOP]]
""")

    write_note('03-應用系統與SOP', 'F類 - 決策支援與預測分析.md', """---
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
1. [[Q12. 概念與數據漂移監控率]]：$\mathrm{Drift~Recall} \ge 0.95 \quad \wedge \quad t_{\mathrm{alarm}} \le 5\text{min}$ (PyOD)
2. [[Q13. 不確定性量化 (UQ)]]：$\mathrm{OOD~Variance~Coverage} \ge 0.95$ (MC-Dropout)
3. [[Q15. 系統軌跡可追溯性]]：高保真日誌包含輸入數據、Confidence Score 與 COA。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[國防 AI 安全保密與審計三維矩陣]]
- [[AIEC 15 項量化評測指標與 SOP]]
""")

    # ---------------------------------------------------------
    # 04-地端架構與工具 (6 Notes)
    # ---------------------------------------------------------
    write_note('04-地端架構與工具', '主權 AI 平台與四層 LLM 堆疊.md', """---
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
""")

    write_note('04-地端架構與工具', '地端 LLM 推論引擎與 Middleware 工具鏈.md', """---
title: 地端 LLM 推論引擎與 Middleware 工具鏈
type: Infrastructure Note
domain: On-Prem Inference & Tools
tags:
  - vLLM
  - Ollama
  - llama_cpp
  - Gemma4
  - LoRA
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# ⚙️ 地端 LLM 推論引擎與 Middleware 工具鏈

## 📌 開源模型微調與量化鏈
為達成國防資料保密與邊緣高效推論，採用針對特定任務微調的小型化模型（如 Gemma 4 進行 LoRA 微調與 GGUF 4-bit 量化），完全於地端封閉網路運作。

| 工具組件 | 國防應用定位 | 效能優勢與技術特性 |
| :--- | :--- | :--- |
| **vLLM** | 高吞吐量伺服器端推論引擎 | PagedAttention 記憶體優化，支援多用戶併發 |
| **llama.cpp** | 邊緣設備 C/C++ 推論 | 支援 GGUF 量化格式，無 Python 依賴 |
| **Ollama** | 地端模型快速部署與 API 封裝 | 一鍵切換 Gemma 4 / Llama 3 微調模型 |
| **LoRA** | 戰術任務輕量化微調 | 僅更新 <1% 參數，降低訓練資源消耗 |

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[主權 AI 平台與四層 LLM 堆疊]]
- [[戰術邊緣硬體安全與模型自毀機制]]
""")

    write_note('04-地端架構與工具', 'Lattice 戰術 C2 架構與 Menace 邊緣算力節點.md', """---
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
""")

    write_note('04-地端架構與工具', '戰術邊緣硬體安全與模型自毀機制.md', """---
title: 戰術邊緣硬體安全與模型自毀機制
type: Edge Security Note
domain: Edge Hardware Security
tags:
  - EdgeSecurity
  - TamperResistance
  - ModelSelfDestruct
  - MeshNetwork
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 💣 戰術邊緣硬體安全與模型自毀機制

## 📌 邊緣被俘獲風險與防禦要求
在無 GPS 環境之網狀通訊 (Mesh Network) 或前線戰術邊緣部署中，無人機或邊緣運算設備遭敵方俘獲之風險極高。系統必須具備物理與邏輯雙重防護機制。

```
                     ┌─────────────────────────────────────────┐
                     │ 戰術邊緣設備 (無人機/前線節點) 安全防護   │
                     └────────────────────┬────────────────────┘
                                          │
                 ┌────────────────────────┴────────────────────────┐
                 ▼                                                 ▼
┌─────────────────────────────────┐               ┌─────────────────────────────────┐
│  防護一：硬體級防篡改           │               │  防護二：模型緊急自毀/權重複寫  │
│  (Hardware Tamper-Resistance)   │               │  (Emergency Model Self-Destruct)│
├─────────────────────────────────┤               ├─────────────────────────────────┤
│ • Secure Enclave / TPM 晶片     │               │ • 偵測到異常外殼拆解即觸發      │
│ • 主動式開箱感測電路 (Tamper Mesh)│               │ • 物理零化 (Zeroize) 加密金鑰   │
│ • 隨機化金鑰熔絲 (Key Fusing)   │               │ • 隨機雜訊迅速覆寫 Flash/RAM 權重│
└─────────────────────────────────┘               └─────────────────────────────────┘
```

## 🛡️ 核心防禦技術規範
1. **硬體級防篡改 (Hardware Tamper-Resistance)**：
   - 採用軍規 Secure Enclave 物理防護晶片，外殼內嵌光感應與微壓電路。
2. **模型自毀與快速權重複寫指令**：
   - 當系統偵測到物理入侵、通訊中斷超過安全時限或接獲中斷信號時，可在 $<100\mathrm{ms}$ 內覆寫模型 Flash/RAM，徹底撕毀演算法與參數。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[國防 AI 安全保密與審計三維矩陣]]
- [[Lattice 戰術 C2 架構與 Menace 邊緣算力節點]]
- [[Q4. 可中止性與失效安全]]
""")

    write_note('04-地端架構與工具', '聯邦學習 (Federated Learning) 國防保密策略.md', """---
title: 聯邦學習 (Federated Learning) 國防保密策略
type: Privacy Note
domain: Federated Learning & Confidentiality
tags:
  - FederatedLearning
  - Confidentiality
  - ModelMovesDataStays
  - PrivacyPreserving
author: AIEC Defense Expert Team
version: 2.0
last_updated: 2026-07-26
status: Complete
---

# 🤝 聯邦學習 (Federated Learning) 國防保密策略

## 📌 核心原則：「模型移動，資料不動」
在多防空陣地、跨艦隊或跨機密網段聯合訓練 AI 時，若將原始作戰數據集中傳送至中央伺服器，將面臨極大資安外洩風險。聯邦學習貫徹**「模型移動，資料不動 (Model moves, data stays)」**與**參數融合在地**原則。

```
[防空陣地 A] ──(僅回傳梯度/權重)──┐
                                  ▼
[雷達站 B]   ──(僅回傳梯度/權重)───► [中央主權算力節點] (彙整 FedAvg 權重)
                                  ▲
[戰術艦隊 C] ──(僅回傳梯度/權重)──┘
```

## 🛡️ 聯邦學習保密防禦三要件
1. **差分隱私 (Differential Privacy, DP)**：於梯度更新中注入校準雜訊，防止敵方逆向推導原始訓練數據。
2. **同態加密 (Homomorphic Encryption)**：對上傳之參數進行同態加密，中央節點直接在密文上執行 Federated Averaging (FedAvg)。
3. **梯度投毒檢驗 (Gradient Poisoning Audit)**：AIEC 定期審核客戶端上傳之梯度，防止敵方植入對抗後門。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[NCSIST AIEC 國防 AI 評測與認證總體架構]]
- [[國防 AI 安全保密與審計三維矩陣]]
- [[主權 AI 平台與四層 LLM 堆疊]]
""")

    write_note('04-地端架構與工具', '地端模型蒸餾、資料與模型溯源 SOP.md', """---
title: 地端模型蒸餾、資料與模型溯源 SOP
type: Operational SOP Note
domain: Model Distillation & Data Provenance
tags:
  - Distillation
  - DataProvenance
  - ModelProvenance
  - ConfidenceScore
author: AIEC Defense Expert Team
version: 1.0
last_updated: 2026-07-26
status: Complete
---

# 🧪 地端模型蒸餾、資料與模型溯源 SOP

> [!IMPORTANT]
> 本 SOP 專門呼應 NCSIST AIEC 架構圖 (`AIEC_1.pptx`) 中**「地端模型蒸餾/微調」、「Data & Model Provenance 溯源」與「信心分數 (Confidence Score) 校準」**模組。

```
[教師模型 Teacher Model (70B)] ──(Knowledge Distillation 知識蒸餾)──> [邊緣學生模型 Edge Student (7B/3B)]
                                                                               │
                                                                               ▼
[資料/模型溯源 Data & Model Provenance] <──(邏輯檢查 / 清洗規則 / 版本號)──── [信心分數 Confidence Score 校準]
```

## 📌 核心作業程序與控制點

### 1. Edge 端模型蒸餾與輕量化 (Edge Distillation)
- 將地端 70B 主權大模型之知識蒸餾 (Knowledge Distillation) 至 7B/3B 輕量化邊緣模型，兼顧作戰時延與精度。

### 2. 資料與模型溯源 (Data & Model Provenance)
- **Data Provenance (資料溯源)**：記錄每一筆訓練樣本之採集來源、邏輯檢查規則、清洗演算法版本號 (`v1.4.2`) 與標籤品質。
- **Model Provenance (模型溯源)**：追溯模型訓練超參數、權重 Checkpoint 雜湊值與微調歷程。一旦模型發生戰術誤判，能於 10 分鐘內回溯並隔離污染數據。

### 3. 信心分數 (Confidence Score) 與可解釋路徑
- 所有輸出必須伴隨校準後之信心指數 (Confidence Score, score)，評估 ECE 期望校準誤差 ($\mathrm{ECE} \le 0.05$)，防止盲目過度信任。

## 🔗 關聯筆記
- [[AIEC 筆記主索引 (MOC)]]
- [[NCSIST AIEC 國防 AI 評測與認證總體架構]]
- [[SHIELD 治理循環活動]]
- [[5. 信任校準與過度依賴]]
- [[15. 系統軌跡可追溯性與可稽核性]]
""")

    print("All 28 Notes & Templates generated successfully!")

if __name__ == '__main__':
    build_all_notes()
