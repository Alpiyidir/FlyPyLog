# Imports
from tkinter import *
import tkinter.scrolledtext as tkscrolled
from tkinter import messagebox
from usefulFunctions import getUsefulInfoFromAirportCode, getDistanceBetweenTwoAirports
import json
import os


def createWindow(nameOfBook, typeOfWindow, logToViewOrEdit=None):
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
        inputWindow.title(f"FlyPyLog - Viewing {logToViewOrEdit}")
        inputWindow.geometry("800x550")
    elif typeOfWindow == "edit":
        inputWindow.title(f"FlyPyLog - Editing {logToViewOrEdit}")
        inputWindow.geometry("800x550")

    inputWindow.configure(bg=light2)
    inputWindow.resizable(False, False)
    inputWindow.grab_set()

    if typeOfWindow == "add" or "edit":
        def capitalizeLoop():
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

            inputWindow.after(1, capitalizeLoop)

    def cancel():
        inputWindow.destroy()

    def save():
        logName = log.get()
        depICAO = depAir.get()
        desICAO = desAir.get()
        logContent = entry.get('1.0', END)
        # Removes the \n from the logContent which gets added to the end every single time it is saved for some reason
        logContent = logContent[:-1]

        depICAOlength = len(depICAO)
        desICAOlength = len(desICAO)

        # Checking User Input

        # If logcontent is left empty it will be equal to \n
        if len(logContent) == 0:
            logContent = None

        if len(logName) == 0:
            messagebox.showerror(title="lol no", message="Please enter a log name.",
                                 parent=inputWindow)
            return

        if typeOfWindow == "add":
            if os.path.isfile(os.getcwd() + f"\Books\{nameOfBook}\{logName}.json"):
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

        # Removes the previous file so that it can be replaced after all errors have been checked
        if typeOfWindow == "edit":
            os.remove(os.getcwd() + f"\Books\{nameOfBook}\{logToViewOrEdit}.json")

        if depICAOExists and desICAOExists:
            distanceTraveled = getDistanceBetweenTwoAirports(depICAO, desICAO)
        else:
            distanceTraveled = None

        info = {"logName": logName, "logContent": logContent, "departure": depDict, "destination": desDict,
                "distanceTraveled": distanceTraveled}

        with open(os.getcwd() + f"\Books\{nameOfBook}\{logName}.json", "w") as jsonout:
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

        entry = tkscrolled.ScrolledText(inputWindow, width=84, height=18, wrap='word')
        entry.place(x=45, y=185)

        cancel = Button(inputWindow, font=("Arial", 12, "bold"), text="Cancel", bg=light1, fg=dark1, command=cancel)
        cancel.place(x=320, y=500)

        save = Button(inputWindow, font=("Arial", 12, "bold"), text="Save", bg=light1, fg=dark1, command=save)
        save.place(x=430, y=500)

        inputWindow.after(1, capitalizeLoop)
    elif typeOfWindow == "edit":
        logLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Log Name:", bg=light2, fg=dark1)
        logLabel.place(x=60.5, y=10)

        log = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        log.place(x=63.5, y=35)

        depAirLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Departure Airport ICAO Code:", bg=light2,
                            fg=dark1)
        depAirLabel.place(x=60.5, y=60)

        depAir = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        depAir.place(x=63.5, y=85)

        desAirLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Destination Airport ICAO Code:", bg=light2,
                            fg=dark1)
        desAirLabel.place(x=60.5, y=110)

        desAir = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        desAir.place(x=63.5, y=135)

        entryLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Log:", bg=light2, fg=dark1)
        entryLabel.place(x=60.5, y=160)

        entry = tkscrolled.ScrolledText(inputWindow, width=84, height=18, wrap='word')
        entry.place(x=63.5, y=185)

        cancel = Button(inputWindow, font=("Arial", 12, "bold"), text="Cancel", bg=light1, fg=dark1, command=cancel)
        cancel.place(x=320, y=500)
        save = Button(inputWindow, font=("Arial", 12, "bold"), text="Save", bg=light1, fg=dark1, command=save)
        save.place(x=430, y=500)

        fileToRead = os.getcwd() + f"\Books\{nameOfBook}\{logToViewOrEdit}.json"
        f = open(fileToRead)
        data = json.load(f)
        log.insert(0, data["logName"])
        if data["departure"]["airportCode"]:
            depAir.insert(0, data["departure"]["airportCode"])
        if data["destination"]["airportCode"]:
            desAir.insert(0, data["destination"]["airportCode"])
        if data["logContent"]:
            entry.insert('1.0', data["logContent"])
        f.close()
        inputWindow.after(1, capitalizeLoop)
    elif typeOfWindow == "view":
        logLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Log Name:", bg=light2, fg=dark1)
        logLabel.place(x=60.5, y=10)

        log = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        log.place(x=63.5, y=35)

        depAirLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Dep. Airport ICAO Code:", bg=light2,
                            fg=dark1)
        depAirLabel.place(x=60.5, y=60)

        depAir = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        depAir.place(x=63.5, y=85)

        desAirLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Dest. Airport ICAO Code:", bg=light2,
                            fg=dark1)
        desAirLabel.place(x=60.5, y=110)

        desAir = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
        desAir.place(x=63.5, y=135)

        entryLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Log:", bg=light2, fg=dark1)
        entryLabel.place(x=60.5, y=160)

        entry = tkscrolled.ScrolledText(inputWindow, width=84, height=18, wrap='word')
        entry.place(x=63.5, y=185)

        cancel = Button(inputWindow, font=("Arial", 12, "bold"), text="Back", bg=light1, fg=dark1, command=cancel)
        cancel.place(x=373, y=500)

        fileToRead = os.getcwd() + f"\Books\{nameOfBook}\{logToViewOrEdit}.json"
        f = open(fileToRead)
        data = json.load(f)
        log.insert(0, data["logName"])

        if data["departure"]["airportCode"]:
            depAir.insert(0, data["departure"]["airportCode"])

            depAirportNameLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Dep. Airport Name:", bg=light2,
                                        fg=dark1)
            depAirportNameLabel.place(x=306, y=60)

            depAirportName = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
            depAirportName.place(x=309, y=85)
            depAirportName.insert(0, data["departure"]["airportName"])
            depAirportName.config(state="disabled")

            depCountryNameLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Dep. Country Name:", bg=light2,
                                        fg=dark1)
            depCountryNameLabel.place(x=551.5, y=60)

            depCountryName = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
            depCountryName.place(x=554.5, y=85)
            depCountryName.insert(0, data["departure"]["countryName"])
            depCountryName.config(state="disabled")

        if data["destination"]["airportCode"]:
            desAir.insert(0, data["destination"]["airportCode"])

            desAirportNameLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Dest. Airport Name:", bg=light2,
                                        fg=dark1)
            desAirportNameLabel.place(x=306, y=110)

            desAirportName = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
            desAirportName.place(x=309, y=135)
            desAirportName.insert(0, data["destination"]["airportName"])
            desAirportName.config(state="disabled")

            desCountryNameLabel = Label(inputWindow, font=("Arial", 12, "bold"), text="Dest. Country Name:", bg=light2,
                                        fg=dark1)
            desCountryNameLabel.place(x=551.5, y=110)

            desCountryName = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
            desCountryName.place(x=554.5, y=135)
            desCountryName.insert(0, data["destination"]["countryName"])
            desCountryName.config(state="disabled")

        if data["departure"]["airportCode"] and data["destination"]["airportCode"]:
            v = IntVar()

            nauticalMile = Radiobutton(inputWindow, highlightthickness=0, borderwidth=0, variable=v, value=1)
            nauticalMile.place(x=623.75, y=35)
            nauticalMile.select()

            kilometre = Radiobutton(inputWindow, highlightthickness=0, borderwidth=0, variable=v, value=2)
            kilometre.place(x=653.75, y=35)

            distanceTraveledLabel = Label(inputWindow, font=("Arial", 12, "bold"),
                                          text="Distance Traveled:            NM KM", bg=light2,
                                          fg=dark1)
            distanceTraveledLabel.place(x=428.75, y=10)

            def radioButtonLoop(selected):
                distanceTraveled = Entry(inputWindow, font=("Arial", 12), highlightthickness=0, borderwidth=0)
                distanceTraveled.place(x=431.75, y=35)
                distanceTraveled.delete(0, "end")
                if selected == 1:
                    distanceTraveled.insert(0, str(("{:.2f}".format(data["distanceTraveled"] / 1.852))))
                else:
                    distanceTraveled.insert(0, str(("{:.2f}".format(data["distanceTraveled"]))))
                distanceTraveled.config(state="disabled")

                inputWindow.after(100, lambda: radioButtonLoop(v.get()))

            inputWindow.after(0, lambda: radioButtonLoop(v.get()))
        if data["logContent"]:
            entry.insert('1.0', data["logContent"])

        log.config(state="disabled")
        depAir.config(state="disabled")
        desAir.config(state="disabled")
        entry.config(state="disabled")
        f.close()

    inputWindow.mainloop()
