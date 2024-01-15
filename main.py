from tkinter import *
import pygame
import os
import time

root = Tk()
root.title("Music Player")
root.geometry("300x480")
root.configure(bg='green')

pygame.mixer.init()

def playy():
    song = songlist.get(ACTIVE)
    song = f'/Users/azwarshafi/Library/CloudStorage/OneDrive-Personal/Desktop/Python_/Projects/Music app/music/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

global paused
paused = False

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False

    else:
        pygame.mixer.music.pause()
        paused = True

def next():
    next_one = songlist.curselection()
    next_one = next_one[0] + 1
    song = songlist.get(next_one)
    song = f'/Users/azwarshafi/Library/CloudStorage/OneDrive-Personal/Desktop/Python_/Projects/Music app/music/{song}'
     

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    songlist.selection_clear(0, END)
    songlist.activate(next_one)
    songlist.selection_set(next_one, last=None)

def back():
    previous_one = songlist.curselection()
    previous_one = previous_one[0] - 1
    song = songlist.get(previous_one)
    song = f'/Users/azwarshafi/Library/CloudStorage/OneDrive-Personal/Desktop/Python_/Projects/Music app/music/{song}'
     

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    songlist.selection_clear(0, END)
    songlist.activate(previous_one)
    songlist.selection_set(previous_one, last=None)

def update_volume(val):
    volume = int(val) / 10
    pygame.mixer.music.set_volume(volume)

songlist = Listbox(root, bg="gray", fg= "white", width= 30, height= 7,font='Helvetica 29 bold', justify='center')
songlist.pack(fill='both',padx=5,pady=10)

path = '/Users/azwarshafi/Library/CloudStorage/OneDrive-Personal/Desktop/Python_/Projects/Music app/music'

for list in os.listdir(path):
    songlist.insert('end',list)

volume_bar = Scale(root, from_=1, to=10,orient='horizontal',length=250, command=update_volume)
volume_bar.set(3)
volume_bar.pack(pady=15)

backk = Button(root, text= '<<', height=3, width=3, font=('Helvetica',14,'bold'), command=back,)
pausee = Button(root, text='I I', height=3, width=3,font=('Helvetica',14,'bold'), command=lambda: pause(paused))
play = Button(root, text='I>', height=3, width=3,font=('Helvetica',14,'bold'), command=playy)
nextt = Button(root, text='>>', height=3, width=3,font=('Helvetica',14,'bold'), command=next)
backk.pack(padx=12, side=LEFT)
pausee.pack(padx=5,side=LEFT)
play.pack(padx=5,side=LEFT)
nextt.pack(padx=5, side=LEFT)

root.mainloop()
