#EX3

def fibon (n):
    i1=0
    i2=1
    summ=0
    count=0
    for number in range ( 0 , n+1):
        if number < 0:
            print("Incorrect input")
            # First Fibonacci number is 0
        elif number == 0:
            summ=0
        elif number == 1:
            summ=summ+1
            # Second Fibonacci number is 1
        else:
            count=i1 + i2
            i1=i2
            i2=count
            summ=summ + count
    return summ

print("the sum of the first 5 terms of the fibonacci series:", fibon(5) )
print("the sum of the first 10 terms of the fibonacci series:", fibon(10) )