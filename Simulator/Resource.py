class Resource:
    def __init__(self, name):
        self.name = name
        self.r_timestamp = 0
        self.w_timestamp = 0

    # GETTER
    def getName(self):
        return self.name

    def getRTS(self):
        return self.r_timestamp
    
    def getWTS(self):
        return self.w_timestamp

    # SETTER
    def setRTS(self, newR):
        self.r_timestamp = newR
    
    def setWTS(self, newW):
        self.w_timestamp = newW

    # PRINT ya ges ya
    def printerNiBhovst(self):
        print("Resource :"+self.name)
        print("RTS :"+str(self.r_timestamp))
        print("WTS :"+str(self.w_timestamp))
        print("")