Add-Type -AssemblyName System.Runtime.WindowsRuntime

$asTaskGeneric = ([System.Windows.Forms.Form].Assembly.GetType('System.Windows.Forms.Application')).Assembly.GetType('System.Runtime.WindowsRuntimeSystemExtensions').GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' }

[void][Windows.Globalization.Language, Windows.Globalization, ContentType=WindowsRuntime]
[void][Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics, ContentType=WindowsRuntime]
[void][Windows.Media.Ocr.OcrEngine, Windows.Media.Ocr, ContentType=WindowsRuntime]
[void][Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]

$imgPath = Join-Path (Get-Location) 'slide8_image.png'
$fileTask = [Windows.Storage.StorageFile]::GetFileFromPathAsync($imgPath)
while ($fileTask.Status -eq 'Started') { Start-Sleep -Milliseconds 50 }
$file = $fileTask.GetResults()

$streamTask = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read)
while ($streamTask.Status -eq 'Started') { Start-Sleep -Milliseconds 50 }
$stream = $streamTask.GetResults()

$decoderTask = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
while ($decoderTask.Status -eq 'Started') { Start-Sleep -Milliseconds 50 }
$decoder = $decoderTask.GetResults()

$bitmapTask = $decoder.GetSoftwareBitmapAsync()
while ($bitmapTask.Status -eq 'Started') { Start-Sleep -Milliseconds 50 }
$bitmap = $bitmapTask.GetResults()

$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
if ($null -eq $engine) {
    $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new("zh-Hant"))
}
$ocrTask = $engine.RecognizeAsync($bitmap)
while ($ocrTask.Status -eq 'Started') { Start-Sleep -Milliseconds 50 }
$result = $ocrTask.GetResults()
Write-Output $result.Text
