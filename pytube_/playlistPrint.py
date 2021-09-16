from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLRrUisvYoUw9-cTYgkbTbr9f9CpbGdq4F')

print(f'Downloading: {p.title}')


for url in p.video_urls:
    print(url)


#for video in p.videos:
#    video.streams.first().download()

