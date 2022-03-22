import os
from pytube import YouTube
from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLQNlK4RYJxm8u3_aZ5ZyYsvfjnHLVpfRN')
print(f'Downloading: {p.title}')

for video in p.video_urls:
	yt = YouTube(video)
	print(yt.title)
#	for i, stream in enumerate(yt.streams.all()):
#		print(i, " : ", stream)
	for i, stream in enumerate(yt.streams.filter(progressive=True, file_extension="mp4", type="video").all()):
		print(i, " : ", stream)
	yt.streams.get_by_itag(22).download('/data')
