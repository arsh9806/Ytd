import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from tkinter import filedialog
from PIL import Image,ImageTk
import threading
import os
window = tk.Tk()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#print(BASE_DIR)
window.iconbitmap(os.path.join(BASE_DIR,"ytdIcon.ico"))
window.title("Youtube Video Downloader")
window.geometry("900x500")
#Image Setting !!
path = os.path.join(BASE_DIR,"ytd.jpg")
img = Image.open(path)
image = img.resize((700, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
label = tk.Label(window,image=img)
label.place(x=100,y=0)
#Image setting


def browseDir():
    feedback = filedialog.askdirectory()
    entryPath.delete(0, "end")
    entryPath.insert(0, feedback)
def DownloadAudio():
    link = entrylink.get()
    video = YouTube(link)
    AudioStreams = video.streams.filter(only_audio=True).all()
    lisAudio = [(i+1,"-",stream.mime_type,"Bit Rate-", stream.abr) for i,stream in enumerate(video.streams.filter(only_audio=True).all())]
    print(AudioStreams)

    AudioWindow = tk.Tk()
    def startDownloadAudio():                    #called when start download clicked after selecting quality
        messagebox.showinfo("started", "Download started!")
        activea = lisboxAudio.get("active")
        print(activea)
        AudioStreams[activea[0] - 1].download(entryPath.get())
        messagebox.showinfo("Done", "Finished Downloading")
    AudioWindow.title("Select Video Quality")
    AudioWindow.geometry("400x400")
    lisboxAudio = tk.Listbox(AudioWindow, width=40)  # listbox for audio
    lisboxAudio.pack()
    for i in lisAudio:
        lisboxAudio.insert("end",i)
    buttona = tk.Button(AudioWindow, text="Start Download", command=startDownloadAudio)  # audio download button
    buttona.pack()
    AudioWindow.mainloop()

def DownloadVideo():
    link = entrylink.get()
    video = YouTube(link)
    streams = video.streams.filter(progressive=True).order_by('resolution').desc().all()
    lis = [(i+1,"-", stream.resolution,"-" ,stream.mime_type,"-", stream.fps,"fps") for i,stream in enumerate(video.streams.filter(progressive=True).order_by('resolution').desc().all())]
    #new window opens for selecting quality
    VideoWindow = tk.Tk()

    def startDownloadVideo(): #called when start download clicked after selecting quality
        activev = lisbox.get("active")
        print(activev)
        streams[activev[0] - 1].download(entryPath.get())
        messagebox.showinfo("Done", "Finished Downloading")


    #new window specs
    VideoWindow.title("Select Video Quality")
    VideoWindow.geometry("400x400")
    lisbox = tk.Listbox(VideoWindow,width=40) #listbox for video
    lisbox.pack()
    for i in lis:
        lisbox.insert("end",i)
    buttonv = tk.Button(VideoWindow, text = "Start Download",command=startDownloadVideo)#video download button
    buttonv.pack()
    VideoWindow.mainloop()


labellink = tk.Label(window,text="Enter Url : ")
labellink.place(x=150,y=210)
entrylink = tk.Entry(window, width=80)
entrylink.place(x=210,y=210)
labelPath = tk.Label(window,text="Download Location : ")
labelPath.place(x=150,y=240)
entryPath = tk.Entry(window,width = 70)
entryPath.insert(0,"C:/Users/Arsh/Downloads")
entryPath.place(x=270,y=240)
browseButton = tk.Button(window, text="Browse",width=20,command=browseDir)
browseButton.place(relx=0.79,y=240)
downVideoButton = tk.Button(window,text="Download Video",width=30,command=DownloadVideo)
downVideoButton.place(relx = 0.3, rely = 0.56, anchor = "center")
downAudioButton = tk.Button(window,text="Download Audio",width=30,command=DownloadAudio)
downAudioButton.place(relx = 0.6, rely = 0.56, anchor = "center")






#The Pack geometry manager packs widgets in rows or columns.
window.mainloop()
