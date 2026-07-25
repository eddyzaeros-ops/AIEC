---
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
在多防空陣地、跨艦隊或跨機密網段聯合訓練 AI 時，若將原始作戰數據集中傳送至中央伺服器，將面臨極大資安外洩風險。聯邦學習貫徹**「模型移動，資料不動 (Model moves, data stays)」**原則。

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
- [[國防 AI 安全保密與審計三維矩陣]]
- [[主權 AI 平台與四層 LLM 堆疊]]
