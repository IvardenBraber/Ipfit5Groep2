from tkinter import *

import hashlib as hash

# import verifyTest

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

        cc = Button(gui, text="Verify your image(s)..") # command=lambda: verifyTest.Listbox)
        cc.place(x=180, y=146)

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


if __name__ == "__main__":
    run = Verify()
    run.mainloop()
