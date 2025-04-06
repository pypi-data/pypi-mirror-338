clc;
x = [3,1;2,4];
h1 = [1,5;2,3];
h2 = h1(:,$:-1:1);
h = h2($:-1:1,:);
y = conv2(x,h)
disp(y, 'Linear cross Correlation result y=')
