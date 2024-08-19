# Python YouTube Video Cutout App

## Proje Açıklaması

Python YouTube Video Cutout App, kullanıcıların YouTube videolarını indirip belirli bir süre aralığında kesmelerine olanak tanıyan bir Python uygulamasıdır. Bu uygulama, PyQt5 kullanılarak oluşturulmuş modern bir GUI ile kullanıcılara video indirme ve düzenleme işlevlerini sunar. Kullanıcılar ayrıca videonun çözünürlüğünü seçebilir ve kesilen videonun dosya adında YouTube video ID'sini görebilirler.

## Özellikler

- **YouTube Video İndirme:** Kullanıcıların YouTube bağlantısını girerek videoyu bilgisayarlarına indirmelerini sağlar.
- **Video Kesme:** İndirilen videoyu belirlenen başlangıç ve bitiş zamanına göre keser.
- **Çözünürlük Seçimi:** Videonun çözünürlüğünü seçme imkanı sunar (144p, 360p, 480p, 720p, 1080p, 1440p, 2160p).
- **Dosya Adı Düzenleme:** Kesilen video dosyasının adını, videonun YouTube ID'sini içerecek şekilde düzenler.
- **Gelişmiş GUI:** PyQt5 kullanılarak tasarlanmış kullanıcı dostu bir arayüz.

## Gereksinimler

- Python 3.x
- PyQt5
- yt-dlp
- moviepy
- FFmpeg

## Kurulum

### Python ve Gerekli Kütüphaneleri Kurma

Python 3.x'i [Python'un resmi sitesinden](https://www.python.org) indirip kurun. Aşağıdaki komutları kullanarak gerekli Python kütüphanelerini yükleyin:

bash
pip install PyQt5 yt-dlp moviepy

FFmpeg Kurulumu
FFmpeg'in en son sürümünü FFmpeg'in resmi sitesinden indirin ve sisteminizde kurun. FFmpeg'in çalışabilir olduğundan emin olun ve ortam değişkenlerine ekleyin.

Kullanım
Uygulamayı Başlatma
Uygulamayı başlatmak için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:

bash
Kodu kopyala
python main.py
Video İndirme ve Kesme
YouTube Linki: İndirmek istediğiniz YouTube videosunun URL'sini girin.
Başlangıç Zamanı: Videonun kesilmeye başlanacağı zamanı saat:dakika:saniye formatında girin.
Bitiş Zamanı: Videonun kesilmesini istediğiniz zamanı saat:dakika:saniye formatında girin.
Çözünürlük: İstediğiniz video çözünürlüğünü seçin.
İndir ve Kes: Butonuna tıklayarak video indirme ve kesme işlemini başlatın.
Kod Açıklamaları
YoutubeDownloader Sınıfı: Arayüz: PyQt5 kullanılarak oluşturulan GUI bileşenlerini içerir.
download_video Metodu: Kullanıcının girdiği URL, zaman aralığı ve çözünürlük bilgilerini alır ve download_and_cut_video fonksiyonunu çağırır.
download_and_cut_video Fonksiyonu:
Video İndirme: yt_dlp kütüphanesi kullanılarak video indirilir.
Video Kesme: moviepy kütüphanesi kullanılarak video kesilir ve belirtilen çözünürlükte kaydedilir.
convert_to_seconds Fonksiyonu: Zaman dönüşümü: saat:dakika:saniye formatındaki zaman bilgilerini saniyeye dönüştürür.
Hata Ayıklama
Eğer bir hata ile karşılaşırsanız, hata mesajını dikkatlice okuyun ve yukarıdaki adımları takip ederek gerekli düzeltmeleri yapın. Herhangi bir hata ile ilgili ek destek için GitHub Issues sayfasını kullanabilirsiniz.

İletişim
Herhangi bir soru veya geri bildirim için merve_basak64@hotmail.com ile iletişime geçebilirsiniz.
