from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?...')

print(f'Downloading: {p.title}')


for url in p.video_urls:
    print(url)


#for video in p.videos:
#    video.streams.first().download()

