import os
from pytube import YouTube


f = open("./list.txt", 'r')
lines = f.readlines()

num_=0
for line in lines:
    url_ = line.strip()
    print(url_)
    num_ = num_ + 1
    #youtube download
    try:
        yt = YouTube(url_)
        print("...")
        print(yt.title)
        for i, stream in enumerate(yt.streams.filter(progressive=True, file_extension="mp4", type="video").all()):
            print(i, " : ", stream)
        if i == 1:
            print("itag:22")
            yt.streams.get_by_itag(22).download(output_path='/data/Youtube/', filename_prefix=str(num_)+'_')
        else:
            print("itag:18")
            yt.streams.get_by_itag(18).download(output_path='/data/Youtube/', filename_prefix=str(num_)+'_')
    except:
        print("<< ERROR.........")

f.close()
