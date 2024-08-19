import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import yt_dlp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os

# FFmpeg yolu
FFMPEG_PATH = r'C:\ffmpeg-7.0.2\bin\ffmpeg.exe'

# FFmpeg yolunu ortam değişkenlerine ekleme
os.environ['FFMPEG_BINARY'] = FFMPEG_PATH

class YoutubeDownloader(QWidget):
    def __init__(self):
        super().__init__()

        # Arayüz Elemanları
        self.setWindowTitle('YouTube Video Downloader')
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("""
            QWidget {
                background-color: black;
                color: white;
            }
            QLabel {
                color: white;
                font-size: 14px;
            }
            QLineEdit {
                background-color: black;
                border: 2px solid #d4af37;
                color: white;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #d4af37;
                color: black;
                border: 2px solid #d4af37;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #b8972e;
            }
            QComboBox {
                background-color: black;
                border: 2px solid #d4af37;
                color: white;
                padding: 5px;
                font-size: 14px;
            }
            QComboBox::drop-down {
                background-color: black;
                border: none;
                color: white;
            }
        """)

        self.url_label = QLabel('YouTube Linki:')
        self.url_input = QLineEdit()

        self.start_label = QLabel('Başlangıç Zamanı (saat:dakika:saniye):')
        self.start_input = QLineEdit()

        self.end_label = QLabel('Bitiş Zamanı (saat:dakika:saniye):')
        self.end_input = QLineEdit()

        self.resolution_label = QLabel('Video Çözünürlüğü:')
        self.resolution_combo = QComboBox()
        self.resolution_combo.addItems(['144p', '360p', '480p', '720p', '1080p', '1440p', '2160p'])

        self.download_button = QPushButton('Videoyu İndir ve Kes')
        self.download_button.clicked.connect(self.download_video)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.start_label)
        layout.addWidget(self.start_input)
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_input)
        layout.addWidget(self.resolution_label)
        layout.addWidget(self.resolution_combo)
        layout.addWidget(self.download_button)

        self.setLayout(layout)

    def download_video(self):
        youtube_url = self.url_input.text()
        start_time = self.start_input.text()
        end_time = self.end_input.text()
        resolution = self.resolution_combo.currentText()

        # Video indirme ve kesme işlemleri
        download_and_cut_video(youtube_url, start_time, end_time, resolution)


def download_and_cut_video(youtube_url, start_time, end_time, resolution):
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': 'downloaded_video.%(ext)s',
        'merge_output_format': 'mp4',
        'ffmpeg_location': r'C:\ffmpeg-master-latest-win64-gpl\bin',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    if os.path.exists("downloaded_video.mp4"):
        print("Video başarıyla indirildi.")
    else:
        print("Video indirilemedi.")
        return

    start_seconds = convert_to_seconds(start_time)
    end_seconds = convert_to_seconds(end_time)

    try:
        print("Kesme işlemi başlatılıyor...")
        video = VideoFileClip("downloaded_video.mp4").subclip(start_seconds, end_seconds)
        output_filename = f"cut_video_{resolution}.mp4"
        video.write_videofile(output_filename, codec="libx264", audio_codec="aac")
        if os.path.exists(output_filename):
            print("Video başarıyla kesildi.")
        else:
            print("Kesme işlemi başarısız oldu.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


def convert_to_seconds(time_str):
    time_parts = [int(part) for part in time_str.split(':')]
    if len(time_parts) == 3:
        return time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2]
    elif len(time_parts) == 2:
        return time_parts[0] * 60 + time_parts[1]
    elif len(time_parts) == 1:
        return time_parts[0]
    return 0


def main():
    app = QApplication(sys.argv)
    window = YoutubeDownloader()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
