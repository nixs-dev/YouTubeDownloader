from http.client import RemoteDisconnected

from pytube import YouTube
from PyQt5.QtCore import QThread, pyqtSignal
import urllib
import certifi

class Downloader(QThread):
    video = None
    size = 0
    window = None
    _type = ''
    video_data_ready = pyqtSignal(dict)

    def __init__(self, link, window):
        super().__init__()

        self.video = YouTube(link, on_progress_callback=self.get_progress)
        self.window = window

    def run(self):
        self.get_video_info()

    def start_download(self):
        self.window.link.setEnabled(False)
        self.window.search.setEnabled(False)
        self.window.downloadSong.setEnabled(False)
        self.window.downloadVideo.setEnabled(False)
        self.download()

    def get_video_info(self):
        try:
            self.video.check_availability()
            video_info = {
                'title': self.video.title,
                'author': self.video.author,
                'thumbnail': urllib.request.urlopen(self.video.thumbnail_url, cafile=certifi.where()).read()
            }

            self.video_data_ready.emit(video_info)
        except RemoteDisconnected:
            self.video_data_ready.emit({})
        except ConnectionResetError:
            self.video_data_ready.emit({})

    def set_type(self, _type):
        self._type = _type

    def set_size_in_bytes(self, file):
        self.size = file.filesize

    def get_types(self):
        return self.video.streams

    def download(self):
        file = None
        
        if self._type == 'music':
            file = self.video.streams.filter(only_audio=True, file_extension='mp4').first()
        elif self._type == 'video':
            file = self.video.streams.filter(progressive=True, file_extension='mp4').first()

        self.set_size_in_bytes(file)

        file.download()

    def get_progress(self, stream, chunk, bytes_remaining):
        percentage = round(100 - ((bytes_remaining/self.size)*100))

        self.window.progressBar.setValue(percentage)

        if percentage == 100:
            self.window.downloadStatus.setText('Download Finalizado')

            self.window.link.setEnabled(True)
            self.window.search.setEnabled(True)
            self.window.downloadSong.setEnabled(True)
            self.window.downloadVideo.setEnabled(True)