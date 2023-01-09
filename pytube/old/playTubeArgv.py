from pytube import YouTube
import sys
url_path = sys.argv[1]

if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

p = YouTube(url_path)
print(f'Downloading: {p.title}')

p.streams.get_by_itag(22).download('/mnt/share')
print("end.")
