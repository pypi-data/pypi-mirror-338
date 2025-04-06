clc;
close ;
RGB = imread('C:\Users\Admin\Downloads\car.jpg');
R = RGB;
G = RGB;
B = RGB;
R(: ,: ,2) =0;
R(: ,: ,3) =0;
G(: ,: ,1) =0;
G(: ,: ,3) =0;
B(: ,: ,1) =0;
B(: ,: ,2) =0;
figure(1)
imshow(RGB);
title('Original Color Image');
figure(2)
imshow(R);
title('Red Component');
figure(3)
imshow(G);
title('Green Component');
figure(4)
imshow(B);
title('Blue Component')
