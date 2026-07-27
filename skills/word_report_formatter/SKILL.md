---
name: word_report_formatter
description: 全自動 Word 報告格式化與 VBA 巨集目錄生成工具 Skill。提供規範之 Heading 1 (20pt), Heading 2 (16pt), Heading 3 (14pt 置中圖表標題) 樣式排版，頁尾頁碼，並在第 2, 3, 4 頁原位嵌入主目錄、表目錄與圖目錄，內嵌 6 大任務 VBA 巨集並透過 Word COM 全自動計算執行。
---

# Word 報告全自動格式化與目錄生成 Skill 指引 (Word Report Formatter Skill)

## 📌 概述與核心功能

本 Skill 旨在協助使用者快速將 Markdown 或文字報告轉換為具備國際標準格式、視覺精美且嚴謹之 Microsoft Word (.docx / .docm) 國防/專業報告文件。

---

## 🎯 4 大核心規範與參數定義

當使用者呼叫本 Skill 時，可自訂下列樣式與排版參數（若未指定則自動套用預設標準）：

### 1. 字型與字級規範 (Typography Parameters)
- **中文預設字型 (`Font_ZH`)**：`SimHei` (中黑體)
- **英文預設字型 (`Font_EN`)**：`Arial`
- **標題一 (`Heading 1`)**：**20 pt**、加粗、主色 `#0C2340` (深藍)
- **標題二 (`Heading 2`)**：**16 pt**、加粗、副色 `#2563EB` (亮藍)
- **標題三 (`Heading 3`)**：**14 pt**、加粗、輔色 `#1E3A8A` (深紺)；**圖表標題必須強制置中對齊 (`WD_ALIGN_PARAGRAPH.CENTER`)**
- **內文 (`Normal`)**：**14 pt**、行高 1.35、字色 `#334155` (深灰)

### 2. 頁面佈局與目錄結構 (Page Architecture)
- **第 1 頁 (Page 1)**：獨立封面頁 (Cover Page)，包含題目、副標題與詮釋資料表格，末尾加 `PageBreak`。
- **第 2 頁 (Page 2)**：獨立「📋 目錄 (Table of Contents)」，內嵌 `{ TOC \o "1-2" \h \z \u }`。
- **第 3 頁 (Page 3)**：獨立「📊 表目錄 (List of Tables)」，內嵌 `{ TOC \h \z \c "表" }`，並於每個表格標題加入原生 `{ SEQ 表 \* ARABIC }` 欄位。
- **第 4 頁 (Page 4)**：獨立「🖼️ 圖目錄 (List of Figures)」，內嵌 `{ TOC \h \z \c "圖" }`，並於每個圖片標題加入原生 `{ SEQ 圖 \* ARABIC }` 欄位。
- **第 5 頁起 (Page 5 Onwards)**：正文第一章至第五章順延開始，**文件末尾絕不放置任何殘留目錄**。
- **頁尾頁碼 (Footer)**：右對齊，格式為 `第 X 頁`，使用原生 `PAGE` 欄位。

---

## 💻 6 大自動化任務 VBA 巨集程式碼 (`AIEC_AutoTOC_Module`)

本巨集會內嵌於 Word `.docm` 檔案中，並可在使用者開啟 Word 時自動或手動執行：

