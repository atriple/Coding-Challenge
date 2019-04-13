#This one is for number-type, nothing different in the algorithm
from random import shuffle

# Creating list
x = list(range(1,37)) #generate list of number from 1 to 36 (you can change this)
#removing certain element is also possible if you want to...

num_of_group = int(input("Input > Number of Group(s) : "))
num_of_members = int(len(x)/num_of_group)
print(num_of_members) #dbg

shuffle(x)
the_groups = []
group = []
for j in range(0, num_of_group):
    for k in range(0,num_of_members):
        group.append(x.pop())
    the_groups.append(group)
    group = []

#dbg
print(the_groups)
print(x)

# Mengassign sisanya, pasti hanya sekali looping karena sisanya jelas akan kurang dari 1 grup penuh
index = 0
for x in x:
    the_groups[index].append(x)
    index = index + 1

print("Final results : {}".format(the_groups))