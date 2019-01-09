from tkinter import *


class CreateCaseError(Tk):

    def createerror(self):
        gui = self
        gui.geometry("400x200")
        gui.title("HOAX")

        error_label = Label(gui, text="Error", width=15, font=("bold", 15))
        error_label.place(x=118, y=43)

        a = Label(gui, text="You entered a number that already exists.", width=38)
        a.place(x=65, y=100)

        b = Button(gui, text="OK", command=lambda: self.destroy())
        b.place(x=190, y=146)

    def __init__(self):
        Tk.__init__(self)
        self.createerror()


if __name__ == "__main__":
    run = CreateCaseError()
    run.mainloop()
