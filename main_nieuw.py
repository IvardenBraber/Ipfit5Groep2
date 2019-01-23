from database_nieuw import DatabaseManager


def main():

    # USER
    DatabaseManager().createUser("Michael", "password", "michael@email.com")
    print(DatabaseManager().userAuthenticate("Michael@email.com", "password"))

    # Case
    DatabaseManager().createCase("Map", 101, "/image/evidence.img", "ljfhdgdgjfjnb", "KPN0284", "2019-01-01 18:01:00.000", "2019-01-20 18:01:00.000")
    print(DatabaseManager().getCaseImageNumber(1))

    # evidence
    DatabaseManager().createEvidence(1, "fdbfb", True, False, "Notes staan hier")
    print(DatabaseManager().getAllEvidenceIds(1))
    print(DatabaseManager().getEvidenceHashValue(1))

    # hours worked on
    #DatabaseManager().insertWorksOn(1,1)
    DatabaseManager().setHoursWorkedOn(1,1, 24)
    print(DatabaseManager().getHoursWorkedOn(1,1))



if __name__ == "__main__":
    main()

