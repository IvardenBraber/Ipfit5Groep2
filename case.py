import datetime
class case:
    def __init__(self, case_name, case_folder, case_summary, serial_number_case, imaged_number, serial_number_carrier):
        self.case_name = case_name
        self.folder = case_folder
        self.summary = case_summary
        self.date = datetime.datetime.now()
        self.serial_number_case = serial_number_case
        self.imaged_number = imaged_number
        self.serial_number_carrier = serial_number_carrier
