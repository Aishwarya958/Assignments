# Produce result as 120 from only five 0's using any arithmentic operations

num1 = ~0
num2 = ~0
num3 = ~0
num4 = ~0
num5 = ~0

num = num1 + num2  + num3 + num4 + num4

def factorial(num):
    '''Finds Factorial '''
    factorial = 1

    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
           factorial = factorial*i
        print("Result"factorial)

factorial(abs(num))
