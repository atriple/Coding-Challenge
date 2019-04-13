# By acessing txt files, not csv
from random import shuffle

results = []
with open("test.txt") as nama:
    results = nama.readlines()

new_results = []
for i in results :
    i = i.strip() #remove the \n
    new_results.append(i)

#input how many group to divide
num_of_group = int(input("Input > Number of Group(s) : "))
num_of_members = int(len(new_results)/num_of_group)
print(num_of_members) #dbg

shuffle(new_results)
the_groups = []
group = []
for j in range(0, num_of_group):
    for k in range(0,num_of_members):
        group.append(new_results.pop())
    the_groups.append(group)
    group = []

#dbg
print(the_groups)
print(new_results)

# Mengassign sisanya, pasti hanya sekali looping karena sisanya jelas akan kurang dari 1 grup penuh
index = 0
for x in new_results:
    the_groups[index].append(x)
    index = index + 1

print("Final results : {}".format(the_groups))