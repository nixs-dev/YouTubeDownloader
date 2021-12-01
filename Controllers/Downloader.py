from http.client import RemoteDisconnected

from pytube import YouTube
from PyQt5.QtCore import QThread, pyqtSignal
import urllib
import certifi


class Downloader(QThread):
    video = None
    stream = None
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
        self.window.song_option.setEnabled(False)
        self.window.video_option.setEnabled(False)
        self.window.download_button.setEnabled(False)
        self.window.file_format.setEnabled(False)
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

    def set_stream(self, stream):
        self.stream = stream

    def set_size_in_bytes(self, file):
        self.size = file.filesize

    def get_streams(self, type_):
        if type_ == 'song':
            streams = self.video.streams.filter(only_audio=True)
        else:
            streams = self.video.streams.filter(progressive=True)

        return streams

    def download(self):
        self.set_size_in_bytes(self.stream)
        self.stream.download()

    def get_progress(self, stream, chunk, bytes_remaining):
        percentage = round(100 - ((bytes_remaining/self.size)*100))

        self.window.progressBar.setValue(percentage)

        if percentage == 100:
            self.window.downloadStatus.setText('Download Finalizado')

            self.window.link.setEnabled(True)
            self.window.search.setEnabled(True)
            self.window.song_option.setEnabled(True)
            self.window.video_option.setEnabled(True)
            self.window.download_button.setEnabled(True)
            self.window.file_format.setEnabled(True)