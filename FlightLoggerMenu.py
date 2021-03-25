# Imports
from tkinter import *
from tkinter import messagebox
import os
import shutil

# Window Setup
dark2 = "#103B82"
dark1 = "#2B5384"
med = "#5E9CCB"
light2 = "#7DC6EB"
light1 = "#EBDFD8"

root = Tk()
root.title("FlyPyLog")
root.geometry("400x500")
root.configure(bg="white")
root.resizable(False, False)

# Color Change on Hover
def on_enterV(e):
    View['background'] = med
def on_leaveV(e):
    View['background'] = dark2

def on_enterE(e):
    Edit['background'] = med
def on_leaveE(e):
    Edit['background'] = dark2

def on_enterN(e):
    NewLog['background'] = med
def on_leaveN(e):
    NewLog['background'] = dark2

def on_enterD(e):
    Del2['background'] = med
def on_leaveD(e):
    Del2['background'] = dark2

Can2 = Canvas(bg=light2, borderwidth=0, height=43.5, width=200000, highlightthickness=0)
Can2.place(x=0, y=0)

Logo2 = Label(root, font=("Arial", 18, "bold"), text="FlyPyLog", bg=light2, fg=dark2)
Logo2.place(x=10, y=5)

# Ye 2nd Mighty Listbox
BooksBox2 = Listbox(root, font=("Arial", 12, "bold"), bg="light gray", bd=0, height=15, width=20, selectbackground=light2)
BooksBox2.place(x=40, y=90)
BooksBox2.yview()

View = Button(root, font=("Arial", 12), text='View', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=10, height=1)
View.place(x=240, y=90)
View.bind("<Enter>", on_enterV)
View.bind("<Leave>", on_leaveV)

Edit = Button(root, font=("Arial", 12), text='Edit', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=10, height=1)
Edit.place(x=240, y=120)
Edit.bind("<Enter>", on_enterE)
Edit.bind("<Leave>", on_leaveE)

NewLog = Button(root, font=("Arial", 12), text='New Log', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=10, height=1)
NewLog.place(x=240, y=150)
NewLog.bind("<Enter>", on_enterN)
NewLog.bind("<Leave>", on_leaveN)

Del2 = Button(root, font=("Arial", 12), text='Delete', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=10, height=1)
Del2.place(x=240, y=180)
Del2.bind("<Enter>", on_enterD)
Del2.bind("<Leave>", on_leaveD)

root.mainloop()