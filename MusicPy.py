#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 00:16:13 2018

@author: yogendraluna
"""

import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image
import mutagen.mp3

root = Tk()
root.minsize(800,500)

listofsongs = []

index = 0
#------------------------------------------------------------------------------
def playsong(event):
    global index
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()


def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()


def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()


def stopsong(event):
    pygame.mixer.music.stop()

def volume(event):
    pygame.mixer.music.set_volume(vol.get())

def double_click(event):
  pos = event.widget.curselection()[0]
  #"Now playing %s" % event.widget.get(pos)
  pygame.mixer.music.load(listofsongs[pos])
  pygame.mixer.music.play()

#------------------------------------------------------------------------------
def directorychooser():
    global index
    directory = askdirectory() #"/home/yogendraluna/Music/"#
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()

#------------------------------------------------------------------------------
directorychooser()

"""Setting Heading of Player"""
label =Label(root,text='MusicPy',width=300)
label.pack()

"""Volume Slider """
vol = Scale(root,orient=VERTICAL,length=100,width=10,sliderlength=10,from_=0,to=1,tickinterval=10,command=volume, resolution = .1, bg="black", fg="white")
vol.pack(side='left')

"""Home Screen of music Player"""

img = ImageTk.PhotoImage(Image.open("/home/yogendra/Music/Icon/Player 3.png"))
panel = Label(root, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")

pics = ImageTk.PhotoImage(Image.open("/home/yogendra/Music/Icon/speaker.png"))
panel = Label(root, image = pics)
panel.pack(side = LEFT, fill = Y, expand = 0)

pic = ImageTk.PhotoImage(Image.open("/home/yogendra/Music/Icon/speaker.png"))
panel = Label(root, image = pic)
panel.pack(side = RIGHT, fill = Y, expand = 0)

"""Creating Scroll-Bar"""
scrollbar = Scrollbar(root, width=10)
scrollbar.pack(side='left',fill=Y)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
#listbox.activate(index)
listbox.pack(side="top",fill=X)
scrollbar.config(command=listbox.yview)

"""Listing Song list menu"""
listofsongs.reverse()
for items in listofsongs:
    listbox.insert(0,items)
listofsongs.reverse()
for i in range(0, len(listofsongs)):
    listbox.itemconfig(i, bg='gray5', fg='white')

"""Creating Buttons """
buttonsFrame = Frame(root)

nextbutton = Button(buttonsFrame,width=6, bg="black", fg="white")
nextbutton["text"] = "Next"
nextbutton.grid(row = 0, column=1)

prevbutton = Button(buttonsFrame,width=6, bg="black", fg="white")
prevbutton["text"] = "Prev"
prevbutton.grid(row = 0, column=3)

stop = Button(buttonsFrame,width=6, bg="black", fg="white")
stop["text"] = "Stop"
stop.grid(row = 0, column=2)

play = Button(buttonsFrame,width=6,bg="black", fg="white")
play["text"] = "Play"
play.grid(row = 0, column=0)
buttonsFrame.pack(side=BOTTOM)


"""Background Color """
root.configure(background='gray25')

"""Connecting to function that we made above
   so that Buttons work """

play.bind("<Button-1>", playsong)
nextbutton.bind("<Button-1>",nextsong)
prevbutton.bind("<Button-1>",prevsong)
stop.bind("<Button-1>",stopsong)
listbox.bind("<Double-Button-1>", double_click) #Selecting using Double click

root.mainloop()
