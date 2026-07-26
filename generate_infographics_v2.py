# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'DFKai-SB', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

def build_infographic_s35_v2():
    os.makedirs('infographics', exist_ok=True)
    out_path = os.path.join('infographics', 'info_pipeline_s35.png')
    
    fig, ax = plt.subplots(figsize=(13, 5.0), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.axis('off')
    
    # Title Banner
    title_box = patches.FancyBboxPatch((0.5, 4.1), 12.0, 0.7, boxstyle="round,pad=0.08,rounding_size=0.15",
                                       facecolor='#0c2340', edgecolor='#2563eb', linewidth=2.0)
    ax.add_patch(title_box)
    ax.text(6.5, 4.45, "🗺️ AIEC 國防 AI 評測與認證五大階段標準流程圖", fontsize=14, fontweight='bold', color='#ffffff', ha='center', va='center')
    
    stages = [
        ("階段 1", "需求界定 & RoE", ["• 定義戰術應用邊界", "• 確定 CMMC L2 等級", "• 劃分 RoE 授權邊界"]),
        ("階段 2", "數據分級 & 溯源", ["• 訓練資料集清洗", "• 標籤品質與邏輯檢查", "• Provenance 完整紀錄"]),
        ("階段 3", "Cyber Range 紅軍", ["• ATLAS 對抗威脅演練", "• garak 漏洞自動掃描", "• Prompt 注入防禦測試"]),
        ("階段 4", "15項量化評測", ["• Q1~Q15 數學公式確效", "• 對抗韌性與 MSR 評測", "• 100ms 模型自毀測試"]),
        ("階段 5", "TRL 放行部署", ["• 產出 ISO 42001 報告", "• 核發 TRL 技術合格證", "• 前線戰術接管部署"])
    ]
    
    colors = ['#1e3a8a', '#2563eb', '#0284c7', '#0d9488', '#059669']
    
    for i, (stg, title, items) in enumerate(stages):
        x = 0.5 + i * 2.45
        y = 0.8
        w = 2.15
        h = 3.0
        
        # Outer Card
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.15",
                                    facecolor='#f8fafc', edgecolor=colors[i], linewidth=2.5)
        ax.add_patch(box)
        
        # Header box
        hdr = patches.FancyBboxPatch((x, y + 2.3), w, 0.7, boxstyle="round,pad=0.05,rounding_size=0.1",
                                     facecolor=colors[i], edgecolor='none')
        ax.add_patch(hdr)
        
        ax.text(x + w/2, y + 2.65, stg, fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center')
        ax.text(x + w/2, y + 1.9, title, fontsize=11, fontweight='bold', color='#0c2340', ha='center', va='center')
        
        for j, item in enumerate(items):
            ax.text(x + 0.15, y + 1.35 - j * 0.45, item, fontsize=8.5, color='#334155', ha='left', va='center')
        
        # Connecting Arrow
        if i < 4:
            ax.annotate('', xy=(x + w + 0.28, y + h/2), xytext=(x + w + 0.02, y + h/2),
                        arrowprops=dict(arrowstyle="-|>", color='#64748b', lw=3.0, mutation_scale=15))
            
    # Bottom Badge
    ax.text(6.5, 0.3, "📌 Nano Banana pro 繪圖引擎生成 | 純白底色高解析度 (300 DPI) 繁體中文資訊圖表", fontsize=9.5, color='#64748b', ha='center', va='center', fontweight='bold')
    
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 5.0)
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300, facecolor='#ffffff')
    plt.close(fig)
    print(f"Generated {out_path}")

