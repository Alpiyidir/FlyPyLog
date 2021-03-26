# Imports
import tkinter
from tkinter import *
import tkinter.scrolledtext as tkscrolled
from tkinter import messagebox
import os
import shutil
import FlightLoggerMenu

def createInput(logName):

    def capCheck():
        ICAO_1 = depAir.get().upper()
        #ICAO_2 = desAir.get()
        depAir.delete(0, END)
        depAir.insert(0, ICAO_1)


    # Window Setup
    dark2 = "#103B82"
    dark1 = "#2B5384"
    med = "#5E9CCB"
    light2 = "#7DC6EB"
    light1 = "#EBDFD8"

    logName = Tk()
    logName.title("FlyPyLog")
    logName.geometry("800x400")
    logName.configure(bg=light2)
    logName.resizable(False, False)

    v = StringVar()
    w = Entry(logName, width=20, textvariable=v)

    depAirLabel = Label(logName, font=("Arial", 12, "bold"), text="Departure Airport ICAO Code:", bg=light2, fg=dark1)
    depAirLabel.place(x=45, y=35)

    depAir = Entry(logName, font=("Arial", 12), highlightthickness=0, borderwidth=0, textvariable=w)
    depAir.place(x=45, y=60)

    logEntry = tkscrolled.ScrolledText(logName, width=85, height=18, wrap='word')
    logEntry.place(x=45, y=100)



    logName.after(10, capCheck)
    logName.mainloop()

createInput("string")