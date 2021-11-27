from Simulator.Resource import Resource
from Simulator.Schedule import Schedule

class MVCC:
    def __init__(self, ScheduleString):
        self.sched = Schedule(ScheduleString)
        self.resourceVersions = {}
        for name, resource_obj in self.sched.getResources().items():
            # key is RESOURCE NAME, value is DICT OF RESOURCE  VERSIONS
            # initalize with ver 0
            self.resourceVersions[name] = {0 : resource_obj}

        self.sched.printTransactions()

        for res, versions in self.resourceVersions.items():
            for vernum, resource in versions.items():
                resource.printerNiBhovst()
        
        op = self.sched.getTopMostOp()
        while(op != None):
            #MVCC#
            ver_read, res_to_read = self.getResLatestVersionPossible(op.getResource(), op.getTimestamp())
            if(op.getKind() == 'READ'):
                op.doOperation()
                if(res_to_read.getRTS() < op.getTimestamp()):
                    print("Setting new RTS...")
                    res_to_read.setRTS(op.getTimestamp())
                    res_to_read.printerNiBhovst()
                else:
                    print("RTS remains the same.")
                    res_to_read.printerNiBhovst()
                
            else: # op.getKind() == 'WRITE'
                if(op.getTimestamp() < res_to_read.getRTS()):
                    op.failOperation()
                elif(op.getTimestamp() == res_to_read.getWTS()):
                    op.doOperation()
                    print("Overwriting contents of "+res_to_read.getName()+" version: "+str(ver_read))
                else: #Create new version
                    op.doOperation()
                    print("Creating new version...")
                    newVer = Resource(res_to_read.getName())
                    newVer.setRTS(op.getTimestamp())
                    newVer.setWTS(op.getTimestamp())
                    self.resourceVersions[res_to_read.getName()][op.getTimestamp()] = newVer

                    # print all versions of newly updated particular resource
                    print("All versions of "+res_to_read.getName())
                    for ver, resobj in self.resourceVersions[res_to_read.getName()].items():
                        resobj.printerNiBhovst()

            #MVCC#
            op = self.sched.getTopMostOp()
    
    def getResLatestVersionPossible(self, resource, timestamp):
        verToRet = 0
        for ver, resobj in self.resourceVersions[resource].items():
            if(verToRet < ver and ver <= timestamp):
                verToRet = ver

        return verToRet, self.resourceVersions[resource][verToRet]

MVCC("5-READ-X,2-READ-Y,1-READ-Y,3-WRITE-Y,3-WRITE-Z,5-READ-Z,2-READ-Z,1-READ-X,4-READ-W,3-WRITE-W,5-WRITE-Y,5-WRITE-Z")