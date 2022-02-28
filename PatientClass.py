class Patient:
    def __init__(self,id,nm,ad,pn,vs):
        self.__id = id
        self.__name = nm
        self.__address = ad
        self.__pnum = pn
        self.__vstatus = vs

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getPhNum(self):
        return self.__pnum

    def getVetStatus(self):
        return self.__vstatus