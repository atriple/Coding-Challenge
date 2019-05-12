x= 1:7
y= [1.1, 1.9, 3.3, 3.4, 3.1, 3.3, 7.1] 
coefs = polyfit(x,y,1); 
curve = polyval(coefs,x); 
plot(x,y,'ro',x,curve) 
xlabel('Time') 
ylabel('Voltage')
axis([0 8 0 10])


