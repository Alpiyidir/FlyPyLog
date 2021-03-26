# Imports
from tkinter import *
from tkinter import messagebox
import os
import shutil

# Window Setup
def createWindowForBook(nameOfBook):
    dark2 = "#103B82"
    dark1 = "#2B5384"
    med = "#5E9CCB"
    light2 = "#7DC6EB"
    light1 = "#EBDFD8"
    textForUi = "FlyPyLog - " + nameOfBook
    windowName = nameOfBook + "Window"
    windowName = Tk()
    windowName.title("FlyPyLog")
    windowName.geometry("400x500")
    windowName.configure(bg="white")
    windowName.resizable(False, False)

    # Color Change on Hover
    Can = Canvas(windowName, bg=light2, borderwidth=0, height=43.5, width=200000, highlightthickness=0)
    Can.place(x=0, y=0)

    Logo = Label(windowName, font=("Arial", 18, "bold"), text=textForUi, bg=light2, fg=dark2)
    Logo.place(x=10, y=5)

    # Ye 2nd Mighty Listbox
    BooksBox = Listbox(windowName, font=("Arial", 12, "bold"), bg="light gray", bd=0, height=15, width=20, selectbackground=light2)
    BooksBox.place(x=40, y=90)
    BooksBox.yview()

    View = Button(windowName, font=("Arial", 12), text='View', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=10, height=1)
    View.place(x=240, y=90)

    Edit = Button(windowName, font=("Arial", 12), text='Edit', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=10, height=1)
    Edit.place(x=240, y=120)

    NewLog = Button(windowName, font=("Arial", 12), text='New Log', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=10, height=1)
    NewLog.place(x=240, y=150)

    Del = Button(windowName, font=("Arial", 12), text='Delete', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=10, height=1)
    Del.place(x=240, y=180)
