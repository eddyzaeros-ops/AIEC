---
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
