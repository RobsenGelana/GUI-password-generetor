from cgitb import text
from curses import window
from email.mime import image
from tkinter import *
from turtle import width

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")

canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 102, image=lock_img)
canvas.grid(padx=20, pady=20)






window.mainloop()