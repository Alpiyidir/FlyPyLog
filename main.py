# Imports
from tkinter import *

# Window Setup
darkest = "103B82"

root = Tk()
root.title("FlyPyLog")
root.geometry("1000x700")
root.configure(bg='white')
root.resizable(False, False)

def on_enterF(e):
    FileB['background'] = 'orange red'
def on_leaveF(e):
    FileB['background'] = 'orange'

def on_enterD(e):
    Del['background'] = 'orange red'
def on_leaveD(e):
    Del['background'] = 'orange'

def on_enterN(e):
    NB['background'] = 'orange red'
def on_leaveN(e):
    NB['background'] = 'orange'


FileB = Button(root, font=("Arial", 12), text='Files', highlightthickness=0, bg='orange', fg='white', borderwidth=0, width=15, height=2)
FileB.place(x=0, y=0)
FileB.bind("<Enter>", on_enterF)
FileB.bind("<Leave>", on_leaveF)

Del = Button(root, font=("Arial", 12), text='Delete', highlightthickness=0, bg='orange', fg='white', borderwidth=0, width=15, height=2)
Del.place(x=140, y=0)
Del.bind("<Enter>", on_enterD)
Del.bind("<Leave>", on_leaveD)

NB = Button(root, font=("Arial", 12), text='New Book', highlightthickness=0, bg='orange', fg='white', borderwidth=0, width=15, height=2)
NB.place(x=280, y=0)
NB.bind("<Enter>", on_enterN)
NB.bind("<Leave>", on_leaveN)

Can1 = Canvas(bg="orange", borderwidth=0,  height=43.5, width=200000, highlightthickness=0)
Can1.place(x=420, y=0)

Logo = Label(root, font=("Arial", 18, "bold"), text="FlyPyLog", bg="orange")
Logo.place(x=800, y=5)

root.mainloop()