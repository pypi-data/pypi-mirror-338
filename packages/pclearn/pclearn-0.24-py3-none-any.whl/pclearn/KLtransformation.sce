clear;
clc;
X=[4,3,5,6;4,2,7,7;5,5,6,7];
[m,n]=size(X);
A=[];
E=[];
for i=1:n
 A=A+X(:,i);
 E=E+X(:,i)*X(:,i)';
end
mx=A/n;
E=E/n;
C=E-mx*mx';
[V,D]=spec(C);
d=diag(D);
[d,i]=gsort(d);
for j=1: length(d)
 T(:,j)=V(:,i(j));
end
T=T'
disp(d,'Eigen Values are U= ')
disp(T,'The eigen vector matrix T=')
disp(T,'The KL transform basis is=')
for i=1:n
 Y(:,i)=T*X(:,i);
end
disp(Y,'KL transformation of the input matrix Y=')
for i=1:n
 x(:,i)=T*Y(:,i);
end
disp(x,'Reconstruct matrix of the given sample matrix X= ')
