#Ex2


def fibon (n):
    a, b = 0, 1
    for i in range(1, n):
        print(a, end=" ")
        a, b = b, a + b


print ("the fifth value:", fibon(5))
print ("the tenth value:", fibon(10))
print("the finfteenth value: ", fibon(15))


'''    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
        # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibon(n - 1) + fibon(n - 2)'''