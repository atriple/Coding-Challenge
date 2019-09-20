#Environment Variables
MC_MAX = 16
REPAIR_TIME = 5 # Time required to repair a machine
OPERATIONAL_TIME = 10 # Repaired machine operational duration

#Entities specs
class Machine:
    def __init__(self, name, duration):
        self.name = name
        self.global_life_time = duration
        self.operation_duration = duration
        self.repaired = False
        self.data = []
        
    def decreaseLife(self):
        self.operation_duration -= 1

    def setOperationDuration(self, duration, MC):
        self.operation_duration = duration
        self.global_life_time = MC + duration
    
    def isOperational(self):
        return self.operation_duration != 0
    
    def setRepaired(self, val):
        self.repaired = val

    def isRepaired(self):
        return self.repaired
    
    def logData(self):
        if self.isOperational():
            log = str(self.operation_duration) + '/' + str(self.global_life_time)
        else:
            log = 'Break'
        self.data.append(log)

class Repairman:
    def __init__(self, name):
        self.name = name
        self.repair_queue = []
        self.idle = True
        self.global_repair_time = "-"
        self.repair_duration = 0
        self.data_log = []
        self.status_log = []
    
    def enqueue(self, machine):
        self.repair_queue.append(machine)

    def dequeue(self):
        return self.repair_queue.pop(0)

    def doRepair(self, MC):
        global REPAIR_TIME
        if self.idle:
            if len(self.repair_queue) > 0:
                self.global_repair_time = MC + REPAIR_TIME
                self.idle = False
                self.repair_duration += 1

        elif not self.idle:       
            self.repair_duration += 1
    
    def currentMachine(self):
        return self.repair_queue[0]

    def logData(self):
        log = str(self.repair_duration) + '/' + str(self.global_repair_time)
        self.data_log.append(log)

    def logStatus(self):
        if self.idle:
            self.status_log.append("Idle")
        else:
            self.status_log.append("Busy" + "(Repairing " + self.currentMachine().name + ")")
    
    def resetDuration(self):
        self.repair_duration = 0

# Machine Instantiation
CL1 = Machine("CL1", 1)
CL2 = Machine("CL2", 4)
CL3 = Machine("CL3", 9)

machine_list = [CL1, CL2, CL3]

# Repairman as CL4
repairman = Repairman("CL4")

# Simulation
for MC in range(MC_MAX + 1):
    for machine in machine_list:
        machine.logData()
        if machine.isOperational():
            machine.decreaseLife()
        elif not machine.isRepaired():
            machine.setRepaired(True)
            repairman.enqueue(machine)
    
    repairman.doRepair(MC)
    repairman.logData()
    repairman.logStatus()

    # After repairman repaired a machine
    if repairman.repair_duration == 5:
        repairman.idle = True
        repairman.currentMachine().setRepaired(False)
        repairman.currentMachine().setOperationDuration(OPERATIONAL_TIME, MC + 1)
        repairman.dequeue()
        repairman.resetDuration()
    
print(CL1.data)
print(CL2.data)
print(CL3.data)
print(repairman.data_log)
print(repairman.status_log)