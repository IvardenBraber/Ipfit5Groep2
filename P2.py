from tkinter import *
import tkinter as tk
import menuV1
import LogoutV1

class HOAX(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("HOAX")
        self.geometry("500x500")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frame = {}
        for F in (Main, CreateAccount, Login):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frame[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Main")

    def show_frame(self, page_name):
        frame = self.frame[page_name]
        frame.tkraise()

    def close_frame(self):
        self.destroy()


class Main(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        a = Button(self, text="LOGIN", command=lambda: controller.show_frame("Login"))
        a.place(x=220, y=200)

        b = Button(self, text="CREATE ACCOUNT", command=lambda: controller.show_frame("CreateAccount"))
        b.place(x=185, y=250)


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        login_label = Label(self, text="Login Page", width=14, font=("bold", 15))
        login_label.place(x=170, y=73)

        a = Label(self, text="Username: ")
        a.place(x=130, y=200)

        b = Label(self, text="Password: ")
        b.place(x=132, y=220)

        c = Button(self, text="LOGIN", width=5, command=lambda: [menuV1.Homepage(), controller.close_frame()]) #controller.close_frame() toegevoegd
        #[menuV1.Homepage(), self.destroy()])
        #self.destroy verwijdert de frame Login#homepage command toegevoegd

        c.place(x=200, y=350)

        f = Button(self, text="Go Back", width=7, command=lambda: controller.show_frame("Main"))
        f.place(x=120, y=350)

        e = Entry(self)
        e.place(x=220, y=200)
        f = Entry(self, show="**")
        f.place(x=220, y=220)


class CreateAccount(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        create_account_label = Label(self, text="Create Account", width=14, font=("bold", 15))
        create_account_label.place(x=170, y=53)

        a = Label(self, text="Full Name: ", width=11)
        a.place(x=80, y=130)

        ab = Entry(self)
        ab.place(x=185, y=130)

        b = Label(self, text="Email: ", width=7)
        b.place(x=90, y=180)

        bb = Entry(self)
        bb.place(x=185, y=180)

        c = Label(self, text="Username: ", width=10)
        c.place(x=80, y=230)

        cb = Entry(self)
        cb.place(x=185, y=230)

        d = Label(self, text="Password: ", width=10)
        d.place(x=80, y=280)

        db = Entry(self, show="**")
        db.place(x=185, y=280)

        e = Button(self, text="Register account", width=16, command=lambda: controller.show_frame("Login"))
        e.place(x=195, y=350)

        f = Button(self, text="Go Back", width=7, command=lambda: controller.show_frame("Main"))
        f.place(x=120, y=350)


# positionRight = tk.winfo_screenwidth() / 2 - tk.winfo_reqwidth() / 2
# positionDown = tk.winfo_screenheight() / 3 - tk.winfo_reqheight() / 2
#
# tk.geometry("+{}+{}".format(positionRight, positionDown))

if __name__ == '__main__':
    test = HOAX()
    test.title("HOAX")
    test.geometry("500x500")
    test.mainloop()
