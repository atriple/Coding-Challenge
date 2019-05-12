% Function untuk soal Bab 12 No 22
function sorted_vector = vectsort(vect, direction)
% Function to sort a vector
% vect -- input argument in vector/list type
% direction -- option argument, 'a' for ascending, 'd' for descending

if direction == 'a'
    sorted_vector = sort(vect, 'ascend');
elseif direction == 'd'
    sorted_vector = sort(vect, 'descend');
end

end