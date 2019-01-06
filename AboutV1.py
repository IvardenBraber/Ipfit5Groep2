from tkinter import *


class About(Tk):

    def aboutinfo(self):
        gui = self
        gui.geometry("400x250")
        gui.title("HOAX")

        new_case_label = Label(gui, text="About this tool", width=15, font=("bold", 15))
        new_case_label.place(x=118, y=43)

        a = Label(gui, text="This tool has been created for analyze purposes.\n "
                            "If you have any questions, you may contact the following email: ", width=116)
        a.place(x=-200, y=100)

        a = Label(gui, text="Created by: \n Ivar den Braber, Calvin Dijk, Michael Heenes and Alison de Bruijn ",
                  width=80)
        a.place(x=-85, y=170)

    def __init__(self):
        Tk.__init__(self)
        self.aboutinfo()


if __name__ == "__main__":
    run = About()
    run.mainloop()
