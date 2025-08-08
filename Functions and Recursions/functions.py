a = 1
b = 2
c = 3

average = (a + b + c)/3
print(average)

def average(a, b, c):
    return (a + b + c)/3

print(average(1, 3, 5))

def greet(name = "Guest"): # (parameters)
    print(f"Hello, {name} have a nice day!")

greet("Mujeeb") # (arguments)