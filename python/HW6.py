# 1.

# Use loop and recursive function calls to implement factorial functions.
#  For recursive calls, print a line when each function is initialized and 
#  another line before exit. Use time module to measure the running time of
#   those two functions.

# Examples: Factorial(5)=120

# When use recursive function calls, and enter Factorial(5), 
# print "Entering Factorial(5)...". Just before return from Factorial(5), 
# print "Exiting Factorial(5)..."
import time
def Factorial(number):
    product=1
    for i in range(1,number+1):
        product=product*i
    return product
start_time=time.time()
print(Factorial(10))
print(time.time()-start_time)
start_time=time.time()
print(Factorial(20))
print(time.time()-start_time)
start_time=time.time()
print(Factorial(30))
print(time.time()-start_time)

#2 answer
def Fibonacci(number):
    fib=[1,1]
    for i in range(2,number):
            sum=fib[i-1]+fib[i-2]
            fib.append(sum)  
    return fib[number-1]
    sum=1
    for i in range(number+1):
        if i==1:
            fib=1
        elif i==2:
            fib=1
        elif i>2: 
            sum+=fib
            fib=sum
            print(fib)
            return(sum)
start_time=time.time()
print(Fibonacci(10))
print(time.time()-start_time)
start_time=time.time()
print(Fibonacci(20))
print(time.time()-start_time)
start_time=time.time()
print(Fibonacci(30))
print(time.time()-start_time)


