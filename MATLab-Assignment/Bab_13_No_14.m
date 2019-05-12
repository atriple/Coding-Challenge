A = double(imread('flower','jpg'));
%B = imread('cat','png');

red_mean = mean(mean(A(:,:,1)))
green_mean = mean(mean(A(:,:,2)))
blue_mean = mean(mean(A(:,:,3)))

mean_color = [red_mean, green_mean, blue_mean]
%image(mean_color) %rata-ratanya jika dikombinasi akan berwarna kuning

red_std = std(std(A(:,:,1)))
green_std = std(std(A(:,:,2)))
blue_std = std(std(A(:,:,3)))
color_std = [red_std, green_std, blue_std]

