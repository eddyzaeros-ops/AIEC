# -*- coding: utf-8 -*-
import os, sys
import re

vault_path = r'G:\我的雲端硬碟\secondbrain\AIEC'

# Mapping of subfolders to category names
CAT_MAP = {
    "00-Index_and_Templates": "00-導覽與模板",
    "01-治理與標準": "01-治理與標準",
    "02-矩陣與架構": "02-矩陣與架構",
    "03-系統與SOP": "03-系統與SOP",
    "04-地端架構與工具": "04-地端架構與工具"
}

INFOGRAPHIC_NOTICE = """\n> 📌 **資訊圖表繪製規範**：本主題相關之高解析度戰術與系統「資訊圖表」(Infographics / Visual Architecture Diagrams) 統一採用 **Nano Banana pro** 繪圖引擎進行繪製與視覺化呈現。\n"""

ARCHITECT_HEADER = """\n> 🛡️ **技術長與架構師視角 (CTO & Chief Architect Note)**：本筆記由國防 AI 技術長暨系統架構師觀點編撰，整合資安 ISO 42001 (AIMS)、CMMC Level 2、Threat Hunting、紅藍隊對抗與語意網 (Ontology/Knowledge Graphs) 核心原則，對齊國防 AI 應用發展藍圖。\n"""

def process_note(filepath):
    filename = os.path.basename(filepath)
    rel_dir = os.path.basename(os.path.dirname(filepath))
    
    if filename == 'claude.md' or filename == 'README.md' or 'log' in filepath:
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Frontmatter check/update
    title_str = filename.replace('.md', '')
    cat_str = CAT_MAP.get(rel_dir, "00-導覽與模板")
    
    frontmatter_template = f"""---
title: "{title_str}"
category: "{cat_str}"
tags: [AIEC, 國防AI, 評測SOP, ISO42001, CMMC_L2, NanoBanana_pro]
architect_role: "國防 AI 應用技術長 & 系統架構師"
created: 2026-07-26 12:35:00
last_modified: 2026-07-26 12:35:00
status: "Verified & Standardized"
---
"""

    if not content.startswith('---'):
        content = frontmatter_template + content
        modified = True
    else:
        # Update status or tags if needed
        if 'status:' not in content:
            content = re.sub(r'(---\s*\n)', r'\1status: "Verified & Standardized"\narchitect_role: "國防 AI 應用技術長 & 系統架構師"\n', content, count=1)
            modified = True

    # 2. Add Architect Notice if missing
    if '技術長與架構師視角' not in content and filename != 'AIEC 主主題地圖 (MOC).md' and not filename.startswith('Template'):
        # Insert after first header or frontmatter
        fm_end = content.find('---', 3)
        if fm_end != -1:
            insert_pos = fm_end + 3
            content = content[:insert_pos] + ARCHITECT_HEADER + content[insert_pos:]
            modified = True

    # 3. Add Nano Banana pro Infographic notice if note mentions diagrams/architectures/charts
    if ('架構' in content or '圖' in content or 'MOC' in filename or 'SOP' in filename or '藍圖' in content) and 'Nano Banana pro' not in content:
        fm_end = content.find('---', 3)
        if fm_end != -1:
            insert_pos = fm_end + 3
            content = content[:insert_pos] + INFOGRAPHIC_NOTICE + content[insert_pos:]
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

updated_count = 0
for root, dirs, files in os.walk(vault_path):
    for f in files:
        if f.endswith('.md') and 'log' not in root:
            fp = os.path.join(root, f)
            if process_note(fp):
                updated_count += 1
                print(f"Refined note: {f}")

print(f"Total notes refined & standardized: {updated_count}")