```vba
Sub FormatHeadingsAndInsertFourPagesTOC()
    ' =========================================================================
    ' 巨集名稱：FormatHeadingsAndInsertFourPagesTOC
    ' 1. 自動辨識『第X章』設為 Heading 1，『X.X』設為 Heading 2
    ' 2. 在整份文件的第二頁 (P2)，自動更新標準『目錄』 (TablesOfContents)
    ' 3. 自動辨識『表』開頭表格標題，設為 Heading 3 樣式且置中對齊
    ' 4. 在整份文件的第三頁 (P3)，自動更新標準『表目錄』 (TablesOfFigures 1)
    ' 5. 自動辨識『圖』開頭圖片標題，設為 Heading 3 樣式且置中對齊
    ' 6. 在整份文件的第四頁 (P4)，自動更新標準『圖目錄』 (TablesOfFigures 2)
    ' =========================================================================
    
    Dim doc As Document
    Dim para As Paragraph
    Dim paraText As String
    Dim regExChapter As Object
    Dim regExSection As Object
    Dim regExTable As Object
    Dim regExFigure As Object
    Dim tocObj As TableOfContents
    Dim tofObj As TableOfFigures
    
    Set doc = ActiveDocument
    
    Set regExChapter = CreateObject("VBScript.RegExp")
    With regExChapter
        .Pattern = "^第[0-9一二三四五六七八九十百]+章"
        .IgnoreCase = True
        .Global = False
    End With
    
    Set regExSection = CreateObject("VBScript.RegExp")
    With regExSection
        .Pattern = "^[0-9]+\.[0-9]+"
        .IgnoreCase = True
        .Global = False
    End With

    Set regExTable = CreateObject("VBScript.RegExp")
    With regExTable
        .Pattern = "^表\s*"
        .IgnoreCase = True
        .Global = False
    End With

    Set regExFigure = CreateObject("VBScript.RegExp")
    With regExFigure
        .Pattern = "^圖\s*"
        .IgnoreCase = True
        .Global = False
    End With
    
    ' 遍歷全文段落，設定標題樣式與置中對齊
    For Each para In doc.Paragraphs
        paraText = Trim(para.Range.Text)
        If Right(paraText, 1) = vbCr Or Right(paraText, 1) = Chr(13) Then
            paraText = Left(paraText, Len(paraText) - 1)
        End If
        paraText = Trim(paraText)
        
        If Len(paraText) > 0 Then
            If regExChapter.Test(paraText) Then
                para.Style = doc.Styles(wdStyleHeading1)
            ElseIf regExSection.Test(paraText) Then
                para.Style = doc.Styles(wdStyleHeading2)
            ElseIf regExTable.Test(paraText) Then
                para.Style = doc.Styles(wdStyleHeading3)
                para.Alignment = wdAlignParagraphCenter
            ElseIf regExFigure.Test(paraText) Then
                para.Style = doc.Styles(wdStyleHeading3)
                para.Alignment = wdAlignParagraphCenter
            End If
        End If
    Next para
    
    ' 全局更新欄位、主目錄 (TablesOfContents) 與圖表目錄 (TablesOfFigures)
    doc.Fields.Update
    For Each tocObj In doc.TablesOfContents
        tocObj.Update
    Next tocObj
    For Each tofObj In doc.TablesOfFigures
        tofObj.Update
    Next tofObj
    
    MsgBox "6 大任務巨集執行成功！目錄 (P2)、表目錄 (P3) 與圖目錄 (P4) 已精準顯示內容！", _
           vbInformation, "AIEC 國防 AI 巨集"
End Sub
```

---

## 🛠️ Python 自動化建置與 Word COM 執行流程 (Implementation Workflow)

1. **XML 節點原位嵌入**：
   - 使用 `p._p.addnext(sdt_elem)` 將 `<w:sdt>` 目錄組件精準嵌入至第 2, 3, 4 頁標題下方，絕不使用 `body.append()` 避免目錄推至文末。
2. **圖表 SEQ 功能變數**：
   - 於所有 `Heading 3` 表格標題加入 `<w:fldSimple w:instr="SEQ 表 \* ARABIC"/>`。
   - 於所有 `Heading 3` 圖片標題加入 `<w:fldSimple w:instr="SEQ 圖 \* ARABIC"/>`。
3. **Word COM 自動化調用與快取快照**：
   - 啟動 `win32com.client.Dispatch("Word.Application")`。
   - 匯入 VBA 巨集模組 `AIEC_AutoTOC_Module`。
   - 執行 `wdoc.Fields.Update()`、`wdoc.TablesOfContents(1).Update()`、`wdoc.TablesOfFigures(1).Update()` 與 `wdoc.TablesOfFigures(2).Update()`。
   - 儲存產出 `.docx` 與 `.docm` 檔案並同步至使用者桌面。
