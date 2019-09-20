# Assignment 01 : The machine interference problem

Simple program example from Computer Simulation Techniques Books. We use **Python** to implement the simulation program.

First, set up the environment variables, this will be parameter that you can change on the simulations.

```python
# ENVIRONMENT VARIABLES

MC_MAX = 16
REPAIR_TIME = 5 # Time required to repair a machine
OPERATIONAL_TIME = 10 # Repaired machine operational duration
```

## Entities Specifications
In the system, we found that there are two main entities :
- The Machine
- The Repairman

Under some design assumptions :
- Repair system using Queue data structures (FIFO rule)
- The system will be based on the clock, we representate the clock in two ways :
    - Globally using MC (Master Clock)
    - Locally, each instance has their own local duration
    - Later in the table results, you will see the data in form of (Local/Global), example : (3/5)

```python
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
```

## Instantiation
We will follow the number of machine according the book, we can actually instantiate the machine according the number that we want.


```python
# Machine Instantiation
CL1 = Machine("CL1", 1)
CL2 = Machine("CL2", 4)
CL3 = Machine("CL3", 9)

machine_list = [CL1, CL2, CL3]

# Repairman as CL4
repairman = Repairman("CL4")

# Event Log
event_log = []
```

## Running The Simulation
Clock based simulation, so we can implement looping for the process, it will run the event in MC_MAX time(s)


```python
for MC in range(MC_MAX + 1):
    for machine in machine_list:
        machine.logData()
        if machine.isOperational():
            machine.decreaseLife()
        elif not machine.isRepaired():
            machine.setRepaired(True)
            repairman.enqueue(machine)
            event_log.append([MC, machine.name + " break"])
    
    repairman.doRepair(MC)
    repairman.logData()
    repairman.logStatus()

    # After repairman repaired a machine
    if repairman.repair_duration == 5:
        event_log.append([MC, repairman.currentMachine().name + " repaired"])
        repairman.idle = True
        repairman.currentMachine().setRepaired(False)
        repairman.currentMachine().setOperationDuration(OPERATIONAL_TIME, MC + 1)
        repairman.dequeue()
        repairman.resetDuration()
```

## Results


```python
print(CL1.data)
print(CL2.data)
print(CL3.data)
print(repairman.data_log)
print(repairman.status_log)
print(event_log)
```
### Outputs

    ['1/1', 'Break', 'Break', 'Break', 'Break', 'Break', '10/16', '9/16', '8/16', '7/16', '6/16', '5/16', '4/16', '3/16', '2/16', '1/16', 'Break']
    ['4/4', '3/4', '2/4', '1/4', 'Break', 'Break', 'Break', 'Break', 'Break', 'Break', 'Break', '10/21', '9/21', '8/21', '7/21', '6/21', '5/21']
    ['9/9', '8/9', '7/9', '6/9', '5/9', '4/9', '3/9', '2/9', '1/9', 'Break', 'Break', 'Break', 'Break', 'Break', 'Break', 'Break', '10/26']
    ['0/-', '1/6', '2/6', '3/6', '4/6', '5/6', '1/11', '2/11', '3/11', '4/11', '5/11', '1/16', '2/16', '3/16', '4/16', '5/16', '1/21']
    ['Idle', 'Busy(Repairing CL1)', 'Busy(Repairing CL1)', 'Busy(Repairing CL1)', 'Busy(Repairing CL1)', 'Busy(Repairing CL1)', 'Busy(Repairing CL2)', 'Busy(Repairing CL2)', 'Busy(Repairing CL2)', 'Busy(Repairing CL2)', 'Busy(Repairing CL2)', 'Busy(Repairing CL3)', 'Busy(Repairing CL3)', 'Busy(Repairing CL3)', 'Busy(Repairing CL3)', 'Busy(Repairing CL3)', 'Busy(Repairing CL1)']
    [[1, 'CL1 break'], [4, 'CL2 break'], [5, 'CL1 repaired'], [9, 'CL3 break'], [10, 'CL2 repaired'], [15, 'CL3 repaired'], [16, 'CL1 break']]
    

### Beautifying using Pandas Dataframe Library


```python
import pandas as pd

dict = {
    "CL1" : CL1.data, 
    "CL2" : CL2.data, 
    "CL3" : CL3.data, 
    "CL4" : repairman.data_log, 
    "Repairman Status" : repairman.status_log
}

table = pd.DataFrame(dict)
print(table)
```

          CL1    CL2    CL3   CL4     Repairman Status
    0     1/1    4/4    9/9   0/-                 Idle
    1   Break    3/4    8/9   1/6  Busy(Repairing CL1)
    2   Break    2/4    7/9   2/6  Busy(Repairing CL1)
    3   Break    1/4    6/9   3/6  Busy(Repairing CL1)
    4   Break  Break    5/9   4/6  Busy(Repairing CL1)
    5   Break  Break    4/9   5/6  Busy(Repairing CL1)
    6   10/16  Break    3/9  1/11  Busy(Repairing CL2)
    7    9/16  Break    2/9  2/11  Busy(Repairing CL2)
    8    8/16  Break    1/9  3/11  Busy(Repairing CL2)
    9    7/16  Break  Break  4/11  Busy(Repairing CL2)
    10   6/16  Break  Break  5/11  Busy(Repairing CL2)
    11   5/16  10/21  Break  1/16  Busy(Repairing CL3)
    12   4/16   9/21  Break  2/16  Busy(Repairing CL3)
    13   3/16   8/21  Break  3/16  Busy(Repairing CL3)
    14   2/16   7/21  Break  4/16  Busy(Repairing CL3)
    15   1/16   6/21  Break  5/16  Busy(Repairing CL3)
    16  Break   5/21  10/26  1/21  Busy(Repairing CL1)
    
### Filtering the table based on event that happen

```python
# Filtering Events
print(table.iloc[[0] + [row[0] for row in event_log]])
```

          CL1    CL2    CL3   CL4     Repairman Status
    0     1/1    4/4    9/9   0/-                 Idle
    1   Break    3/4    8/9   1/6  Busy(Repairing CL1)
    4   Break  Break    5/9   4/6  Busy(Repairing CL1)
    6   10/16  Break    3/9  1/11  Busy(Repairing CL2)
    9    7/16  Break  Break  4/11  Busy(Repairing CL2)
    11   5/16  10/21  Break  1/16  Busy(Repairing CL3)
    16  Break   5/21  10/26  1/21  Busy(Repairing CL1)
    