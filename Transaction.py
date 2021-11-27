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

class Transaction:
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.transactions = []