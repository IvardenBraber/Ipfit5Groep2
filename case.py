import datetime
class case:
    def __init__(self, case_name, case_folder, case_summary, serial_number_case, imaged_number, serial_number_carrier):
        self.case_name = case_name
        self.folder = case_folder
        self.summary = case_summary
        self.date = datetime.datetime.now()


    def get_case_name(self):
        return self.case_name
    def get_case_folder(self):
        return self.case_folder
    def get_case_summary(self):
        return self.case_summary
    def get_date(self):
        return self.date

    def set_case_name(self, new_value):
        self.case_name = new_value
    def set_case_folder(self, new_value):
        self.case_folder = new_value
    def set_case_summary(self, new_value):
        self.case_summary = new_value
    def set_date(self):
        self.date = datetime.datetime.now()