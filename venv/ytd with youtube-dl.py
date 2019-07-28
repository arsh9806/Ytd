
import youtube_dl
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)