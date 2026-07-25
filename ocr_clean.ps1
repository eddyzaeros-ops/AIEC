Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Runtime.WindowsRuntime

$extAssembly = [System.IO.File].Assembly.GetType("System.Runtime.WindowsRuntimeSystemExtensions")
if ($null -eq $extAssembly) {
    # Load System.Runtime.WindowsRuntime assembly
    $assemblies = [AppDomain]::CurrentDomain.GetAssemblies()
    foreach ($a in $assemblies) {
        $t = $a.GetType("System.Runtime.WindowsRuntimeSystemExtensions")
        if ($t) { $extAssembly = $t; break }
    }
}

[void][Windows.Media.Ocr.OcrEngine, Windows.Media.Ocr, ContentType=WindowsRuntime]
[void][Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics, ContentType=WindowsRuntime]
[void][Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]

$imgPath = (Resolve-Path "slide8_image.png").Path
$fileTask = [Windows.Storage.StorageFile]::GetFileFromPathAsync($imgPath)
while ($fileTask.Status -eq 0) { Start-Sleep -Milliseconds 50 }
$file = $fileTask.GetResults()

$streamTask = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read)
while ($streamTask.Status -eq 0) { Start-Sleep -Milliseconds 50 }
$stream = $streamTask.GetResults()

$decoderTask = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
while ($decoderTask.Status -eq 0) { Start-Sleep -Milliseconds 50 }
$decoder = $decoderTask.GetResults()

$bitmapTask = $decoder.GetSoftwareBitmapAsync()
while ($bitmapTask.Status -eq 0) { Start-Sleep -Milliseconds 50 }
$bitmap = $bitmapTask.GetResults()

$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
if (-not $engine) {
    $lang = [Windows.Globalization.Language]::new("zh-Hant")
    $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($lang)
}

$ocrTask = $engine.RecognizeAsync($bitmap)
while ($ocrTask.Status -eq 0) { Start-Sleep -Milliseconds 50 }
$result = $ocrTask.GetResults()

Write-Host "=== OCR RESULT ==="
Write-Host $result.Text
Write-Host "=================="
