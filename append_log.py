# -*- coding: utf-8 -*-
import os

log_path = r'G:\我的雲端硬碟\secondbrain\AIEC\log\obsidian_operation_log.md'
with open(log_path, 'r', encoding='utf-8') as f:
    content = f.read()

entry_8 = """
### 8. 更新 MOC 地圖雙向連結與日誌索引
- **時間戳記**：`2026-07-26 11:48:25 (UTC+8)`
- **操作類型**：`[UPDATE]`
- **影響檔案**：
  - `00-Index_and_Templates/AIEC 主主題地圖 (MOC).md`
- **摘要與細節**：
  - 在主主題地圖 (MOC) 尾端新增《專案操作與異動日誌 (Operation Logs)》專區，雙向連結 `[[log/obsidian_operation_log]]` 與 `[[log/README]]`，完備 Obsidian 審計紀錄導覽功能。

---
"""

if '### 8.' not in content:
    content += entry_8
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Entry 8 to operation log!")
