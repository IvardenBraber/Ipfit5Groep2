from tkinter import *


class CreateAccountError(Tk):

    def createerror(self):
        gui = self
        gui.geometry("400x200")
        gui.title("HOAX")

        new_case_label = Label(gui, text="Error", width=15, font=("bold", 15))
        new_case_label.place(x=118, y=43)

        a = Label(gui, text="You entered a name that already exists.", width=38)
        a.place(x=65, y=100)

        cc = Button(gui, text="OK", command=lambda: self.destroy())
        cc.place(x=190, y=146)


    def __init__(self):
        Tk.__init__(self)
        self.createerror()


if __name__ == "__main__":
    run = CreateAccountError()
    run.mainloop()
