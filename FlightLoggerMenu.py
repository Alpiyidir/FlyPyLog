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
root.geometry("350x500")
root.configure(bg="white")
root.resizable(False, False)

Can1 = Canvas(bg=light2, borderwidth=0, height=43.5, width=200000, highlightthickness=0)
Can1.place(x=0, y=0)

root.mainloop()