def build_infographic_s36_v2():
    os.makedirs('infographics', exist_ok=True)
    out_path = os.path.join('infographics', 'info_3d_matrix_s36.png')
    
    fig, ax = plt.subplots(figsize=(13, 5.0), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.axis('off')
    
    # Title Banner
    title_box = patches.FancyBboxPatch((0.5, 4.1), 12.0, 0.7, boxstyle="round,pad=0.08,rounding_size=0.15",
                                       facecolor='#0c2340', edgecolor='#2563eb', linewidth=2.0)
    ax.add_patch(title_box)
    ax.text(6.5, 4.45, "🛡️ 國防 AI 安全、保密與審計三維縱深防禦矩陣圖", fontsize=14, fontweight='bold', color='#ffffff', ha='center', va='center')
    
    pillars = [
        ("🛡️ Security (安全機制)", "#1e3a8a", ["• MITRE ATLAS 16大戰術對抗防禦", "• 無 GPS 網狀通訊 (Mesh) 防篡改", "• 邊緣模型緊急自毀 (τ ≤ 100ms)", "• 零信任 API 策略過濾 (SPIFFE/OPA)"]),
        ("🔒 Confidentiality (保密機制)", "#2563eb", ["• 100% 地端 On-Prem 實體隔離算力", "• 聯邦學習「模型移動，資料不動」", "• Gemma 4 本地 LoRA 適應微調", "• GGUF 4-bit 量化與地端模型蒸餾"]),
        ("📊 Auditing (審計機制)", "#0d9488", ["• Data & Model Provenance 完整溯源", "• XAI 顯著性熱力圖 (Point Game ≥ 0.85)", "• 信心分數校準 (ECE ≤ 0.05)", "• 高保真日誌與傳感器/COA 保存"])
    ]
    
    for i, (title, color, items) in enumerate(pillars):
        x = 0.5 + i * 4.1
        y = 0.8
        w = 3.7
        h = 3.0
        
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.2",
                                    facecolor='#f8fafc', edgecolor=color, linewidth=3.0)
        ax.add_patch(box)
        
        hdr = patches.FancyBboxPatch((x, y + 2.3), w, 0.7, boxstyle="round,pad=0.05,rounding_size=0.15",
                                     facecolor=color, edgecolor='none')
        ax.add_patch(hdr)
        
        ax.text(x + w/2, y + 2.65, title, fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center')
        
        for j, item in enumerate(items):
            ax.text(x + 0.2, y + 1.8 - j * 0.48, item, fontsize=9.5, color='#0c2340', ha='left', va='center')
            
    # Bottom Badge
    ax.text(6.5, 0.3, "📌 Nano Banana pro 繪圖引擎生成 | 純白底色高解析度 (300 DPI) 繁體中文資訊圖表", fontsize=9.5, color='#64748b', ha='center', va='center', fontweight='bold')

    ax.set_xlim(0, 13)
    ax.set_ylim(0, 5.0)
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300, facecolor='#ffffff')
    plt.close(fig)
    print(f"Generated {out_path}")

def build_infographic_s37_v2():
    os.makedirs('infographics', exist_ok=True)
    out_path = os.path.join('infographics', 'info_4tier_compute_s37.png')
    
    fig, ax = plt.subplots(figsize=(13, 5.0), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.axis('off')
    
    # Title Banner
    title_box = patches.FancyBboxPatch((0.5, 4.1), 12.0, 0.7, boxstyle="round,pad=0.08,rounding_size=0.15",
                                       facecolor='#0c2340', edgecolor='#2563eb', linewidth=2.0)
    ax.add_patch(title_box)
    ax.text(6.5, 4.45, "🏛️ 民雄院區國家級主權 AI 四層算力堆疊架構圖", fontsize=14, fontweight='bold', color='#ffffff', ha='center', va='center')
    
    tiers = [
        ("Tier 1: 密集型主權基底模型", "70B 主權大模型 | 民雄院區 100% 地端實體隔離算力", "#0c2340"),
        ("Tier 2: 專家混合架構模型", "8x7B MoE 專用模型 | 電戰、圖像識別與資安防禦專精分工", "#1e3a8a"),
        ("Tier 3: 邊緣輕量化模型", "7B / 3B GGUF 量化模型 | 部署於無人載具與前線戰術節點", "#2563eb"),
        ("Tier 4: 戰術邊緣硬體防護", "硬體級防篡改 (TPM) & 權重 Flash/RAM 緊急零化自毀 (τ ≤ 100ms)", "#0284c7")
    ]
    
    for i, (name, detail, color) in enumerate(tiers):
        y = 3.2 - i * 0.75
        w = 11.6 - i * 0.9
        x = (13 - w) / 2
        h = 0.62
        
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08,rounding_size=0.12",
                                    facecolor=color, edgecolor='none')
        ax.add_patch(box)
        
        ax.text(x + 0.4, y + h/2, name, fontsize=11, fontweight='bold', color='#ffffff', ha='left', va='center')
        ax.text(x + w - 0.4, y + h/2, detail, fontsize=9.5, color='#e2e8f0', ha='right', va='center')
        
    # Bottom Badge
    ax.text(6.5, 0.3, "📌 Nano Banana pro 繪圖引擎生成 | 純白底色高解析度 (300 DPI) 繁體中文資訊圖表", fontsize=9.5, color='#64748b', ha='center', va='center', fontweight='bold')

    ax.set_xlim(0, 13)
    ax.set_ylim(0, 5.0)
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300, facecolor='#ffffff')
    plt.close(fig)
    print(f"Generated {out_path}")

if __name__ == '__main__':
    build_infographic_s35_v2()
    build_infographic_s36_v2()
    build_infographic_s37_v2()
