I1 =imread('flower.jpg');  %Mengkonversi gambar ke bentuk matrix
[rc,h] = size(I1); %Mengambil size dari matrix
Inew(:,:,:) = I1(:,rc:-1:1,:); %Mereverse image dengan mengkonstruksi matriks dari belakang

% Melakukan Plotting

% Menggunakan Image biasa
% figure(1) 
% subplot(2,1,1) 
% image(I1); 
% subplot(2,1,2) 
% image(Inew);

% Menggunakan imshow
subplot(1,2,1), imshow(I1)
title('Original Image')
subplot(1,2,2), imshow(Inew)
title('Reversed Image')