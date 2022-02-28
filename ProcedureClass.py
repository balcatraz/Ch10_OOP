class Procedure:
    def __init__(self, nm, date, pract, chrg, pid):
        self.__name = nm
        self.__date = date
        self.__pract = pract
        self.__charge = chrg
        self.__patientid = pid

    def getName(self):
        return self.__name

    def getDate(self):
        return self.__date

    def getPractitioner(self):
        return self.__pract

    def getCharge(self):
        return self.__charge

    def getPtID(self):
        return self.__patientid