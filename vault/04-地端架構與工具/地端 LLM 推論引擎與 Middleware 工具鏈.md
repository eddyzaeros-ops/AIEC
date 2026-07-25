---
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
