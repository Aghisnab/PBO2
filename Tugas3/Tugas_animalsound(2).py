import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os

player = tkinter.Tk()
player.title("Animal Sound Music Player")
player.geometry("350x385")

var = tkinter.StringVar()
var.set("Pilih Suara Untuk Diputar")

os.chdir(askdirectory())
soundlist = os.listdir()

putar = tkinter.Listbox(player,font="Helvetica 12 bold",width=28,bg="black",fg="white",selectmode=tkinter.SINGLE)

for sound in soundlist:
    putar.insert(0,sound)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(putar.get(tkinter.ACTIVE))
    nama = putar.get(tkinter.ACTIVE)
    var.set(f"{nama[:16]}..." if len(nama)>18 else nama)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

text = tkinter.Label(player,font="Helvetica",textvariable=var).grid(row=0,columnspan=3)
putar.grid(columnspan=3)

play_button = tkinter.Button(player,width=7,height=1,font="Helvetica",text="Play",command=play,bg="lightgreen").grid(row=2,column=0)
pause_button = tkinter.Button(player,width=7,height=1,font="Helvetica",text="Pause",command=pause,bg="lightblue").grid(row=2,column=1)
resume_button = tkinter.Button(player,width=7,height=1,font="Helvetica",text="Resume",command=resume,bg="lightpink").grid(row=2,column=2)

player.mainloop()