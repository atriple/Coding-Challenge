%Matsort function digunakan untuk soal Bab 12 No 21
function output = matsort(X)
% Sort Matrix for any size n x m
% X -- argument in matrix type
    X_size = size(X);
    X_list = reshape(X, 1, X_size(1) * X_size(2));
    output = reshape(sort(X_list), X_size(1), X_size(2));
end
