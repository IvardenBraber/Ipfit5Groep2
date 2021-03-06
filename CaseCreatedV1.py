from tkinter import *
from tkinter import ttk
#from case import case

import menuV1
import AddImageV2

casename = ''

class NewClassCreated(Tk):

    def save_casename(new_casename):
        global casename
        casename = new_casename

    def newclasscreated(self):
        gui = self
        gui.geometry("500x250")
        gui.title("HOAX")
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, '-topmost', False)
        gui.iconbitmap('Hoax.ico')

        new_class_label = Label(gui, text="New Case", width=14, font=("bold", 15))
        new_class_label.place(x=170, y=53)

        a = Label(gui, text="The new case has been created. \n You can now either close this window or click next to add an image.", width=102)
        a.place(x=-105, y=110)

        global casename
        b = ttk.Button(gui, text="Add Image", width=11,
                       command=lambda: [AddImageV2.AddImage.save_casename(casename), self.destroy(), AddImageV2.AddImage()])
        b.place(x=235, y=175)

        c = ttk.Button(gui, text="Close", width=7, command=lambda: [menuV1.Homepage.save_casename(casename), menuV1.Homepage(), self.destroy()])
        c.place(x=170, y=175)

    def __init__(self):
        Tk.__init__(self)
        self.newclasscreated()

#if __name__ == "__main__":
#    run = NewClassCreated()
#    run.title("HOAX")
#    run.mainloop()
