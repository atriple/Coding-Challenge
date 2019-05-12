clear
clc

A = imread('flower','jpg');

maximum = max(max(max(A)))
minimum = min(min(min(A)))

