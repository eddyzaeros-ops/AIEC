using System;
using System.IO;
using System.Threading.Tasks;
using Windows.Graphics.Imaging;
using Windows.Media.Ocr;
using Windows.Storage;
using Windows.Storage.Streams;

class Program {
    static void Main(string[] args) {
        string imgPath = Path.Combine(Directory.GetCurrentDirectory(), "extracted_images", "slide_08_img_02.png");
        if (args.Length > 0) imgPath = args[0];
        
        Task.Run(async () => {
            StorageFile file = await StorageFile.GetFileFromPathAsync(imgPath);
            using (IRandomAccessStream stream = await file.OpenAsync(FileAccessMode.Read)) {
                BitmapDecoder decoder = await BitmapDecoder.CreateAsync(stream);
                SoftwareBitmap bitmap = await decoder.GetSoftwareBitmapAsync();
                OcrEngine engine = OcrEngine.TryCreateFromUserProfileLanguages();
                if (engine == null) {
                    engine = OcrEngine.TryCreateFromLanguage(new Windows.Globalization.Language("zh-Hant"));
                }
                OcrResult result = await engine.RecognizeAsync(bitmap);
                Console.WriteLine("=== OCR START ===");
                Console.WriteLine(result.Text);
                Console.WriteLine("=== OCR END ===");
            }
        }).Wait();
    }
}
