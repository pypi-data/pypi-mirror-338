clc;
x=[4,5,6;7,8,9];
h=[1;1;1];
disp(x,"x=");
disp(h,"h=");
y=conv2(x,h);
disp(y, '2D Linear Convolution result: y =' );
