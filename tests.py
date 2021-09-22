from Controllers.Downloader import Downloader

d = Downloader('https://www.youtube.com/watch?v=u-VMMQA-d00', '')
print(d.getVideoInfo().thumbnail_url)