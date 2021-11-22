from Controllers.Downloader import Downloader

d = Downloader('https://www.youtube.com/watch?v=CBXLc2qAvrU', '')
d.get_video_info()

print(d.video.streams)