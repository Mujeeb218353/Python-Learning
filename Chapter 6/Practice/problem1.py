list = []

a1 = int(input("Enter a number 1:"))
a2 = int(input("Enter a number 2:"))
a3 = int(input("Enter a number 3:"))
a4 = int(input("Enter a number 4:"))

if a1 > a2 and a1 > a3 and a1 > a4:
    print("Max number is a1:", a1)
elif a2 > a1 and a2 > a3 and a2 > a4:
    print("Max number is a2:", a2)
elif a3 > a1 and a3 > a2 and a3 > a4:
    print("Max number is a3:", a4)
elif a4 > a1 and a4 > a2 and a4 > a3:
    print("Max number is a4:", a4)
else:
    print("Enter a valid numbers!")