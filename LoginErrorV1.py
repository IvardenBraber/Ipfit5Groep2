from tkinter import *


class LoginError(Tk):

    def logginerror(self):
        gui = self
        gui.geometry("400x200")
        gui.title("HOAX")

        new_case_label = Label(gui, text="Error", width=15, font=("bold", 15))
        new_case_label.place(x=118, y=43)

        a = Label(gui, text="Your username or password is not correct.", width=116)
        a.place(x=-200, y=100)

        cc = Button(gui, text="OK", command=lambda: self.destroy())
        cc.place(x=190, y=146)


    def __init__(self):
        Tk.__init__(self)
        self.logginerror()


if __name__ == "__main__":
    run = LoginError()
    run.mainloop()
