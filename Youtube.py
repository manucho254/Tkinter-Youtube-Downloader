from pytube import YouTube
from tkinter import *
from pytube import Playlist
from tkinter import messagebox

root = Tk()

winicon = PhotoImage(file = 'cool.png')

root.iconphoto(False, winicon)
root.configure(bg='#2B547E')
root.configure(bg='black')

root.title("YOUTUBE DOWNLOADER")
root.geometry('450x400')
root.resizable(width=0, height=0)

label = Label(root,text = "YOUTUBE DOWNLOADER",bg='red',fg='white',
              font = "bold" , width="40", borderwidth=10 ,padx=10, pady=13
              )
label.grid(row=0,columnspan=3, padx=10, pady=10)
label.place(x = 20,
          y = 10)


label1 = Label(root, text = "Download 1 Video",
              font = "bold",
              bg = "black", fg="white",width=30
              )
label1.place(x = 90,
          y = 85)

tube_entry1 = StringVar()
entry1 = Entry(root, width = 45,  
              bd = 6, font = 14, borderwidth=6, textvariable=tube_entry1)
entry1.insert(0,"Youtube Video Link")
entry1.grid(row=1, column=1, columnspan=1, padx=10, pady=13)

entry1.place(x = 10,
          y = 120)

#single download function
def download_single():
    url = entry1.get()
    try:
       YouTube(url).streams.first().download()
       yt = YouTube(url)
       yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
       if yt == True:
           messagebox.showinfo("Download started")
    except:
        messagebox.showerror("Error", "Please insert Url.!!")

button_single = Button(
    root, text="DOWNLOAD" ,
    padx=30, pady=10, 
    bg = 'red', fg='white', command=download_single
    )

button_single.place(x = 150,
          y = 165)

label2 = Label(root, text = "Download Playlist",
              font = "bold",
              bg = "black", fg="white",width=30
              )
label2.place(x = 90,
          y = 217)

tube_entry2 = StringVar()
entry2 = Entry(root, width = 45,  
              bd = 6, font = 14, borderwidth=6, textvariable=tube_entry2)
entry2.insert(0,"Youtube Playlist Link")
entry2.grid(row=2, column=1, columnspan=1, padx=10, pady=13)
entry2.place(x = 10,
          y = 250)

# multi download function
def download_playlist():
    url = entry2.get()
    try:
        pl = Playlist(url)
        for video in pl.videos:
            video.streams.first().download()
    except:
        messagebox.showerror("Error", "Please insert Url.!!")

button_playlist = Button(
    root, text="DOWNLOAD" ,
    padx=30, pady=10, 
    bg = 'red', fg="white", command=download_playlist
    )

button_playlist.place(x = 150,
          y = 300)

# exit function
def button_exit():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        messagebox.showinfo('Return','You will now return to the application screen')
    return

button_exit = Button(
    root, text="EXIT" ,
    padx=30, pady=10,
    bg = 'red', fg="black", command=button_exit
    )

button_exit.place(x = 175,
          y = 350)

root.mainloop()