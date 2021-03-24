# Imports
from tkinter import *

# Window Setup
dark2 = "#103B82"
dark1 = "#2B5384"
med = "#5E9CCB"
light2 = "#7DC6EB"
light1 = "#EBDFD8"

root = Tk()
root.title("FlyPyLog")
root.geometry("1000x700")
root.configure(bg=light1)
root.resizable(False, False)


def on_enterF(e):
    FileB['background'] = med


def on_leaveF(e):
    FileB['background'] = light2


def on_enterD(e):
    Del['background'] = med


def on_leaveD(e):
    Del['background'] = light2


def on_enterN(e):
    NB['background'] = med


def on_leaveN(e):
    NB['background'] = light2


FileB = Button(root, font=("Arial", 12), text='Files', highlightthickness=0, bg=light2, fg='white', borderwidth=0,
               width=15, height=2)
FileB.place(x=0, y=0)
FileB.bind("<Enter>", on_enterF)
FileB.bind("<Leave>", on_leaveF)

Del = Button(root, font=("Arial", 12), text='Delete', highlightthickness=0, bg=light2, fg='white', borderwidth=0,
             width=15, height=2)
Del.place(x=140, y=0)
Del.bind("<Enter>", on_enterD)
Del.bind("<Leave>", on_leaveD)

NB = Button(root, font=("Arial", 12), text='New Book', highlightthickness=0, bg=light2, fg='white', borderwidth=0,
            width=15, height=2)
NB.place(x=280, y=0)
NB.bind("<Enter>", on_enterN)
NB.bind("<Leave>", on_leaveN)

Can1 = Canvas(bg=light2, borderwidth=0, height=43.5, width=200000, highlightthickness=0)
Can1.place(x=420, y=0)

Logo = Label(root, font=("Arial", 18, "bold"), text="FlyPyLog", bg=light2, fg=dark2)
Logo.place(x=800, y=5)

root.mainloop()
