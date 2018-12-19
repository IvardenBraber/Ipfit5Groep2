import sqlite3
class account:
    name = ''
    employee_number = ''
    password = ''
    email = ''

    def __init__(self, name, employee_number, password, email):
        self.name = name
        self.employee_number = employee_number
        self.password = password
        self.email = email

    def get_account_name(self):
        return self.name
    def get_account_employee_number(self):
        return self.employee_number
    def get_account_password(self):
        return self.password
    def get_account_email(self):
        return self.email

    def set_account_name(self, new_name):
        self.name = new_name
    def set_account_employee_number(self, new_number):
        self.employee_number = new_number
    def set_account_password(self, new_password):
        self.password = new_password
    def set_account_email(self, new_email):
        self.email = new_email



def check_login(input_name, input_password):
    dictionary_1 = {'Geerd' : 'wachtwoord1', 'Piet' : 'wachtwoord2' }
    try:

        for slot in dictionary_1:
            if input_password == dictionary_1[input_name]:
                print('U wordt nu doorgestuurd')
                break
            else:
                print('Foutief wachtwoord')
                break
    except:
        print('Onbekende gebruiker')

    '''Moet nog een koppeling met de database gemaakt worden zodra deze af is.'''



