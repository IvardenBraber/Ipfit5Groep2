import sqlite3
class account:
    def __init__(self, name, employee_number, password, email):
        self.name = name
        self.employee_number = employee_number
        self.password = password
        self.email = email
