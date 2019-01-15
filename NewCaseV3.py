from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#from case import case

import menuV1
import CaseCreatedV1

def browsefunction(self):
    filedirectory = filedialog.askdirectory()
    self.directorypath.set(filedirectory)
    #print(self.entIn.get())

class NewCase(Tk):

    def createnewcase(self):
        gui = self
        gui.geometry("600x425")
        gui.title("HOAX")

        new_case_label = Label(gui, text="New Case", width=14, font=("bold", 15))
        new_case_label.place(x=215, y=53)

        a = Label(gui, text="Case Name:", width=10)
        a.place(x=110, y=130)

        ab = Entry(gui)
        ab.place(x=230, y=130)

        c = Label(gui, text="Case Folder:", width=12)
        c.place(x=100, y=180)

        cc = Button(gui, text="Browse..", command=lambda: browsefunction(self))
        cc.place(x=375, y=176)

        self.directorypath = StringVar()
        cb = Entry(gui, textvariable=self.directorypath)
        cb.place(x=230, y=180)

        d = Label(gui, text="Case Summary:", width=13)
        d.place(x=105, y=230)

        db = Entry(gui)
        db.place(x=230, y=230)

        cInfo = ab.get()
        cFolder = cb.get()
        cSummary = db.get()

        e = ttk.Button(gui, text="Create Case", width=11,
                       command=lambda: [self.destroy(), CaseCreatedV1.NewClassCreated()]) #, (case(cInfo, cFolder, cSummary))]) #lambda toegevoegd, is dit nodig?
        e.place(x=285, y=300)

        f = ttk.Button(gui, text="Go Back", width=7, command=self.destroy)
        f.place(x=205, y=300)

    def __init__(self):
        Tk.__init__(self)
        self.createnewcase()


#if __name__ == "__main__":
#    run = NewCase()
#    run.title("HOAX")
#    run.mainloop()
