clc;
close;
a=imread('C:\Users\Admin\Downloads\white-flower.jpg');
a=rgb2gray(a);
b=double(a)+50;
b=uint8(b);
figure(1);
imshow(a);
title("Original Image")
figure(2);
imshow(b);
title("Enhanced Image")
