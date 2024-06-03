from msilib.schema import ListBox
import socket
from tkinter import *
from threading import Thread
from tkinter import ttk
from tkinter import filedialog
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path
from playsound import playsound
import pygame
from pygame import mixer
import os
import time
from ftplib import FTP


IP_ADDRESS = '127.0.0.1'
PORT = 8000
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox = None
filePathLabel = None
global song_counter
song_counter = 0
infoLabel = None





def play():
    global song_seleted
    global infoLabel
    song_selected = listbox.get(ANCHOR)
    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.play()
    if (song_selected != ""):
        infoLabel.configure(text = 'Now Playing: ' + song_selected)
    else:
        infoLabel.configure(text = "")
    
def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.pause()
    infoLabel.configure(text = "")
    
def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.play()
    
def pause():
    global song_selected   
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.pause()
    
def browseFiles():
    global listbox
    global song_counter
    global filePathLabel
    try:
        filename = filedialog.askopenfile()
        HOSTNAME = '127.0.0.1'
        USERNAME = 'lftpd'
        PASSWORD = 'lftpd'
        ftp_server = FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = 'utf-8'
        ftp_server.cwd('shared_files')
        fname = ntpath.basename(filename)
        with open(filename, 'rb') as file:
            ftp_server.storbinary(f"STOR {fname}", file)
        
        ftp_server.dir()
        ftp_server.quit()
    except FileNotFoundError:
        print('Cancel Button Pressed')


def musicWindow():
    window = Tk()
    window.title('Music Window')
    window.geometry('300x350')
    window.configure(bg = 'LightSkyBlue')
    
    selectLabel = Label(window, text = 'Select Song', bg = 'LightSkyBlue', font = ("Calibri", 8))
    selectLabel.place(x = 2, y = 1)
    
    listBox = Listbox(window, height = 10, width = 39, activestyle = 'dotbox', bg = 'LightSkyBlue', 
                      borderwidth = 2, font = ("Calibri", 10))
    listBox.place(x = 10, y = 10)
    
    scrollBar1 = Scrollbar(listBox)
    scrollBar1.place(relheight = 1, relx = 1)
    scrollBar1.config(command = listBox.yview)
    
    playButton = Button(window, text = 'Play', width = 10, bd = 1, bg = 'SkyBlue', font = ("Calibri", 10),
                        command = play)
    playButton.place(x = 30, y = 200)
    
    stopButton = Button(window, text = 'Stop', width = 10, bd = 1, bg = 'SkyBlue', font = ("Calibri", 10),
                  command = stop)
    stopButton.place(x = 200, y = 200)
    
    uploadButton = Button(window, text = 'Upload', width = 10, bd = 1, bg = 'SkyBlue', font = ("Calibri", 10), 
                    command = browseFiles)
    uploadButton.place(x = 30, y = 250)
    
    download = Button(window, text = 'Download', bd = 1, width = 10, bg = 'SkyBlue', font = ("Calibri", 10))
    download.place(x = 200, y = 250)
    
    infoLabel = Label(window, text = "", fg = 'blue', font = ("Calibri", 8))
    infoLabel.place(x = 4, y = 200)
    
    resumeButton = Button(window, text = 'RESUME', width = 10, bd = 1, bg = 'SkyBlue', font = ("Calibri", 10),
                          command = resume)
    resumeButton.place(x = 30, y = 250)
    
    pauseButton = Button(window, text = 'Pause', width = 10, bd = 1, bg = 'SkyBlue', font = ("Calibri", 10),
                         command = pause)
    pauseButton.place(x = 200, y = 250)
    
    window.mainloop()
    
    

    

    
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    
    musicWindow()
    
setup()