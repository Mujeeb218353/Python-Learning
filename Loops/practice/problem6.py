n = int(input("Enter a number you want to find the factorial of: "))

factorial = 1

for i in range(1, n+1):
    factorial *= i

print("The factorial of", n, "is:", factorial)