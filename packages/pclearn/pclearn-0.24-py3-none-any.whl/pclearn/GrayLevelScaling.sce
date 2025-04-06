clc ;
x = imread("C:\Users\Admin\Downloads\shinchan.jpg");
x = rgb2gray(x);
y = double(x);
[m,n]= size(y);
L = max(max(x));
a = round(L/2) ;
b = L;
for i =1: m
 for j =1: n
 if(y(i,j)>=a & y(i,j)<=b)
 z(i,j) = L;
 else
 z(i,j)=0;
 end
 end
end
z = uint8(z);
figure(1)
imshow(x);
title('Original Image')
figure(2)
imshow(z);
title('Gray Level Slicing without preserving background')
