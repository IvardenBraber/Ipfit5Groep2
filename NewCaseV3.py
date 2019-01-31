from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sqlite3

#from case import case

import menuV1
import CaseCreatedV1
from database_nieuw import DatabaseManager
import case
import AddImageV2
import datetime
import time
from OpenCaseV1 import OpenCase



def browsefunction(self):
    filedirectory = filedialog.askdirectory()
    self.directorypath.set(filedirectory)
    #print(self.entIn.get())

class NewCase(Tk):

    def createnewcase(self):
        gui = self
        gui.geometry("600x425")
        gui.title("HOAX")
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, '-topmost', False)
        gui.iconbitmap('Hoax.ico')

        new_case_label = Label(gui, text="New Case", width=14, font=("bold", 15))
        new_case_label.place(x=215, y=53)

        a = Label(gui, text="Case Name:", width=10)
        a.place(x=110, y=130)

        ab = Entry(gui)
        ab.place(x=230, y=130)

        def getcasename():
            casename = ab.get()
            return casename

        c = Label(gui, text="Employee number:", width=14)
        c.place(x=100, y=180)

        cb = Entry(gui)
        cb.place(x=230, y=180)

        def getimagelocation():
            imagelocation = cb.get()
            return imagelocation

        d = Label(gui, text="Case Summary:", width=13)
        d.place(x=105, y=230)

        db = Entry(gui)
        db.place(x=230, y=230)

        def getcasesummary():
            casesummary = db.get()
            return casesummary

        #cInfo = ab.get()
        #cFolder = cb.get()
        #cSummary = db.get()

        con = sqlite3.connect("database.db")
        cur = con.cursor()

        e = ttk.Button(gui, text="Create Case", width=11,
                       command=lambda: [DatabaseManager.createCase(DatabaseManager, getcasename(), 0, getimagelocation(), 0, 0, datetime.datetime.now(), datetime.datetime.now()),
                                        CaseCreatedV1.NewClassCreated.save_casename(getcasename()), print(getcasename()), menuV1.Homepage.set_Opencase_False(self),
                                        self.destroy(), CaseCreatedV1.NewClassCreated()]) #"#, print(getcasename(),getcasesummary(), getimagelocation(), datetime.datetime.now())])
        e.place(x=285, y=300)


        f = ttk.Button(gui, text="Go Back", width=7, command=lambda: [menuV1.Homepage(), self.destroy()])
        f.place(x=205, y=300)

    def __init__(self):
        Tk.__init__(self)
        self.createnewcase()


if __name__ == "__main__":
    run = NewCase()
    run.title("HOAX")
    run.mainloop()
