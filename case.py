import datetime
class case:
    def __init__(self, case_Name, case_Folder, case_Summary, serial_Number_Case, imaged_Number, serial_Number_Carrier):
        self.case_Name = case_Name
        self.folder = case_Folder
        self.summary = case_Summary
        self.date = datetime.datetime.now()
        self.serial_Number_Case = serial_Number_Case
        self.imaged_Number = imaged_Number
        self.serial_Number_Carrier = serial_Number_Carrier
