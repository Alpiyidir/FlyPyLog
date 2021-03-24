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
root.geometry("1000x500")
root.configure(bg="white")
root.resizable(False, False)

books = []

def Delete():
    selecind = Books.curselection()
    fselec = list(selecind)[0]
    print(selecind)
    delyn = messagebox.askyesno(title="Delete", message="Do you wish to proceed with the deletion?")
    print(delyn)
    if delyn == True:
        toDel = Books.get(selecind)
        print(toDel)
        delet = str(os.path.abspath(os.getcwd())) + "/Books/" + str(toDel[0])
        shutil.rmtree(delet)
        Books.delete(fselec, last=None)
    lBoxer()

def lBoxer():
    books.clear()
    base = str(os.path.abspath(os.getcwd())) + "/Books"
    for entry in os.listdir(base):
        if os.path.isdir(os.path.join(base, entry)):
            books.append(entry)
    Books.insert("end", books)

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


Books = Listbox(root, font=("Arial", 12, "bold"), bg="light gray", bd=0, height=15, width=80, selectbackground=light2)
Books.place(x=70, y=90)

lBoxer()

FileB = Button(root, font=("Arial", 12), text='Files', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=15, height=2)
FileB.place(x=0, y=0)
FileB.bind("<Enter>", on_enterF)
FileB.bind("<Leave>", on_leaveF)

Del = Button(root, font=("Arial", 12), text='Delete', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=15, height=2, command=Delete)
Del.place(x=140, y=0)
Del.bind("<Enter>", on_enterD)
Del.bind("<Leave>", on_leaveD)

NB = Button(root, font=("Arial", 12), text='New Book', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, width=15, height=2)
NB.place(x=280, y=0)
NB.bind("<Enter>", on_enterN)
NB.bind("<Leave>", on_leaveN)

Can1 = Canvas(bg=light2, borderwidth=0, height=43.5, width=200000, highlightthickness=0)
Can1.place(x=420, y=0)

Logo = Label(root, font=("Arial", 18, "bold"), text="FlyPyLog", bg=light2, fg=dark2)
Logo.place(x=800, y=5)

lBoxLabel = Label(root, font=("Arial", 12, "bold"), text="My Books", bg="white", fg=dark2)
lBoxLabel.place(x=75, y=60)
root.mainloop()
