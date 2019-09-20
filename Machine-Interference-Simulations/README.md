Simple program example from Computer Simulation Techniques (College Assignment)

## Environment Variables
Here's parameter that you can dynamically setups:
- Number of Machine
- How long the simulation will be
- Repair and Operational Times

## How things Work
- Clock based simulation (using Master Clock, it will iterate the process counting from 0)
- Repair system using Queue data structures (FIFO rule)

### Event Logging
The simulation will track given events :
- When a machine breaks
- When the repairman succesfully repair the machine

### Views
This program can show :
- Detailed view, it will show every MC iteration
- Event only view, it will only show row when certain event happen 

I think I can also show more details better than what's given in the book :
- Two way of time representation
    - Local Time for each machine
    - Referencing towards MC (The Global Time)
    - The information displayed as (LocalTime / GlobalTime), for ex : (4/10)