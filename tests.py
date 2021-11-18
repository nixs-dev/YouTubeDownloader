from Controllers.Downloader import Downloader

d = Downloader('https://www.youtube.com/watch?v=u-VMMQA-d00', '')
print(d.get_video_info().thumbnail_url)