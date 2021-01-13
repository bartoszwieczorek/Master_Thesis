from pytube import YouTube

yt = YouTube('www.youtube.com/watch?v=-tJYN-eG1zk')


# print(dir(yt))
# print(yt.vid_info)

# for element in dir(yt):
#     try:
#         if element == 'js':
#                 continue
#         print(element, getattr(yt, element))
#         if 'category' in getattr(yt,element):
#             print(element)
#             break
#     except:
#         pass
#
# print(yt.player_response.)

stream = yt.streams.first()
print(stream)
stream.download('movies/')

