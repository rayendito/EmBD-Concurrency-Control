class Resource:
    def __init__(self, name):
        self.name = name
        self.r_timestamp = 0
        self.w_timestamp = 0

    # GETTER
    def getName(self):
        return self.name

    def getR(self):
        return self.r_timestamp
    
    def getW(self):
        return self.w_timestamp

    # SETTER
    def setTimestamp_R(self, newR):
        self.r_timestamp = newR
    
    def setTimestamp_W(self, newW):
        self.w_timestamp = newW

    # PRINT ya ges ya
    def printerNiBhovst(self):
        print("Resource "+self.name)
        print("RTS urg ni senggol donk : "+str(self.r_timestamp))
        print("WTS urg ni senggol donk : "+str(self.w_timestamp))
        print("")