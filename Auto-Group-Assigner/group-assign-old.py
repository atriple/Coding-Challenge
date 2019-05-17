# Use v1b instead of this!
from random import shuffle
import csv

results = []
with open("test.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: # each row is a list
        results.append(row)

listLength = len(results)
print("Total member(s) : " + str(listLength))
numberOfGroup = int(input("Jumlah grup : "))

# Lower Bound and Upper Bound to distribute members.
try :
    DIFF = int(listLength/numberOfGroup)
except :
    print("ERROR : INVALID VALUE !")
else :
    if DIFF < 1:
        print("Tidak bisa memproses value ini, kemungkinan jumlah grup lebih dari total member")
        raise ValueError('ERROR VALUE')
finally :
    low = 0
    up = DIFF
    print (up) #Hanya sekedar debug.
    print (low) #Hanya sekedar debug.

shuffle(results) #shuffle/randomize list sebelum di alokasi

x = numberOfGroup
while True:
    group = results[low:up]
    low = low + DIFF
    up = up + DIFF
    print(group)
    x = x - 1
    if x == 0:
        break