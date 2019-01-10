from tkinter import *


class Verify(Tk):

    def verifyimage(self):
        gui = self
        gui.geometry("400x250")
        gui.title("HOAX")

        new_case_label = Label(gui, text="Verify your image", width=17, font=("bold", 15))
        new_case_label.place(x=118, y=43)

        a = Label(gui, text="Choose the image you want to verify: ", width=116)
        a.place(x=-200, y=100)

    def __init__(self):
        Tk.__init__(self)
        self.verifyimage()


if __name__ == "__main__":
    run = Verify()
    run.mainloop()
