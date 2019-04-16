# Simulation fair coin toss
from random import randint
import numpy as np

# Head as 0, Tail as 1
count = 0
count_head = 0
prob_head = []
# Iterate 10 times (the more, the better)
for x in range(0,10):
    toss_value = randint(0,1)
    if toss_value == 0:
        count_head = count_head + 1
    count = count + 1
    probability = count_head / count
    prob_head.append(probability)

np_prob_head = np.array(prob_head)
np_prob_tail = 1 - np_prob_head

print(prob_head)
print(type(np_prob_head))
print(np_prob_head)
print(np_prob_tail)