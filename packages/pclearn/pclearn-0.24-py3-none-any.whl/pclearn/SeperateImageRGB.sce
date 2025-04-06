clc;
close ;
RGB = imread('C:\Users\Admin\Downloads\car.jpg');
R = RGB;
G = RGB;
B = RGB;
R(: ,: ,1) =0;
G(: ,: ,2) =0;
B(: ,: ,3) =0;
figure(1)
imshow(RGB);
title('Original Color Image');
figure(2)
imshow(R);
title('Red Component Missing');
figure(3)
imshow(G);
title('Green Component Missing');
figure(4)
imshow(B);
title('Blue Component Missing')
