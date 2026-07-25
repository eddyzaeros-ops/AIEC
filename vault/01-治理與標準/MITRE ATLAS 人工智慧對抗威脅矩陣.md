---
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
