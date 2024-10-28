age = int(input("Enter your age: "))

if  0 <= age < 18:
    print("You are a teenager")
elif 18 <= age < 65:
    print("Adult")
elif age >= 65:
    print("Old Age")
else:
    print("Invalid Age")