from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
#pip install pytube3 withot this we get some error

Folder_Name = ""

#file location to download
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload youtube video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root = Tk()
root.title("YouTube Downloader")
root.geometry("3500x4000") #set window
root.columnconfigure(0,weight=100)#set all content in center.



#Ytd Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",font=("jost",40))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=100,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytdError = Label(root,text="Error",fg="red",font=("jost",10))
ytdError.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",fg ="blue",font=("jost",40,"bold"))
saveLabel.grid()

#button of save file
saveEntry = Button(root,width=40,bg="orange",fg="black",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error Message location
locationError = Label(root,text="Error Message of Path",fg="red",font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",fg="Green",font=("jost",40))
ytdQuality.grid()

#combobox
choices = ["720p","144p","360p","mp3"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#donwload button
downloadbtn = Button(root,text="Donwload",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

#developer Label
developerlabel = Label(root,text="Guddu",font=("jost",15))
developerlabel.grid()

root.mainloop()
