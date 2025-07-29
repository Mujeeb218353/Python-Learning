n = int(input("Enter a number: "))
i=n-1
isPrime = False
while i > 1:
    if n%i == 0:
        isPrime = False
        break
    else:
        isPrime = True
    i -= 1

if isPrime:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")