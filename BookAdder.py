# Imports
from tkinter import *
import os

dark2 = "#103B82"
dark1 = "#2B5384"
med = "#5E9CCB"
light2 = "#7DC6EB"
light1 = "#EBDFD8"

root = Tk()
root.title("FlyPyLog-Add Book")
root.geometry("300x150")
root.configure(bg="white")
root.resizable(False, False)

#Functions
def on_enter(e):
    createB['background'] = med
def on_leave(e):
    createB['background'] = dark2

def create():
    name = bNameEntry.get()
    base = str(os.path.abspath(os.getcwd())) + "/Books/"
    os.mkdir(base+str(name))
    main.listBoxer()
    return name

# Top Canvas and Program Name
topCan = Canvas(root, height=43.5, width=3000, bg=light2, borderwidth=0, highlightthickness=0)
topCan.place(x=0, y=0)

Logo = Label(root, font=("Arial", 18, "bold"), text="FlyPyLog", bg=light2, fg=dark2)
Logo.place(x=170, y=5)

# Book Name Entry
bNameLabel = Label(root, font=("Arial", 12, "bold"), text="Name of new book?", bg="white", fg=dark2)
bNameLabel.place(x=10, y=60)

bNameEntry = Entry(root, font=("Arial", 12, "bold"), bg="white", fg="black")
bNameEntry.place(x=10, y=85)

# Book Create Button
createB = Button(root, font=("Arial", 12), text='Create Book', highlightthickness=0, bg=dark2, fg='white', borderwidth=0, command=create)
createB.place(x=10, y=110)
createB.bind("<Enter>", on_enter)
createB.bind("<Leave>", on_leave)

root.mainloop()