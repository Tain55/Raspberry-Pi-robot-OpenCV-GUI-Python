import tkinter
from tkinter import font
from tkinter import *
from tkvideo import tkvideo

import call_ambulance
import game

def ambulance():
    call_ambulance.ambulance()

def play_game():
    print(1)
    game.playing()


root = Tk()
width= root.winfo_screenwidth()
height= root.winfo_screenwidth()
root.geometry("%dx%d" % (width,height))

l = Label(root, text = "Hello user!")
l.pack()

#background video
player = tkvideo("G:\Technology Network Loop Background _ Blue Animated lines Backgrounds.mp4",
                 l,
                 loop = 1,
                 size=(width,height-340))
player.play()

#canvas for show text //undone

#showing text
robot_text = Label(root, text = "Hello! I am a robot to deliver medicine timely and do several tasks like "
                                "count your exercise, play game with you and call ambulance. You can also controle"
                                "me by the mobile app named \"Robocop\"."
                                "Enjoy my company.", wraplength = 550)
label_font = font.Font(family="Roboto", size=23)
robot_text.config(fg = "white",bg = "gray", font = label_font)
robot_text.place(x = 100, y= 20)


#button call ambulance
b = Button(root, text = "Call Ambulance",
           background = "red",
           foreground = "white",
           borderwidth = 3,
           width = 20,
           height = 3,
           font = ("Arial", 20, "bold"),
           command = ambulance)
b.place(x= 850, y = 25)

#button exercise counter
e = Button(root, text = "Count Exercise",
           background = "green",
           foreground = "white",
           borderwidth = 3,
           width = 20,
           height = 3,
           font = ("Arial", 20, "bold"))
e.place(x= 850, y = 200)

#button game
g = Button(root, text = "Play Game",
           background = "orange",
           foreground = "white",
           borderwidth = 3,
           width = 20,
           height = 3,
           font = ("Arial", 20, "bold"),
           command = play_game
           )
g.place(x= 850, y = 400)


#button two

root.mainloop()

