import sqlite3
import hashlib

class DatabaseManager:
    conn = None
    cursor = None
    databaseLocation = "database.db"

    # initialise DB, creates database and tables if then are not already created
    def __init__(self):
        self.conn = sqlite3.connect(self.databaseLocation)
        self.cursor = self.conn.cursor()

        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS users (
            U_id INTEGER PRIMARY KEY AUTOINCREMENT,
            U_name TEXT,
            U_password TEXT,
            U_mail TEXT);""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            C_number INTEGER PRIMARY KEY AUTOINCREMENT,
            C_folder TEXT,
            image_number INT,
            image_location TEXT,
            serial_number TEXT,
            data_cariernumber TEXT,
            create_date DATE,
            closed_date DATE
        );
        """)

        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Evidence (
            E_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            E_c_number INT,
            hash_value TEXT,
            bookmark BOOLEAN,
            benign BOOLEAN,
            notes TEXT,
                FOREIGN KEY (E_c_number) REFERENCES cases(C_number)
    
        );
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS works_on (
        W_u_ID INT,
        W_c_number INT,
        hours DECIMAL(3,1),
            PRIMARY KEY (W_u_ID, W_c_number),
            FOREIGN KEY (W_u_ID) REFERENCES users(U_id)
        ); 
        """)
        self.conn.commit()

    # Close the Database connection
    def close(self):
        self.conn.close()


    # USERS
    def createUser(self, name, password, email):
        hashedpassword = hashlib.md5(password.encode()).hexdigest()
        if self.getUserId(self, email) is not False:
            return "Email already registered"
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users (U_name, U_password, U_mail) VALUES (?,?,?)", (name, hashedpassword, email))
        con.commit()
        con.close()

    def userAuthenticate(self, email, password):
        passwordRight = False
        userpasswordHashed = hashlib.md5(password.encode()).hexdigest()
        result = self.cursor.execute("SELECT * FROM users WHERE U_mail = ?", [email]).fetchone()

        if result == None:
            return False
        else:
            U_id = result[0]
            U_name = result[1]
            U_password = result[2]
            U_mail = result[3]

            if U_password == userpasswordHashed:
                passwordRight = True

        return passwordRight

    def getUserId(self, email):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        result = cur.execute("SELECT U_id FROM users WHERE U_mail = ?", [email]).fetchone()
        con.close()
        if result == None:
            return False
        else:
            return result[0]


    def getUserName(self, userid):
        result = self.cursor.execute("SELECT U_name FROM users WHERE U_id = ?", [userid]).fetchone()
        if result == None:
            return False
        else:
            return result[0]
    def getUserEmail(self, userid):
        result = self.cursor.execute("SELECT U_mail FROM users WHERE U_id = ?", [userid]).fetchone()
        if result == None:
            return False
        else:
            return result[0]


    # CASES
    def createCase(self, caseFolder, image_number, imageLocation, serialNumber, dataCarrierNumber, createData, closedData):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO cases (C_folder, image_number, image_location, serial_number, data_cariernumber, create_date, closed_date) VALUES (?,?,?,?,?,?,?)", (caseFolder, image_number, imageLocation, serialNumber, dataCarrierNumber, createData, closedData))
        con.commit()
        con.close()

    def getAllCaseIds(self):
        cases = []

        results = self.cursor.execute("SELECT C_number FROM cases").fetchall()
        for row in results:
            caseId = row[0]
            cases.append(caseId)

        return cases

    def getCaseImageLocation(self, id):
        result = self.cursor.execute("SELECT image_location FROM cases WHERE C_number = ?", [id]).fetchone()
        if result == None:
            return False
        else:
            return result[0] and False

    def getCaseSerialNumber(self, id):
        result = self.cursor.execute("SELECT serialNumber FROM cases WHERE C_number = ?", [id]).fetchone()
        if result == None:
            return False
        else:
            return result[0] and False

    def getCaseDataCarrierNumber(self, id):
        result = self.cursor.execute("SELECT dataCarrierNumber FROM cases WHERE C_number = ?", [id]).fetchone()
        if result == None:
            return False
        else:
            return result[0] and False

    def getCaseCreateDate(self, id):
        result = self.cursor.execute("SELECT createData FROM cases WHERE C_number = ?", [id]).fetchone()
        if result == None:
            return False
        else:
            return result[0] and False


    def getCaseClosedDate(self, id):
        result = self.cursor.execute("SELECT closed_date FROM cases WHERE C_number = ?", [id]).fetchone()
        if result == None:
            return False
        else:
            return result[0] and False

    def setCaseClosedDate(self, id, closedDate):
        self.cursor.execute("UPDATE cases SET closed_date = ? WHERE C_number = ?", (closedDate, id))
        self.conn.commit()

    def getCaseFolder(self, id):
        result = self.cursor.execute("SELECT C_folder FROM cases WHERE C_number = ?", [id]).fetchone()
        if result == None:
            return False
        else:
            return result[0] and False

    def getCaseImageNumber(self, id):
        result = self.cursor.execute("SELECT image_number FROM cases WHERE C_number = ?", [id]).fetchone()

        if result == None:
            return False
        else:
            return result[0] and False



    # EVIDENCE
    def createEvidence(self, caseNumber, hashValue, bookmark, benign, notes):
        self.cursor.execute("INSERT INTO Evidence (E_c_number, hash_value, bookmark, benign, notes) VALUES (?,?,?,?,?)",
            (caseNumber, hashValue, bookmark, benign, notes))
        self.conn.commit()

    def getAllEvidenceIds(self, caseId):
        evidence = []

        results = self.cursor.execute("SELECT E_ID FROM Evidence").fetchall()
        for row in results:
            evidenceId = row[0]
            evidence.append(evidenceId)

        return evidence

    def getEvidenceBookmark(self, id):
        result = self.cursor.execute("SELECT bookmark FROM Evidence WHERE E_ID = ?", [id]).fetchone()
        if result == None:
            return False
        else:
            return result[0]

    def getEvidenceBenign(self, id):
        result = self.cursor.execute("SELECT benign FROM Evidence WHERE E_ID = ?", [id]).fetchone()
        if result == None:
            return False
        else:
            return result[0]

    def getEvidenceNotes(self, id):
        result = self.cursor.execute("SELECT notes FROM Evidence WHERE E_ID = ?", [id]).fetchone()
        if result == None:
            return False
        else:
            return result[0]

    def getEvidenceHashValue(self, id):
        result = self.cursor.execute("SELECT hash_value FROM Evidence WHERE E_ID = ?", [id]).fetchone()
        if result == None:
            return False
        else:
            return result[0]

    # works_on
    def insertWorksOn(self, userId, caseNumber):
        self.cursor.execute("INSERT INTO works_on (W_u_ID, W_c_number) VALUES (?,?)",
                            (userId, caseNumber))
        self.conn.commit()

    def getHoursWorkedOn(self, userId, caseNumber):
        result = self.cursor.execute("SELECT hours FROM works_on WHERE W_u_ID = ? and W_c_number = ?", [userId, caseNumber]).fetchone()

        if result == None:
            return False
        else:
            return result[0]

    def setHoursWorkedOn(self, userid, caseNumber, hours):
        self.cursor.execute("UPDATE works_on SET hours = ? WHERE W_u_ID = ? and W_c_number = ?", (hours, userid, caseNumber))
        self.conn.commit()