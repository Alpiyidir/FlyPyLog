# Imports
import tkinter
from tkinter import *
import tkinter.scrolledtext as tkscrolled
from tkinter import messagebox
import os
import shutil
import FlightLoggerMenu

def createInput():
    # Window Setup
    dark2 = "#103B82"
    dark1 = "#2B5384"
    med = "#5E9CCB"
    light2 = "#7DC6EB"
    light1 = "#EBDFD8"

    logName = Tk()
    logName.title("FlyPyLog")
    logName.geometry("800x550")
    logName.configure(bg=light2)
    logName.resizable(False, False)

    def loopdyLoop():
        # Capitalizion checker
        ICAO_1 = depAir.get().upper()
        if len(ICAO_1) > 4:
            ICAO_1 = ICAO_1[:4]
        depAir.delete(0, END)
        depAir.insert(0, ICAO_1)

        ICAO_2 = desAir.get().upper()
        if len(ICAO_2) > 4:
            ICAO_2 = ICAO_2[:4]
        desAir.delete(0, END)
        desAir.insert(0, ICAO_2)


        logName.after(1, loopdyLoop)


    def cancel():
        logName.destroy()
    def save():
        print("this shit at some point will save the log.")

    logLabel = Label(logName, font=("Arial", 12, "bold"), text="Log Name:", bg=light2, fg=dark1)
    logLabel.place(x=45, y=10)

    log = Entry(logName, font=("Arial", 12), highlightthickness=0, borderwidth=0)
    log.place(x=45, y=35)

    depAirLabel = Label(logName, font=("Arial", 12, "bold"), text="Departure Airport ICAO Code:", bg=light2, fg=dark1)
    depAirLabel.place(x=42, y=60)

    depAir = Entry(logName, font=("Arial", 12), highlightthickness=0, borderwidth=0)
    depAir.place(x=45, y=85)

    desAirLabel = Label(logName, font=("Arial", 12, "bold"), text="Destination Airport ICAO Code:", bg=light2, fg=dark1)
    desAirLabel.place(x=42, y=110)

    desAir = Entry(logName, font=("Arial", 12), highlightthickness=0, borderwidth=0)
    desAir.place(x=45, y=135)

    entryLabel = Label(logName, font=("Arial", 12, "bold"), text="Log:", bg=light2, fg=dark1)
    entryLabel.place(x=45, y=160)

    entry = tkscrolled.ScrolledText(logName, width=85, height=18, wrap='word')
    entry.place(x=45, y=185)


    cancel = Button(logName, font=("Arial", 12, "bold"), text="Cancel", bg=light1, fg=dark1, command=cancel)
    cancel.place(x=320,y=500)

    save = Button(logName, font=("Arial", 12, "bold"), text="Save", bg=light1, fg=dark1, command=save)
    save.place(x=430,y=500)


    logName.after(1, loopdyLoop)
    logName.mainloop()
