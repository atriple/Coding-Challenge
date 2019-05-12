clear
clc

A = [2, 2, 1; 0, 1, 2; 1, 1, 3]
b = [2; 1; 3]

C = [A b] % penyelesaian untuk Gauss
D = [A b] % penyelesaian untuk Gauss-Jordan

% Penyelesaian dengan fungsi rref
rref(C)
% 

% Penyelesaian manual dengan OBE

%Solve using Gauss
fprintf('Penyelesaian dengan Gauss:')
% Row Operations:
C(1,:) = C(1,:) / 2
C(3,:) = C(3,:) - C(1,:) 
C(3,:) = C(3,:) / 2.5 

%didapat hasilnya dengan back substitution:
x3 = 0.8
x2 = 1 - 2*x3
x1 = 1 - x2 - 0.5*x3

% Solve Using Gauss Jordan
fprintf('Penyelesaian dengan Gauss-Jordan:')
% Row Operations :
D(1,:) = D(1,:) / 2
D(3,:) = D(3,:) - D(1,:) 
D(3,:) = D(3,:) / 2.5 
D(1,:) = D(1,:) - 0.5*D(3,:)
D(2,:) = D(2,:) - 2*D(3,:)
D(1,:) = D(1,:) - D(2,:)
fprintf('Hasil dari Gauss-Jordan:')
gj_x1 = D(1,4)
gj_x2 = D(2,4)
gj_x3 = D(3,4)

%Using Inverse of Matrix
inverse_A = inv(A)
sol = inverse_A * b
