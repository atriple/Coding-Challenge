from random import shuffle

x = list(range(1,37)) #generate list of number from 1 to 36 (you can change this)
print("Initial : {}".format(x))
shuffle(x) #randomize x list
print('Randomized : {}'.format(x))

n = 