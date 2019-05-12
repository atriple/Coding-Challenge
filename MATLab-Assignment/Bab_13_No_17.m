clear
clc

orig = randi([0, 255], 4)
fin = orig + randi([-10,10],4)

mean(mean(orig))
mean(mean(fin))