# Imports
import tkinter
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
root.title("FlyPyLog")
root.geometry("800x500")
root.configure(bg="white")
root.resizable(False, False)