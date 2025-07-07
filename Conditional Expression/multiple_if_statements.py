a = int(input("Enter first number: "))

if a%2 == 0:
    print("You entered an even number.")
else:
    print("You entered an odd number.")

if a >= 18:
    print("You are an adult.")
elif a <= 0:
    print("Invalid age.")
else:
    print("You are a minor.")