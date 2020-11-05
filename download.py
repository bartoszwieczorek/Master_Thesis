from pytube import YouTube

yt = YouTube('www.youtube.com/watch?v=-tJYN-eG1zk')

print(yt.streams)
print(dir(yt))