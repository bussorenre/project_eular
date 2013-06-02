x = y = 1
sum = 0
while(x < 4000000 ):
	sum += (x+y)
	y = 2*x + y 
	x = 3*x + 2*y

print sum