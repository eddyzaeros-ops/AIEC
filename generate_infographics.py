# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

def build_infographic_s35():
    os.makedirs('infographics', exist_ok=True)
    out_path = os.path.join('infographics', 'info_pipeline_s35.png')
    
    fig, ax = plt.subplots(figsize=(12, 4.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.axis('off')
    
    stages = [
        ("階段 1", "需求界定 & RoE", "定義戰術邊界與 CMMC L2"),
        ("階段 2", "數據分級 & 溯源", "Data/Model Provenance 清洗"),
        ("階段 3", "Cyber Range 紅軍", "ATLAS 威脅與 garak 掃描"),
        ("階段 4", "15項量化評測", "Q1~Q15 門檻與公式確效"),
        ("階段 5", "TRL 放行部署", "核發證書與戰術接管")
    ]
    
    colors = ['#1e3a8a', '#2563eb', '#0284c7', '#0d9488', '#059669']
    
    for i, (stg, title, desc) in enumerate(stages):
        x = 0.5 + i * 2.3
        y = 1.0
        w = 2.0
        h = 2.5
        
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.15",
                                    facecolor='#f8fafc', edgecolor=colors[i], linewidth=2.5)
        ax.add_patch(box)
        
        hdr = patches.FancyBboxPatch((x, y + 1.8), w, 0.7, boxstyle="round,pad=0.05,rounding_size=0.1",
                                     facecolor=colors[i], edgecolor='none')
        ax.add_patch(hdr)
        
        ax.text(x + w/2, y + 2.15, stg, fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center')
        ax.text(x + w/2, y + 1.3, title, fontsize=11, fontweight='bold', color='#0c2340', ha='center', va='center')
        ax.text(x + w/2, y + 0.6, desc, fontsize=8.5, color='#475569', ha='center', va='center', wrap=True)
        
        if i < 4:
            ax.annotate('', xy=(x + w + 0.25, y + h/2), xytext=(x + w + 0.05, y + h/2),
                        arrowprops=dict(arrowstyle="-|>", color='#64748b', lw=3.0, mutation_scale=15))
            
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4.5)
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300, facecolor='#ffffff')
    plt.close(fig)
    print(f"Generated {out_path}")

def build_infographic_s36():
    os.makedirs('infographics', exist_ok=True)
    out_path = os.path.join('infographics', 'info_3d_matrix_s36.png')
    
    fig, ax = plt.subplots(figsize=(12, 4.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.axis('off')
    
    pillars = [
        ("Security (安全機制)", "#1e3a8a", ["• MITRE ATLAS 對抗防禦", "• 無 GPS 網狀通訊防篡改", "• 緊急模型自毀 (<100ms)", "• 零信任 API (SPIFFE/OPA)"]),
        ("Confidentiality (保密機制)", "#2563eb", ["• 100% 地端實體隔離 (Air-Gap)", "• 聯邦學習「模型動，資料不動」", "• Gemma 4 本地 LoRA 微調", "• GGUF 4-bit 量化部署"]),
        ("Auditing (審計機制)", "#0d9488", ["• Data & Model Provenance 溯源", "• XAI 特徵熱力圖 (Point Game)", "• 信心分數校準 (ECE ≤ 0.05)", "• 高保真日誌與 COA 保存"])
    ]
    
    for i, (title, color, items) in enumerate(pillars):
        x = 0.6 + i * 3.8
        y = 0.5
        w = 3.4
        h = 3.5
        
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.2",
                                    facecolor='#f8fafc', edgecolor=color, linewidth=3.0)
        ax.add_patch(box)
        
        hdr = patches.FancyBboxPatch((x, y + 2.7), w, 0.8, boxstyle="round,pad=0.05,rounding_size=0.15",
                                     facecolor=color, edgecolor='none')
        ax.add_patch(hdr)
        
        ax.text(x + w/2, y + 3.1, title, fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center')
        
        for j, item in enumerate(items):
            ax.text(x + 0.3, y + 2.1 - j * 0.55, item, fontsize=10, color='#0c2340', ha='left', va='center')
            
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4.5)
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300, facecolor='#ffffff')
    plt.close(fig)
    print(f"Generated {out_path}")

def build_infographic_s37():
    os.makedirs('infographics', exist_ok=True)
    out_path = os.path.join('infographics', 'info_4tier_compute_s37.png')
    
    fig, ax = plt.subplots(figsize=(12, 4.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.axis('off')
    
    tiers = [
        ("Tier 1: 密集型主權基底模型", "70B 主權大模型 | 民雄院區實體隔離算力", "#0c2340"),
        ("Tier 2: 專家混合架構模型", "8x7B MoE 專用模型 | 電戰、圖像與資安專精", "#1e3a8a"),
        ("Tier 3: 邊緣輕量化模型", "7B / 3B GGUF 量化模型 | 無人載具與前線節點", "#2563eb"),
        ("Tier 4: 戰術邊緣硬體防護", "硬體級防篡改 & 權重緊急自毀 (<100ms)", "#0284c7")
    ]
    
    for i, (name, detail, color) in enumerate(tiers):
        y = 3.2 - i * 0.85
        w = 10.8 - i * 0.8
        x = (12 - w) / 2
        h = 0.7
        
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08,rounding_size=0.12",
                                    facecolor=color, edgecolor='none')
        ax.add_patch(box)
        
        ax.text(x + 0.4, y + h/2, name, fontsize=11, fontweight='bold', color='#ffffff', ha='left', va='center')
        ax.text(x + w - 0.4, y + h/2, detail, fontsize=9.5, color='#e2e8f0', ha='right', va='center')
        
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4.5)
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300, facecolor='#ffffff')
    plt.close(fig)
    print(f"Generated {out_path}")

if __name__ == '__main__':
    build_infographic_s35()
    build_infographic_s36()
    build_infographic_s37()
