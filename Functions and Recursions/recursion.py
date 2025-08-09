def factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers"
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
    
n = 5
print(f"The factorial of {n} is {factorial(n)}")