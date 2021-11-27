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
        """
        print(ScheduleString)