from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#from case import case

import tkinter.messagebox as tm
import menuV1
import CaseCreatedV1
from database_nieuw import DatabaseManager
import menuV1



caseId = 0

def browsefunction(self):
    filedirectory = filedialog.askdirectory()
    self.directorypath.set(filedirectory)


class OpenCase(Tk):



    def opencase(self):
        gui = self
        gui.geometry("400x250")
        gui.title("HOAX")
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, '-topmost', False)
        gui.iconbitmap('Hoax.ico')



        new_case_label = Label(gui, text="Load Case", width=9, font=("bold", 15))
        new_case_label.place(x=148, y=53)

        c = Label(gui, text="Case Name:", width=15)
        c.place(x=15, y=130)

        cb = Entry(gui)
        cb.place(x=136, y=130)

        e = ttk.Button(gui, text="Open Case", width=11, command=lambda: [setCaseName(getCaseName())])
        e.place(x=185, y=200)

        def getCaseName():
            name = cb.get()
            return name
        f = ttk.Button(gui, text="Go Back", width=7, command=lambda: [menuV1.Homepage(), self.destroy()])
        f.place(x=125, y=200)

        def setCaseName(input_name):
            global caseId
            name = input_name
            #check of de naam bestaat



            print(DatabaseManager.getCaseId(DatabaseManager, name))
            print(DatabaseManager.getCaseFolder(DatabaseManager, DatabaseManager.getCaseId(DatabaseManager, name)))

            if DatabaseManager.getCaseId(DatabaseManager, name) == False:
                tm.showerror("Error", "Incorrect case name")
            else:
                caseId = DatabaseManager.getCaseId(DatabaseManager, name)
                print(DatabaseManager.getCaseId(DatabaseManager, name))
                self.destroy()
                menuV1.Homepage()




    def __init__(self):
        Tk.__init__(self)
        self.opencase()


if __name__ == "__main__":
    run = OpenCase()
    run.title("HOAX")
    run.mainloop()
