from pytube import YouTube

p = YouTube('https://')

print(f'Downloading: {p.title}')

p.streams.get_by_itag(22).download('/mnt/share')
