from tkinter import *
import tkinter as tk
import menuV1
import LogoutV1


import sqlite3
import hashlib
from database_nieuw import DatabaseManager

import main_nieuw
# import LoginCheckV1 #toegevoegd
# onderaan toegevoegd
global username
global usernameEntry
# nieuwe import
import tkinter.messagebox as tm


class HOAX(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("HOAX")
        self.geometry("500x500")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        new_database = DatabaseManager()

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

        a = Label(self, text="Password: ")
        a.place(x=132, y=220)

        c = Button(self, text="LOGIN", width=5, command=lambda: logincheck(self))
        # LoginCheckV1.login_check())#LoginCheckV1)#[menuV1.Homepage(), controller.close_frame()])
        # # controller.close_frame() toegevoegd
        # [menuV1.Homepage(), self.destroy()])
        # self.destroy verwijdert de frame Login#homepage command toegevoegd

        c.place(x=200, y=350)

        f = Button(self, text="Go Back", width=7, command=lambda: controller.show_frame("Main"))
        f.place(x=120, y=350)

        usernameEntry = Entry(self)
        usernameEntry.place(x=220, y=200)
        passwordEntry = Entry(self, show="**")
        passwordEntry.place(x=220, y=220)

        def logincheck(self):
            username = usernameEntry.get()
            password = passwordEntry.get()

            errorMessage = False

            if len(username) != 0:
                if len(password) != 0:
                    con = sqlite3.connect("database.db")
                    cur = con.cursor()
                    cur.execute("SELECT U_name, U_password FROM users")
                    users = cur.fetchall()
                    con.close()
                    #cur.close()
                    #con.close()
                    #for user in users:
                    for tuples in users:

                        if tuples[0] == username:
                            password = hashlib.md5(password.encode()).hexdigest()
                            if tuples[1] == password:
                                errorMessage = True

                            #else:
                            #    print(tuples[1])
                            #    print("printing")

                        #else:
                        #    print("test#")
                        #    errorMessage = False
                        #    return errorMessage
                else:
                    tm.showerror("Error", "Wrong username or password..")
            else:
                tm.showerror("Error", "Wrong username or password...")

            if errorMessage is True:
                menuV1.Homepage()
                controller.close_frame()

            if errorMessage is False:
                tm.showerror("Error", "Wrong username or password...")


class CreateAccount(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        create_account_label = Label(self, text="Create Account", width=14, font=("bold", 15))
        create_account_label.place(x=170, y=53)

        create_account_label = Label(self, text="You need to fill in all the boxes in order to create an account.", width=64)
        create_account_label.place(x=30, y=85)

        a = Label(self, text="Full Name: ", width=11)
        a.place(x=80, y=130)

        c_fullname = Entry(self)
        c_fullname.place(x=185, y=130)

        b = Label(self, text="Email: ", width=7)
        b.place(x=90, y=180)

        c_email = Entry(self)
        c_email.place(x=185, y=180)

        c = Label(self, text="Username: ", width=10)
        c.place(x=80, y=230)

        c_username = Entry(self)
        c_username.place(x=185, y=230)

        d = Label(self, text="Password: ", width=10)
        d.place(x=80, y=280)

        c_password = Entry(self, show="**")
        c_password.place(x=185, y=280)

        e = Button(self, text="Register account", width=16, command=lambda: register_account(self))#controller.show_frame("Login"))
        e.place(x=195, y=350)

        f = Button(self, text="Go Back", width=7, command=lambda: controller.show_frame("Main"))
        f.place(x=120, y=350)

        def register_account(self):
            name = c_fullname.get()
            email = c_email.get()
            username_create = c_username.get()
            password_create = c_password.get()

            if len(name) != 0:
                if len(email) != 0:
                    if len(username_create) != 0:
                        if len(password_create) != 0:

                            con = sqlite3.connect("database.db", timeout=1)
                            cur = con.cursor()
                            usernameCheckExists = cur.execute("SELECT COUNT (*) FROM users WHERE U_name = ?", [username_create]).fetchone()
                            con.close()
                            print(usernameCheckExists)
                            print(username_create)

                            if usernameCheckExists[0] == 0:
                                DatabaseManager.createUser(DatabaseManager, name, password_create, email)
                                controller.show_frame("Login")

                            else:
                                tm.showerror("Error", "Incorrect values")

                else:
                    tm.showerror("Error", "Incorrect values")
            else:
                tm.showerror("Error", "Incorrect values")



# positionRight = tk.winfo_screenwidth() / 2 - tk.winfo_reqwidth() / 2
# positionDown = tk.winfo_screenheight() / 3 - tk.winfo_reqheight() / 2
#
# tk.geometry("+{}+{}".format(positionRight, positionDown))

if __name__ == '__main__':
    test = HOAX()
    test.title("HOAX")
    test.iconbitmap('Hoax.ico')
    test.geometry("500x500")
    test.mainloop()
