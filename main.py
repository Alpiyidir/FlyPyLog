# Imports
from tkinter import *
from tkinter import messagebox
import os
import shutil
import sys

# Window Setup
dark2 = "#103B82"
dark1 = "#2B5384"
med = "#5E9CCB"
light2 = "#7DC6EB"
light1 = "#EBDFD8"

root = Tk()
root.title("FlyPyLog")
root.geometry("1000x500")
root.configure(bg="white")
root.resizable(False, False)

books = []

def Delete():
    selecind = BooksBox.curselection()
    fselec = list(selecind)[0]
    print(fselec)
    delYN = messagebox.askyesno(title="Delete", message="Do you wish to proceed with the deletion?")
    print(delYN)
    if delYN == True:
        toDel = BooksBox.get(selecind)
        print(toDel)
        delet = str(os.path.abspath(os.getcwd())) + "/Books/" + str(toDel)
        shutil.rmtree(delet)
        BooksBox.delete(fselec, last=None)
    listBoxer()

def listBoxer():
    books.clear()
    BooksBox.delete(0, "end")
    base = str(os.path.abspath(os.getcwd())) + "/Books"
    for entry in os.listdir(base):
        if os.path.isdir(os.path.join(base, entry)):
            books.append(entry)
    BooksBox.insert(END, *books)

def addBook():
    name = bNameEntry.get()
    base = str(os.path.abspath(os.getcwd())) + "/Books/"
    os.mkdir(base + str(name))
    BooksBox.insert("end", name)

def on_enterF(e):
    FileB['background'] = med
def on_leaveF(e):
    FileB['background'] = dark2


def on_enterD(e):
    Del['background'] = med
def on_leaveD(e):
    Del['background'] = dark2


def on_enterN(e):
    NB['background'] = med
def on_leaveN(e):
    NB['background'] = dark2




BooksBox = Listbox(root, font=("Arial", 12, "bold"), bg="light gray", bd=0, height=15, width=80, selectbackground=light2)
BooksBox.place(x=70, y=90)

listBoxer()

FileB = Button(root, font=("Arial", 12), text='Files', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=15, height=2)
FileB.place(x=0, y=0)
FileB.bind("<Enter>", on_enterF)
FileB.bind("<Leave>", on_leaveF)

Del = Button(root, font=("Arial", 12), text='Delete', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=15, height=2, command=Delete)
Del.place(x=140, y=0)
Del.bind("<Enter>", on_enterD)
Del.bind("<Leave>", on_leaveD)

NB = Button(root, font=("Arial", 12), text='New Book', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=15, height=2, command=addBook)
NB.place(x=280, y=0)
NB.bind("<Enter>", on_enterN)
NB.bind("<Leave>", on_leaveN)

Can1 = Canvas(bg=light2, borderwidth=0, height=43.5, width=200000, highlightthickness=0)
Can1.place(x=420, y=0)

Logo = Label(root, font=("Arial", 18, "bold"), text="FlyPyLog", bg=light2, fg=dark2)
Logo.place(x=800, y=5)

lBoxLabel = Label(root, font=("Arial", 12, "bold"), text="My Books", bg="white", fg=dark2)
lBoxLabel.place(x=75, y=60)

# Book Name Entry
bNameLabel = Label(root, font=("Arial", 10, "bold"), text="Name of new book?", bg=light2, fg=dark2)
bNameLabel.place(x=430, y=0)

bNameEntry = Entry(root, font=("Arial", 10, "bold"), bg="white", fg="black")
bNameEntry.place(x=430, y=23)

root.mainloop()