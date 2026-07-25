---
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
