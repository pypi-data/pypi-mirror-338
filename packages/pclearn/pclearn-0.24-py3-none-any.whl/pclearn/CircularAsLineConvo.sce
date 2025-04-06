clc ;
x =[1,2;3,4];
h=[5,6;7,8];
y=conv2(x,h);
y1=[y(:,1)+y(:,$),y(:,2) ];
y2=[y1(1,:)+y1($,:);y1(2,:)];
disp(y, 'Linear Convolution Result: y=');
disp(y2 , 'Circular Convolution expressed as Linear Convolution =' );
