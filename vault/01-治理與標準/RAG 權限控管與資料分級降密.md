---
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
