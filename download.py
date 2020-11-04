from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=-tJYN-eG1zk')

print(yt.streams)
print(dir(yt))