from Simulator.Schedule import Schedule

class MVCC:
    def __init__(self, ScheduleString):
        self.sched = Schedule(ScheduleString)
        self.resourceVersions = {}
        for name, resource_obj in self.sched.getResources().items():
            # name as key, value as ARRAY OF RESOURCE OBJECT, index indicating version
            self.resourceVersions[name] = [resource_obj]

        self.sched.printTransactions()
        
        ops = self.sched.getTopMostOp()
        while(ops != None):
            ops.printOp()
            ops = self.sched.getTopMostOp()

MVCC("5-READ-X,2-READ-Y,1-READ-Y,3-WRITE-Y,3-WRITE-Z,5-READ-Z,2-READ-Z,1-READ-X,4-READ-W,3-WRITE-W,5-WRITE-Y,5-WRITE-Z")
# MVCC("5-READ-X")