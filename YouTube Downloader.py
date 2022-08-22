from email import message
from tkinter import *
import sys
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube

def path_function():
    path_ask=filedialog.askdirectory(initialdir="C://")
    paths.set(path_ask)
def downloader():
    url=input_url.get()
    path=path_entry.get()
    Video=YouTube(url)
    stream=Video.streams.first()
    stream.download(path)
    messagebox.showinfo(message=f"SUCESSFULLY DOWNLOADED IN "{path})
try:
    root=Tk()
    root.geometry("500x500")
    paths=StringVar()
    heading=Label(root,text="YouTube Downloader",bg="green",fg="white").grid(padx=180,pady=5,ipadx=10,ipady=10)
    url_label=Label(root,text="Enter Video Link:",bg="blue",fg="white").grid(padx=0,column=0)
    input_url=Entry(root)
    input_url.grid()
    path_label=Label(root,text="File Path",bg="blue",fg="white")
    path_label.grid()
    path_entry=Entry(root,textvariable=paths)
    path_entry.grid()
    path_button=Button(root,text="Browse",command=path_function,bg="red",fg="white")
    path_button.grid()
    download_button=Button(root,text="Download",command=downloader,bg="red",fg="white").grid()
    root.mainloop()
except KeyboardInterrupt:
 	sys.exit()