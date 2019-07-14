import pytube
from urllib.request import Request, urlopen
# req = Request('http://youtube.com/watch?v=bK3lslhN458', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req)
video = pytube.YouTube("https://www.youtube.com/watch?v=07d2dXHYb94&t=73s")
new  = video.streams.all()
new = video.streams.filter(only_audio=True).all()   #to list audio streams
# new = video.streams.filter(subtype='mp4').all()     #to list mp4 files
# new = video.streams.filter(subtype='mp4', progressive=True).all()
# new = video.streams.filter(progressive=True).order_by('resolution').desc().all()
# lis = [(stream.resolution,stream.mime_type, stream.fps) for stream in video.streams.filter(progressive=True).order_by('resolution').all()]
# for (i,j) in zip(new,reversed(lis)):
#     print(i,j)
lis = [(stream.mime_type," Bit-Rate -", stream.abr) for stream in video.streams.filter(only_audio=True).all() ]
for i in lis:
    print(i)
# ToDownoad = new[1]
# ToDownoad.download("E:/")
# new  = video.streams.all()
# for i in new:
#     print(i)
# #
# ToDown = new[15]
# ToDown.download("E:/")
# print("Download Complete!!")
