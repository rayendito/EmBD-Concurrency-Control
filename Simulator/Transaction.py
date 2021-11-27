from Simulator.Resource import Resource

class Operation:
    def __init__(self, timestamp, kind, resource, order):
        self.timestamp = timestamp
        self.kind = kind
        self.resource = resource
        self.order = order
    
    # GETTER
    def getKind(self):
        return self.kind

    def getTimestamp(self):
        return self.timestamp

    def getResource(self):
        return self.resource
    
    def getOrder(self):
        return self.order
    
    def printOp(self):
        print("["+str(self.order)+"] T"+str(self.timestamp)+" "+self.kind+" "+self.resource)

    def doOperation(self):
        print("["+str(self.order)+"] T"+str(self.timestamp)+" "+self.kind+" "+self.resource+" is done successfully")
    
    def failOperation(self):
        print("["+str(self.order)+"] T"+str(self.timestamp)+" "+self.kind+" "+self.resource+" failed. Rolling back...")
        print("")

class Transaction:
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.operations = []

    def insertOperation(self, kind, resource, order):
        op = Operation(self.timestamp, kind, resource, order)
        self.operations.append(op)

    def getTopMostOrderOnly(self):
        if (len(self.operations) > 0):
            return self.operations[0].getOrder()
        else:
            return None

    def getTopMostOperation(self):
        topmost = self.operations.pop(0)
        # print("This is after popping")
        # self.printYgsy()
        return topmost

    def printYgsy(self):
        print("T"+str(self.timestamp))
        for i in self.operations:
            i.printOp()
        print("")

    def isZeroOperation(self):
        if (len(self.operations) == 0):
            return True
        return False