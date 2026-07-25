# -*- coding: utf-8 -*-
import os, sys
import collections
import collections.abc

if not hasattr(collections, 'Iterable'):
    collections.Iterable = collections.abc.Iterable

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def set_pure_white_bg(slide):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)

def add_header(slide, title_text, category_text):
    NAVY = RGBColor(12, 35, 64)
    BLUE = RGBColor(37, 99, 235)
    
    tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(14.4), Inches(0.4))
    tf_cat = tb_cat.text_frame
    tf_cat.word_wrap = True
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = BLUE
    p_cat.font.name = "Arial"
    
    tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(14.4), Inches(0.7))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.size = Pt(24)
    p_t.font.bold = True
    p_t.font.color.rgb = NAVY
    p_t.font.name = "微軟正黑體"

def add_icon_card(slide, left, top, width, height, icon, title_zh, title_en, accent_color=None):
    NAVY = RGBColor(12, 35, 64)
    BG_CARD = RGBColor(248, 250, 252)
    BORDER_CARD = RGBColor(226, 232, 240)
    if accent_color is None: accent_color = RGBColor(37, 99, 235)
    
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    card.fill.solid()
    card.fill.fore_color.rgb = BG_CARD
    card.line.color.rgb = BORDER_CARD
    card.line.width = Pt(1.0)
    
    tb = slide.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.2), Inches(width - 0.4), Inches(0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = f"{icon}  {title_zh}"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = accent_color
    p.font.name = "微軟正黑體"
    
    p_sub = tf.add_paragraph()
    p_sub.text = title_en
    p_sub.font.size = Pt(11)
    p_sub.font.bold = True
    p_sub.font.color.rgb = NAVY
    p_sub.font.name = "Arial"

def add_formatted_text(p, text, font_size=13, default_color=None, bold_color=None):
    NAVY = RGBColor(12, 35, 64)
    DARK_GRAY = RGBColor(50, 50, 50)
    if default_color is None: default_color = DARK_GRAY
    if bold_color is None: bold_color = NAVY
    
    parts = text.split('**')
    for idx, part in enumerate(parts):
        if not part:
            continue
        is_bold_part = (idx % 2 == 1)
        
        chunk = ""
        current_ascii = None
        for char in part:
            char_ascii = (ord(char) < 128)
            if current_ascii is None:
                current_ascii = char_ascii
                chunk += char
            elif current_ascii == char_ascii:
                chunk += char
            else:
                run = p.add_run()
                run.text = chunk
                run.font.bold = is_bold_part
                run.font.color.rgb = bold_color if is_bold_part else default_color
                run.font.size = Pt(font_size + 1) if is_bold_part else Pt(font_size)
                run.font.name = "Arial" if current_ascii else "微軟正黑體"
                chunk = char
                current_ascii = char_ascii
        if chunk:
            run = p.add_run()
            run.text = chunk
            run.font.bold = is_bold_part
            run.font.color.rgb = bold_color if is_bold_part else default_color
            run.font.size = Pt(font_size + 1) if is_bold_part else Pt(font_size)
            run.font.name = "Arial" if current_ascii else "微軟正黑體"

def add_formatted_bullets(tf, bullet_list, font_size=13, text_color=None, bold_color=None):
    tf.word_wrap = True
    for i, b_str in enumerate(bullet_list):
        if i == 0 and len(tf.paragraphs[0].text) == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
            
        p.space_after = Pt(6)
        
        # Calculate hanging indent (懸掛縮排)
        # Determine prefix level (indentation level)
        is_sub_bullet = b_str.startswith("   - ") or b_str.startswith("   • ")
        prefix_len = 5 if is_sub_bullet else 3 # e.g. "1. " = 3 chars, "   - " = 5 chars
        
        # OpenXML hanging indent attributes
        pPr = p._p.get_or_add_pPr()
        if is_sub_bullet:
            pPr.set('marL', '640000') # ~0.70 inches left margin
            pPr.set('indent', '-320000') # ~-0.35 inches hanging indent
        else:
            pPr.set('marL', '340000') # ~0.37 inches left margin
            pPr.set('indent', '-340000') # ~-0.37 inches hanging indent
            
        add_formatted_text(p, b_str, font_size=font_size, default_color=text_color, bold_color=bold_color)
