clc;
x = [1,5;2,4];
h = [3,2;4,1];
h = h(:,$:-1:1);
h = h($:-1:1,:);
X = fft2(x);
H = fft2(h);
Y = X.*H;
y = ifft(Y);
disp(y,'Circular Correlation result y=')
