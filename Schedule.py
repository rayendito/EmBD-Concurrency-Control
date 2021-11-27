from Transaction import Transaction

class Schedule:
    def __init__(self, ScheduleString):
        """
        Format of TransactionString: timestamp-operation-resource
        operation name written in all caps and not disingkat (singkat bahasa inggrisnya apa kwoakwo)
        Example:
        5-READ-X

        Multiple operations from different transactions are separated by commas
        Example :
        5-READ-X,2-READ-Y,1-READ-Y,3-WRITE-Z

        Contoh full schedule dari video kuliah MBD
        https://www.youtube.com/watch?v=AlrmbPO7Ovc&list=PLRdh21P3pZqvKMHZoWbyXOnIjnoT63NPK&index=1&t=342s

        5-READ-X,2-READ-Y,1-READ-Y,3-WRITE-Y,3-WRITE-Z,5-READ-Z,2-READ-Z,1-READ-X,4-READ-W,3-WRITE-W,5-WRITE-Y,5-WRITE-Z
        """
        # ATTRIBUTES
        self.resources = []
        self.transactions = {}

        # IDENTIFY TRANSACTIONS AND RESOURCES
        regdTrans = [] # catat trans yg udah dibuat obj nya
        regdResourc = [] # catat resource yg udah dibuat obj nya

        splitToOperations = ScheduleString.split(',')
        for i in range(len(splitToOperations)):
            splitToOperations[i] = splitToOperations[i].split('-')

            # create transaction and register operation if transaction obj hasnt been made
            timestamp = int(splitToOperations[i][0])
            if(timestamp not in regdTrans):
                # create
                tr = Transaction(timestamp)
                self.transactions[timestamp] = tr

                # add
                self.transactions[timestamp].insertOperation(splitToOperations[i][1], splitToOperations[i][2], i) # kind, resource, order
                self.transactions[timestamp].printYgsy()

                # add to registered
                regdTrans.append(timestamp)

        print("akwokawokaw")



if __name__ == "__main__":
    Schedule("5-READ-X,2-READ-Y,1-READ-Y,3-WRITE-Y,3-WRITE-Z,5-READ-Z,2-READ-Z,1-READ-X,4-READ-W,3-WRITE-W,5-WRITE-Y,5-WRITE-Z")

