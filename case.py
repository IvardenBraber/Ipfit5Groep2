import datetime
class case:
    def __init__(self, case_Name, serial_Number_Case, imaged_Number, serial_Number_Carrier, case_Summary):
        self.case_Name = case_Name
        self.date = datetime.datetime.now()
        self.serial_Number_Case = serial_Number_Case
        self.imaged_Number = imaged_Number
        self.serial_Number_Carrier = serial_Number_Carrier
        self.summary = case_Summary
