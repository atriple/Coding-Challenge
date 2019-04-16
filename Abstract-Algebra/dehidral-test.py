import numpy as np

index = [1, 2, 3, 4]
number = "1 2 3 4"
permut = number.split()

def rotate(A) : #there is actually rotate 
    A.append(A.pop(0))
    return A

array = np.array([index, permut])
print(array)