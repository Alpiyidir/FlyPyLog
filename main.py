# Imports
import tkinter
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
root.geometry("800x500")
root.configure(bg="white")
root.resizable(False, False)


class GradientFrame(tkinter.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1="red", color2="black", **kwargs):
        tkinter.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")

def addBook():
    name = bNameEntry.get()
    base = str(os.path.abspath(os.getcwd())) + "/Books/"
    try:
        os.mkdir(base + str(name))
    except WindowsError:
        print("Couldn't create file, file already exists or no name was specified. (root directory)")
        messagebox.showerror(title="lol no", message="Couldn't create file, file already exists or no name was specified. (root directory)")
    BooksBox.insert("end", name)

    originalPath = str(os.path.abspath(os.getcwd())) + "/FlightLoggerMenu.py"
    newPath = base + str(name) + "/FlightLoggerMenu.py"
    shutil.copyfile(originalPath, newPath)


def Delete():
    selecind = BooksBox.curselection()
    try:
        fselec = list(selecind)[0]
    except IndexError:
        return print("No item selected to delete. IndexError")

    print(fselec)
    delYN = messagebox.askyesno(title="Delete", message="Do you wish to proceed with the deletion?")
    print(delYN)
    if delYN == True:
        toDel = BooksBox.get(selecind)
        print(toDel)
        delet = str(os.path.abspath(os.getcwd())) + "/Books/" + str(toDel)
        shutil.rmtree(delet)
        BooksBox.delete(fselec, last=None)


def OpenFilePath():
    base = str(os.path.abspath(os.getcwd()))
    os.startfile(base)


# Color Change on Hover
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


def on_enterO(e):
    Open['background'] = med


def on_leaveO(e):
    Open['background'] = dark2


# Ye Mighty Listbox
BooksBox = Listbox(root, font=("Arial", 12, "bold"), bg="light gray", bd=0, height=15, width=50,
                   selectbackground=light2)
BooksBox.place(x=70, y=90)
BooksBox.yview()

# Listbox File Checking on Start
books = []
books.clear()
BooksBox.delete(0, "end")
base = str(os.path.abspath(os.getcwd())) + "/Books"
for entry in os.listdir(base):
    if os.path.isdir(os.path.join(base, entry)):
        books.append(entry)
BooksBox.insert(END, *books)

# Menu Buttons
FileB = Button(root, font=("Arial", 12), text='Files', highlightthickness=0, bg=dark2, fg='white', borderwidth=0,
               width=15, height=2, command=OpenFilePath)
FileB.place(x=0, y=0)
FileB.bind("<Enter>", on_enterF)
FileB.bind("<Leave>", on_leaveF)

Del = Button(root, font=("Arial", 12), text='Delete', highlightthickness=0, bg=dark2, fg='white', borderwidth=0,
             width=15, height=2, command=Delete)
Del.place(x=140, y=0)
Del.bind("<Enter>", on_enterD)
Del.bind("<Leave>", on_leaveD)

NB = Button(root, font=("Arial", 12), text='New Book', highlightthickness=0, bg=dark2, fg='white', borderwidth=0,
            width=15, height=2, command=addBook)
NB.place(x=280, y=0)
NB.bind("<Enter>", on_enterN)
NB.bind("<Leave>", on_leaveN)

Can1 = Canvas(bg=light2, borderwidth=0, height=43.5, width=200000, highlightthickness=0)
Can1.place(x=420, y=0)

Logo = Label(root, font=("Arial", 18, "bold"), text="FlyPyLog", bg=light2, fg=dark2)
Logo.place(x=600, y=5)

lBoxLabel = Label(root, font=("Arial", 12, "bold"), text="My Books", bg="white", fg=dark2)
lBoxLabel.place(x=75, y=60)

# New Book Name Entry
bNameLabel = Label(root, font=("Arial", 10, "bold"), text="Name of new book?", bg=light2, fg=dark2)
bNameLabel.place(x=430, y=0)

bNameEntry = Entry(root, font=("Arial", 10, "bold"), bg="white", fg="black")
bNameEntry.place(x=430, y=23)

# Opening in Flight Logger
Open = Button(root, font=("Arial", 12), text='Open In Flight Logger', highlightthickness=0, bg=dark2, fg='white',
              borderwidth=0, width=20, height=1)
Open.place(x=70, y=400)
Open.bind("<Enter>", on_enterO)
Open.bind("<Leave>", on_leaveO)

root.mainloop()
