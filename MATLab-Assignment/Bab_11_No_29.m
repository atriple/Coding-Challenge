clear
clc

A = [
    4, -1, 0, 3;
    -2, 3, 1, -5;
    1, 1, -1, 2;
    3, 2, -4, 0;
    ]
b = [10, -3, 2, 4]'

% penyelesaian dengan menggunakan solve
syms x1 x2 x3 x4
col_x1 = x1 * A(:,1)
col_x2 = x2 * A(:,2)
col_x3 = x3 * A(:,3)
col_x4 = x4 * A(:,4)
alg_v = col_x1 + col_x2 + col_x3 + col_x4
fprintf('Hasil:')
[Sx1, Sx2, Sx3, Sx4]  = solve(alg_v(1) == b(1), alg_v(2) == b(2), alg_v(3) == b(3), alg_v(4) == b(4))

% penyelesaian dengan menggunakan metode lain
c = [A b]
rref(c)
% x1 = 2.5581, x2 = 0.4419, x3 = 1.1395, x4 = 0.0698, jika dihitung sama

