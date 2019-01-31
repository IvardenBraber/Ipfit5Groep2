from tkinter import *

import hashlib as hash

from tkinter import ttk
from tkinter import filedialog

# import verifyTest

def browsefunction(self):
    file = filedialog.askopenfilename()
    self.directorypath.set(file)

class Verify(Tk):

    def verifyimage(self):
        gui = self
        gui.geometry("500x250")
        gui.title("HOAX")
        gui.iconbitmap('Hoax.ico')

        new_case_label = Label(gui, text="Verify your image", width=17, font=("bold", 15))
        new_case_label.place(x=148, y=43)

        a = Label(gui, text="To verify the image(s) you've added to this case, click the button below. \n "
                            "It will hash the images to ensure nothing has changed.", width=128)
        a.place(x=-200, y=100)

        cc = Button(gui, text="Verify your raw type image(s)", command= lambda: [self.destroy(), verifydd()]) # command=lambda: verifyTest.Listbox)
        cc.place(x=165, y=146)

        cc = Button(gui, text="Verify your E01 type image(s)")  # command=lambda: verifyTest.Listbox)
        cc.place(x=165, y=176)

        # BLOCKSIZE = 65536
        #
        # sha = hash.sha1()
        #
        # with open('C:\\Users\\aliso\\Downloads\\image.dd', 'rb') as imagefile:
        #     file_buffer = imagefile.read(BLOCKSIZE)
        #     while len(file_buffer) > 0:
        #         sha.update(file_buffer)
        #         file_buffer = imagefile.read(BLOCKSIZE)
        #
        #     print(sha.hexdigest())

    def __init__(self):
        Tk.__init__(self)
        self.verifyimage()


class verifydd(Tk):
    def verifydd(self):
        gui = self
        gui.geometry("500x250")
        gui.title("HOAX")
        gui.iconbitmap('Hoax.ico')

        new_case_label = Label(gui, text="Verify RAW image", width=16, font=("bold", 15))
        new_case_label.place(x=152, y=53)

        c = Label(gui, text="Select the file with hash values:", width=33)
        c.place(x=15, y=130)

        ac = Button(gui, text="Browse..", command=lambda: browsefunction(self))
        ac.place(x=372, y=130)

        self.directorypath = StringVar()
        ab = Entry(gui, textvariable=self.directorypath)
        ab.place(x=236, y=133)

        back_button = ttk.Button(gui, text="Go Back", width=10, command=lambda: [self.destroy(), Verify()])
        back_button.place(x=165, y=180)

        verify_button = ttk.Button(gui, text="Verify", width=11) #, command=lambda: [setCaseName(getCaseName())])
        verify_button.place(x=235, y=180)

    def __init__(self):
        Tk.__init__(self)
        self.verifydd()


if __name__ == "__main__":
    run = Verify()
    run.mainloop()
