import os
from pytube import YouTube

#youtube download
url_ = input('url:')
yt = YouTube(url_)
print(yt.title)
#for i, stream in enumerate(yt.streams.filter(progressive=True, file_extension="mp4", type="video").all()):
#		print(i, " : ", stream)
for i, stream in enumerate(yt.streams.all()):
    print(i, " : ", stream)
                
num = input("itag:")
yt.streams.get_by_itag(num).download('/data/Youtube/haru/')
