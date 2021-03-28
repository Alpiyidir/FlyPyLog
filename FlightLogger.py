# Imports
from tkinter import *
import tkinter.scrolledtext as tkscrolled
from tkinter import messagebox
from usefulFunctions import getUsefulInfoFromAirportCode, getDistanceBetweenTwoAirports
import json
import os


def createWindow(nameOfBook, typeOfWindow, logToEdit=None):
    # Window Setup
    dark2 = "#103B82"
    dark1 = "#2B5384"
    med = "#5E9CCB"
    light2 = "#7DC6EB"
    light1 = "#EBDFD8"

    inputWindow = Toplevel()
    if typeOfWindow == "add":
        inputWindow.title("FlyPyLog - New Log")
        inputWindow.geometry("800x550")
    elif typeOfWindow == "view":
        inputWindow.title(f"FlyPyLog - Viewing {nameOfBook}")
    elif typeOfWindow == "edit":
        inputWindow.title(f"FlyPyLog - Editing {logToEdit}")
        inputWindow.geometry("800x550")

    inputWindow.configure(bg=light2)
    inputWindow.resizable(False, False)
    inputWindow.grab_set()

    if typeOfWindow == "add":
        def loopdyLoop():
            # Capitalization checker
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

            inputWindow.after(1, loopdyLoop)


    def cancel():
        inputWindow.destroy()

    def save():
        logName = log.get()
        depICAO = depAir.get()
        desICAO = desAir.get()
        logContent = entry.get('1.0', END)

        depICAOlength = len(depICAO)
        desICAOlength = len(desICAO)

        # Checking User Input

        # If logcontent is left empty it will be equal to \n
        if logContent == '\n':
            logContent = None

        if len(logName) == 0:
            messagebox.showerror(title="lol no", message="Please enter a log name.",
                                 parent=inputWindow)
            return

        if typeOfWindow == "add":
            if os.path.isfile(os.getcwd() + f"\Books\{nameOfBook}\{logName}.txt"):
                messagebox.showerror(title="lol no", message="A log with this name already exists.",
                                    parent=inputWindow)
                return

        if (depICAOlength != 0 and depICAOlength < 4 or depICAOlength > 4) and (
                desICAOlength != 0 and desICAOlength < 4 or desICAOlength > 4):
            messagebox.showerror(title="lol no", message="Invalid Departure and Destination ICAO, try again.",
                                 parent=inputWindow)
            return
        elif depICAOlength != 0 and depICAOlength < 4 or depICAOlength > 4:
            messagebox.showerror(title="lol no", message="Invalid Departure ICAO, try again.",
                                 parent=inputWindow)
            return
        elif desICAOlength != 0 and desICAOlength < 4 or desICAOlength > 4:
            messagebox.showerror(title="lol no", message="Invalid Destination ICAO, try again.",
                                 parent=inputWindow)
            return

        if typeOfWindow == "edit":
            os.remove(os.getcwd() + f"\Books\{nameOfBook}\{logName}.txt")


        if depICAOlength == 0:
            depICAOExists = False
        else:
            depICAOExists = True

        if desICAOlength == 0:
            desICAOExists = False
        else:
            desICAOExists = True

        types = ["airportCode", "airportName", "cityName", "countryName", "countryCode", "latitude", "longitude"]

        if depICAOExists:
            try:
                depInfo = getUsefulInfoFromAirportCode(depICAO)
            except IndexError:
                messagebox.showerror(title="lol no",
                                     message="The Departure ICAO doesn't match any of the airports in the database.",
                                     parent=inputWindow)
                return

        depDict = {}
        if depICAOExists:
            for i in range(len(types)):
                depDict[types[i]] = depInfo[types[i]]
        else:
            for i in range(len(types)):
                depDict[types[i]] = None

        if desICAOExists:
            try:
                desInfo = getUsefulInfoFromAirportCode(desICAO)
            except IndexError:
                messagebox.showerror(title="lol no",
                                     message="The Destination ICAO doesn't match any of the airports in the database.",
                                     parent=inputWindow)
                return

        desDict = {}
        if desICAOExists:
            for i in range(len(types)):
                desDict[types[i]] = desInfo[types[i]]
        else:
            for i in range(len(types)):
                desDict[types[i]] = None

        if depICAOExists and desICAOExists:
            distanceTraveled = getDistanceBetweenTwoAirports(depICAO, desICAO)
        else:
            distanceTraveled = None

        info = {"logName": logName, "logContent": logContent, "departure": depDict, "destination": desDict,
                "distanceTraveled": distanceTraveled}

        with open(os.getcwd() + f"\Books\{nameOfBook}\{logName}.txt", "w") as jsonout:
            json.dump(info, jsonout)

        inputWindow.destroy()

    if typeOfWindow == "add":
        logLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Log Name:", bg=light2, fg=dark1)
        logLabel.place(x=42, y=10)

        log = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        log.place(x=45, y=35)

        depAirLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Departure Airport ICAO Code:", bg=light2,
                            fg=dark1)
        depAirLabel.place(x=42, y=60)

        depAir = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        depAir.place(x=45, y=85)

        desAirLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Destination Airport ICAO Code:", bg=light2,
                            fg=dark1)
        desAirLabel.place(x=42, y=110)

        desAir = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        desAir.place(x=45, y=135)

        entryLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Log:", bg=light2, fg=dark1)
        entryLabel.place(x=42, y=160)

        entry = tkscrolled.ScrolledText(inputWindow, width=85, height=18, wrap='word')
        entry.place(x=45, y=185)

        cancel = Button(inputWindow, font=("Arial", 12, "bold"), text="Cancel", bg=light1, fg=dark1, command=cancel)
        cancel.place(x=320, y=500)

        save = Button(inputWindow, font=("Arial", 12, "bold"), text="Save", bg=light1, fg=dark1, command=save)
        save.place(x=430, y=500)

        inputWindow.after(1, loopdyLoop)
    elif typeOfWindow == "edit":
        fileToRead = os.getcwd() + f"\Books\{nameOfBook}\{logToEdit}.txt"

        logLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Log Name:", bg=light2, fg=dark1)
        logLabel.place(x=42, y=10)

        log = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        log.place(x=45, y=35)

        depAirLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Departure Airport ICAO Code:", bg=light2,
                            fg=dark1)
        depAirLabel.place(x=42, y=60)

        depAir = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        depAir.place(x=45, y=85)

        desAirLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Destination Airport ICAO Code:", bg=light2,
                            fg=dark1)
        desAirLabel.place(x=42, y=110)

        desAir = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        desAir.place(x=45, y=135)

        entryLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Log:", bg=light2, fg=dark1)
        entryLabel.place(x=42, y=160)

        entry = tkscrolled.ScrolledText(inputWindow, width=85, height=18, wrap='word')
        entry.place(x=45, y=185)

        cancel = Button(inputWindow, font=("Arial", 12, "bold"), text="Cancel", bg=light1, fg=dark1, command=cancel)
        cancel.place(x=320, y=500)

        save = Button(inputWindow, font=("Arial", 12, "bold"), text="Save", bg=light1, fg=dark1, command=save)
        save.place(x=430, y=500)

    inputWindow.mainloop()
