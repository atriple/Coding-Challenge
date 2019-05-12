clear
clc

image = imread('flower.jpg');
new1 = image + 100;
new2 = image - 100;
random = uint8(randi(100,size(image)))
new3 = image + random;


subplot(2,2,1), imshow(image)
title('Original Image')
subplot(2,2,2), imshow(new1)
title('Uniform +100')
subplot(2,2,3), imshow(new2)
title('Uniform -100')
subplot(2,2,4), imshow(new3)
title('Random(1-100)')