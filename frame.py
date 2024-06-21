from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import threading 

myframe =Tk()
myframe.title("Youtube downloader")
myframe.geometry("600x320")
myframe.resizable(False,False)
#-------------------------------------
#my Functions

def browse():
    directory = filedialog.askdirectory (title="Save Video")
    FolderLink.delete(0, "end")
    FolderLink.insert(0, directory)

def down_yt():
    status.config(text="Status: Downloading ...")
    link = ytLink.get()
    folder = FolderLink.get()
    YouTube(link, on_complete_callback=finsh).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(folder)

def finsh(stream=None, chunk=None, file_handle=None, remaining=None):
    status.config(text="Status: Complete")
#-------------------------------------

ytLogo = PhotoImage(file="youtube.png").subsample(2)

ytTitle = Label(myframe , image=ytLogo)
ytTitle.place(relx=0.5 , rely=0.25 , anchor="center")

ytLabel = Label(myframe,text="YouTube Link") 
ytLabel.place(x=25 , y=150)

ytLink = Entry(myframe , width=60)
ytLink.place(x=140 , y=150)

FolderLabel = Label(myframe,text="Download Folder") 
FolderLabel.place(x=25 , y=183)

FolderLink = Entry(myframe , width=50)
FolderLink.place(x=140 , y=183)

browse = Button(myframe, text="browse" , command=browse)
browse.place(x=455 , y=180)

download = Button(myframe , text="Download" , command=threading.Thread(target=down_yt).start)
download.place(x=280 , y=220)

status = Label(myframe, text="Status: Ready", font="Calibre 10 italic", fg="black", bg="white", anchor="w")
status.place(rely=1, anchor="sw", relwidth=1)

myframe.mainloop()