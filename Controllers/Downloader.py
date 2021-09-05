from pytube import YouTube

class Downloader:
    video = None
    size = 0
    window = None

    def __init__(self, link, window):
        self.video = YouTube(link, on_progress_callback=self.get_progress)
        self.window = window

    def getVideoInfo(self):
        return self.video

    def setSizeInBytes(self, file):
        self.size = file.filesize

    def getTypes(self):
        return self.video.streams

    def download(self, _type):
        file = None
        
        if _type == 'music':
            file = self.video.streams.filter(only_audio=True, file_extension='mp4').first()
        elif _type == 'video':
            file = self.video.streams.filter(progressive=True, file_extension='mp4').first()

        self.setSizeInBytes(file)
        file.download()

    def get_progress(self, stream, chunk, bytes_remaining):
        self.window.progressBar.setValue(round(100 - ((bytes_remaining/self.size)*100)))