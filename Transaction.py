from Resource import Resource

class Operation:
    def __init__(self, kind, resource, order):
        self.kind = kind
        self.resource = resource
        self.order = order
    
    def getKind(self):
        return self.kind
    
    def getOrder(self):
        return self.order
    
    def printOp(self):
        print("Ini kind ane",self.kind)
        print("Ini resource ane",self.resource)
        print("Ini order ane",self.order)
        print("")

class Transaction:
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.operations = []

    def insertOperation(self, kind, resource, order):
        op = Operation(kind, resource, order)
        self.operations.append(op)

    def printYgsy(self):
        print("Ini timestamp ane",self.timestamp)
        for i in self.operations:
            i.printOp()