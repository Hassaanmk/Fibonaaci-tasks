def fib(n): 
    a, b = 0, 1 
    while a < n: 
        yield a 
        a, b = b, a + b 
 
# Print all the fibonacci sequence up to 10000  
for n in fib(10000): 
	print(n) 