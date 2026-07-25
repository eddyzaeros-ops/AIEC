$code = @"
using System;
using System.IO;
using System.Threading.Tasks;
using Windows.Graphics.Imaging;
using Windows.Media.Ocr;
using Windows.Storage;
using Windows.Storage.Streams;

public class OcrRunner {
    public static void Execute() {
        ExecuteAsync().GetAwaiter().GetResult();
    }
    public static async Task ExecuteAsync() {
        string imgPath = Path.Combine(Directory.GetCurrentDirectory(), "slide8_image.png");
        StorageFile file = await StorageFile.GetFileFromPathAsync(imgPath);
        using (IRandomAccessStream stream = await file.OpenAsync(FileAccessMode.Read)) {
            BitmapDecoder decoder = await BitmapDecoder.CreateAsync(stream);
            SoftwareBitmap bitmap = await decoder.GetSoftwareBitmapAsync();
            OcrEngine engine = OcrEngine.TryCreateFromUserProfileLanguages();
            if (engine == null) {
                engine = OcrEngine.TryCreateFromLanguage(new Windows.Globalization.Language("zh-Hant"));
            }
            OcrResult result = await engine.RecognizeAsync(bitmap);
            Console.WriteLine(result.Text);
        }
    }
}
"@

$winmdPath = "C:\Windows\System32\WinMetadata\Windows.Media.Ocr.winmd"
$winmdPath2 = "C:\Windows\System32\WinMetadata\Windows.Foundation.UniversalApiContract.winmd"

Add-Type -TypeDefinition $code -ReferencedAssemblies "System.Runtime.WindowsRuntime.dll", $winmdPath2, $winmdPath -Language CSharp
[OcrRunner]::Execute()
