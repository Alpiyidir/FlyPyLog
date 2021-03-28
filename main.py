# Imports
from tkinter import *
from tkinter import messagebox
import os
import shutil
import FlightLoggerMenu

# Window Setup
dark2 = "#103B82"
dark1 = "#2B5384"
med = "#5E9CCB"
light2 = "#7DC6EB"
light1 = "#EBDFD8"

root = Tk()
root.title("FlyPyLog-Main Menu")
root.geometry("800x500")
root.configure(bg="white")
root.resizable(False, False)


if os.path.isdir(os.getcwd() + "\Books") != True:
    os.mkdir("Books")
    print("Created \Books directory (first run or it was manually deleted)")

def addBook():
    name = bNameEntry.get()
    base = str(os.path.abspath(os.getcwd())) + "/Books/"
    try:
        os.mkdir(base + str(name))
    except WindowsError:
        print("Couldn't create book, file already exists or no name was specified.")
        messagebox.showerror(title="lol no",
                             message="Couldn't create book, book already exists or no name was specified.")
        return
    BooksBox.insert("end", name)
    bNameEntry.delete(0,"end")

def Delete():
    selecind = BooksBox.curselection()
    try:
        fselec = list(selecind)[0]
    except IndexError:
        print("No item selected to delete. IndexError")
        messagebox.showerror(title="lol no", message="No item selected to delete. IndexError")
        return

    delYN = messagebox.askyesno(title="Delete", message="Do you wish to proceed with the deletion?")
    if delYN == True:
        toDel = BooksBox.get(selecind)
        print(toDel + " deleted.")
        delet = str(os.path.abspath(os.getcwd())) + "/Books/" + str(toDel)
        shutil.rmtree(delet)
        BooksBox.delete(fselec, last=None)


def OpenFilePath():
    base = str(os.path.abspath(os.getcwd()))
    os.startfile(base)

def OpenFlightLogger():
    try:
        BooksBoxIndex = BooksBox.curselection()[0]
    except IndexError:
        print("No book selected to open flight logger for. IndexError")
        messagebox.showerror(title="lol no", message="No book selected to open in Flight Logger.")
        return

    nameOfBook = BooksBox.get(BooksBoxIndex)

    FlightLoggerMenu.createWindowForBook(nameOfBook)




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
BooksBox = Listbox(root, font=("Arial", 12, "bold"), activestyle="none", bg="light gray", bd=0, height=15, width=50,
                   selectbackground=light2)
BooksBox.place(x=70, y=90)
BooksBox.yview()

# Listbox File Checking on Start
def fileChecking():
    books = []
    books.clear()
    selectedIndex = BooksBox.curselection()
    BooksBox.delete(0, "end")
    base = str(os.path.abspath(os.getcwd())) + "/Books"
    for entry in os.listdir(base):
        books.append(entry)
    BooksBox.insert(END, *books)


    selectedIndexExists = True
    try:
        selectedIndex[0]
    except:
        selectedIndexExists = False

    if selectedIndexExists:
        BooksBox.select_set(selectedIndex)

    root.after(1,fileChecking)

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

Can = Canvas(root, bg=light2, borderwidth=0, height=43.5, width=200000, highlightthickness=0)
Can.place(x=420, y=0)

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
              borderwidth=0, width=20, height=1, command=OpenFlightLogger)
Open.place(x=70, y=400)
Open.bind("<Enter>", on_enterO)
Open.bind("<Leave>", on_leaveO)

root.after(0,fileChecking)
root.mainloop()
