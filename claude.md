
# AIEC 專案與 Obsidian 筆記庫操作全域指南 (claude.md)

本文件 (`claude.md`) 彙整 AIEC 國防級 AI 評測專案中，對 Obsidian 筆記庫進行維護、擴充與重構所需之全域核心概念、目錄分類架構與標準化操作規範。

---

## 🏛️ 1. Obsidian Vault 5 大分類目錄架構 (Taxonomy)

Obsidian 筆記庫實體路徑：`G:\我的雲端硬碟\secondbrain\AIEC\`

| 資料夾名稱 | 涵蓋範疇與代表性主題內容 |
| :--- | :--- |
| **`00-Index_and_Templates/`** | • **AIEC 主主題地圖 (MOC)**：第二大腦總導覽入口<br>• **通用筆記模板 (Templates)**：治理、矩陣與系統 SOP 模板 |
| **`01-治理與標準/`** | • **NCSIST AIEC 總體藍圖**與 5 大戰術柱石<br>• **治理雙支柱** (DAGR 指南 & SHIELD 6階段循環)<br>• **ISO 42001 (AIMS)**、**MITRE ATLAS 16大戰術**、**RAG 資料降密防護** |
| **`02-矩陣與架構/`** | • **DoD CDAO Level 1~4 T&E 能力階梯**<br>• **JATIC 7大共通構面**、**6大評測方法論**<br>• **Q1~Q15 15項量化指標與 SOP**、**3D 安全保密審計矩陣** |
| **`03-系統與SOP/`** | • **A類 電腦視覺與目標偵測 SOP** (YOLO/SAM/ART360)<br>• **B類 生成式 AI 與大語言模型 SOP** (garak/NeMo)<br>• **C類 檢索增強生成 RAG SOP** (RAGAS/TruLens/Milvus RBAC)<br>• **D類 AI Agent 與多代理 SOP** (AgentBench/SPIFFE/OPA)<br>• **E類 自主系統與人機協同 SOP** (RoE/HITL/HOTL/HOOTL/VBS4)<br>• **F類 決策支援與預測分析 SOP** (PyOD/MC-Dropout/UQ) |
| **`04-地端架構與工具/`** | • **民雄院區 100% 地端實體隔離 4-Tier 算力堆疊** (70B, 8x7B MoE, 7B/3B, API)<br>• **地端 LLM 推論引擎** (vLLM, llama.cpp, GGUF)<br>• **Lattice 戰術 C2 架構與 Menace 邊緣算力節點**<br>• **聯邦學習 (Federated Learning)** 保密策略與參數在地融合<br>• **戰術邊緣硬體安全與模型緊急自毀** (<100ms Flash/RAM 零化)<br>• **地端模型蒸餾 (Gemma 4 LoRA) 與 Data/Model Provenance 溯源** |
| **`log/`** | • **README.md**：日誌維護規範與協議<br>• **obsidian_operation_log.md**：所有操作歷程主日誌檔 |

---

## 📌 2. 操作 Obsidian 筆記之全域規範 (Global Protocol Rules)

### 規則一：強制自動化異動日誌 (Mandatory Action Logging)
- 凡對 Obsidian 筆記庫進行任何 **新增 (`[CREATE]`)、修改 (`[UPDATE]`)、重構 (`[RESTRUCTURE]`) 或刪除 (`[DELETE]`)** 操作，**必須第一時間追加紀錄至 [log/obsidian_operation_log.md](file:///G:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E碟/secondbrain/AIEC/log/obsidian_operation_log.md)**。
- 條目必須包含：
  1. **時間戳記 (Timestamp)**：`YYYY-MM-DD HH:mm:ss (UTC+8)`
  2. **操作類型 (Action Type)**
  3. **影響檔案 (Target Files)**
  4. **摘要與異動細節 (Summary & Details)**

### 規則二：原子化筆記與雙向連結 (Atomicity & Double-Bracket Links)
- **單一職責與原子化**：每篇筆記專注單一主題（如 `Q4 可中止性`），避免內容過度龐雜。
- **雙向連結網頁圖譜 (`[[...]]`)**：跨主題或概念引註時，必須使用 Obsidian 雙括號（例如在 SOP 中連結 `[[RoE 交戰規則]]` 與 `[[MITRE ATLAS 人工智慧對抗威脅矩陣]]`）。
- **MOC 雙向掛載**：所有新建或調整之筆記，必須同步更新 `00-Index_and_Templates/AIEC 主主題地圖 (MOC).md` 入口連結，防止產生孤立筆記 (Orphan Notes)。

### 規則三：標準化 YAML Frontmatter 元數據
- 所有 `.md` 筆記頭部必須包含 YAML Frontmatter 區塊：
  ```yaml
  ---
  title: "筆記完整標題"
  category: "01-治理與標準 | 02-矩陣與架構 | 03-系統與SOP | 04-地端架構與工具"
  tags: [AIEC, 國防AI, SOP, 評測, 治理]
  created: 2026-07-26 11:55:00
  last_modified: 2026-07-26 11:55:00
  status: "Verified"
  ---
  ```

### 規則四：LaTeX 數學公式標準渲染
- 凡涉及量化指標計算公式（如 Q1~Q15），一律採用標準 LaTeX 格式 (`$...$` 內聯或 `$$...$$` 區塊)，確保 Obsidian 內建 MathJax 技術能夠 100% 正確編譯與視覺呈現。

### 規則五：語言偏好
- 所有對話、思考、筆記內容、說明與維護日誌，必須一律使用**繁體中文 (Traditional Chinese)** 呈現。

---
