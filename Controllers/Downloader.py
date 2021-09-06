from pytube import YouTube
from PyQt5.QtCore import QThread

class Downloader(QThread):
    video = None
    size = 0
    window = None
    _type = ''

    def __init__(self, link, window):
        super().__init__()

        self.video = YouTube(link, on_progress_callback=self.get_progress)
        self.window = window

    def run(self):
        self.window.link.setEnabled(False)
        self.window.search.setEnabled(False)
        self.window.downloadSong.setEnabled(False)
        self.window.downloadVideo.setEnabled(False)
        self.download()

    def getVideoInfo(self):
        return self.video

    def setType(self, _type):
        self._type = _type

    def setSizeInBytes(self, file):
        self.size = file.filesize

    def getTypes(self):
        return self.video.streams

    def download(self):
        file = None
        
        if self._type == 'music':
            file = self.video.streams.filter(only_audio=True, file_extension='mp4').first()
        elif self._type == 'video':
            file = self.video.streams.filter(progressive=True, file_extension='mp4').first()

        self.setSizeInBytes(file)
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