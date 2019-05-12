x= 1:4
y= [2, 5, 6, 10] 
coefs2 = polyfit(x,y,1); 
coefs2 = polyfit(x,y,2); 
curve1 = polyval(coefs1,x); 
curve2 = polyval(coefs2,x);
plot(x,y,'ro',x,curve1)
plot(x,y,'ro',x,curve2)


