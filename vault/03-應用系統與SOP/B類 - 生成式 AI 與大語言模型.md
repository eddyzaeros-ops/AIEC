---
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
