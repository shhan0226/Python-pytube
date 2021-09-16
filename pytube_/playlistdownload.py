from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLRrUisvYoUw9-cTYgkbTbr9f9CpbGdq4F')

print(f'Downloading: {p.title}')


for video in p.videos:
    #video.streams.first().download('/mnt/share')
    #print(video.streams.filter(progressive=True, file_extension="mp4", type="video"))
    print(video.streams.get_by_itag(22).title)
    video.streams.get_by_itag(22).download('/mnt/share')

