close;
clear;
clc;
x=[65,75,80,70;72,75,82,68;84,72,62,65;66,68,72,80];
disp(x,"Original Block is x = " );
[ m1 n1 ] = size(x);
blk = input("Enter the block size: ");
for i = 1:blk:m1
 for j = 1:blk:n1
 y = x(i:i+(blk-1),j:j+(blk -1));
 m = mean(mean(y));
 disp(m,"mean value is m = ");
 sig = stdev(y);
 disp(sig,"Standard deviation of the block is = ");
 b = y>m;
 disp(b,"Binary allocation matrix is B= ");
 K = sum(sum(b));
 disp(K,"number of ones = ");
 if(K~=blk^2)&( K~=0)
 ml = m-sig*sqrt(K/((blk^2)-K));
 disp(ml,"The value of a = ");
 mu = m+sig*sqrt(((blk^2)-K)/K);
 disp(mu,"The value of b = ");
 x(i:i+(blk-1),j:j+(blk-1))=b*mu+(1-b)*ml;
 end
 end
end
disp(round(x),"Reconstructed Block is x = " );
