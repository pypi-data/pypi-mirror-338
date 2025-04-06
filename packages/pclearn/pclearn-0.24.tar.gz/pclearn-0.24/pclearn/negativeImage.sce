clc;
close;
a = imread('C:\Users\Admin\Downloads\Doremon.jpg');
k = 255-double(a);
k = uint8(k);
figure(1)
imshow(a);
title('Original Image')
figure(2)
imshow(k);
title('Negative of Original Image')
