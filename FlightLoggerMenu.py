# Imports
from tkinter import *
from tkinter import messagebox
import FlightLogger
import os


# Window Setup
def createWindowForBook(nameOfBook):
    dark2 = "#103B82"
    dark1 = "#2B5384"
    med = "#5E9CCB"
    light2 = "#7DC6EB"
    light1 = "#EBDFD8"
    textForUi = "FlyPyLog - " + nameOfBook
    windowName = nameOfBook + "Window"
    windowName = Toplevel()
    windowName.title("FlyPyLog-FlightLogger Menu")
    windowName.geometry("400x500")
    windowName.configure(bg="white")
    windowName.resizable(False, False)
    # Error Checking
    currentBookLocation = os.getcwd() + f'\Books\{nameOfBook}'

    if not os.path.isdir(currentBookLocation):
        messagebox.showerror(title="lol no", message="This book no longer exists.", parent=windowName)
        windowName.destroy()
        return

    def add_log():
        FlightLogger.createWindow(nameOfBook, "add")

    def view_log():
        curselectiontmp = LogBox.curselection()
        try:
            curselection = list(curselectiontmp)[0]
        except IndexError:
            print("No item selected to view. IndexError")
            messagebox.showerror(title="lol no", message="No item selected to view. IndexError", parent=windowName)
            return
        curselectionText = LogBox.get(curselection)
        FlightLogger.createWindow(nameOfBook, "view", curselectionText)

    def edit_log():
        curselectiontmp = LogBox.curselection()
        try:
            curselection = list(curselectiontmp)[0]
        except IndexError:
            print("No item selected to edit. IndexError")
            messagebox.showerror(title="lol no", message="No item selected to edit. IndexError", parent=windowName)
            return
        curselectionText = LogBox.get(curselection)
        FlightLogger.createWindow(nameOfBook, "edit", curselectionText)

    def delete_log():
        curselectiontmp = LogBox.curselection()
        try:
            curselection = list(curselectiontmp)[0]
        except IndexError:
            print("No item selected to delete. IndexError")
            messagebox.showerror(title="lol no", message="No item selected to delete. IndexError", parent=windowName)
            return

        log_delYN = messagebox.askyesno(title="Delete", message="Do you wish to proceed with the deletion?",
                                        parent=windowName)
        if log_delYN == True:
            TextFileNameWithoutTxt = LogBox.get(curselectiontmp)
            textFileToDelete = currentBookLocation + str(f"\\{TextFileNameWithoutTxt}.json")
            os.remove(textFileToDelete)
            LogBox.delete(curselection, last=None)

    # Color Change on Hover
    def on_enterV(e):
        View['background'] = med

    def on_leaveV(e):
        View['background'] = dark2

    def on_enterE(e):
        Edit['background'] = med

    def on_leaveE(e):
        Edit['background'] = dark2

    def on_enterN(e):
        NewLog['background'] = med

    def on_leaveN(e):
        NewLog['background'] = dark2

    def on_enterD(e):
        Del['background'] = med

    def on_leaveD(e):
        Del['background'] = dark2

    # Ye 2nd Mighty Listbox
    LogBox = Listbox(windowName, font=("Arial", 12, "bold"), activestyle="none", bg="light gray", bd=0, height=15,
                     width=20,
                     selectbackground=light2)
    LogBox.place(x=40, y=90)
    LogBox.yview()

    # File Checking On Start
    def fileChecking():
        logs = []
        logs.clear()
        selectedIndex = LogBox.curselection()

        LogBox.delete(0, "end")
        base = str(os.path.abspath(os.getcwd())) + f"\Books\{nameOfBook}"
        for entry in os.listdir(base):
            # Removes the last 5 characters, so removes .json while displaying
            logs.append(entry[:-5])
        LogBox.insert(END, *logs)

        selectedIndexExists = True
        try:
            selectedIndex[0]
        except:
            selectedIndexExists = False

        if selectedIndexExists:
            LogBox.select_set(selectedIndex)

        windowName.after(1, fileChecking)

    Can2 = Canvas(windowName, bg=light2, borderwidth=0, height=43.5, width=200000, highlightthickness=0)
    Can2.place(x=0, y=0)

    Logo2 = Label(windowName, font=("Arial", 18, "bold"), text=textForUi, bg=light2, fg=dark2)
    Logo2.place(x=10, y=5)

    View = Button(windowName, font=("Arial", 12), text='View', highlightthickness=0, bg=dark2, fg='white',
                  borderwidth=0, width=10, height=1, command=view_log)
    View.place(x=240, y=90)
    View.bind("<Enter>", on_enterV)
    View.bind("<Leave>", on_leaveV)

    Edit = Button(windowName, font=("Arial", 12), text='Edit', highlightthickness=0, bg=dark2, fg='white',
                  borderwidth=0, width=10, height=1, command=edit_log)
    Edit.place(x=240, y=120)
    Edit.bind("<Enter>", on_enterE)
    Edit.bind("<Leave>", on_leaveE)

    NewLog = Button(windowName, font=("Arial", 12), text='New Log', highlightthickness=0, bg=dark2, fg='white',
                    borderwidth=0, width=10, height=1, command=add_log)
    NewLog.place(x=240, y=150)
    NewLog.bind("<Enter>", on_enterN)
    NewLog.bind("<Leave>", on_leaveN)

    Del = Button(windowName, font=("Arial", 12), text='Delete', highlightthickness=0, bg=dark2, fg='white',
                 borderwidth=0, width=10, height=1, command=delete_log)
    Del.place(x=240, y=180)
    Del.bind("<Enter>", on_enterD)
    Del.bind("<Leave>", on_leaveD)

    windowName.after(0, fileChecking)
    windowName.mainloop()
