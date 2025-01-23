# Assignment Operators
a1 = 5
a1 +=5

print(a1)

# Arithmetic Operators
a = 3+2
b = 3-2
c = 3*2
d = 3/2
e = 5%2
f = 15//2 # Integer Division
g = 3**2

# print(f)

# Comparison Operators
h = (3 == 2)  # False
i = (3 != 2)  # True
j = (3 > 2)  # True
k = (3 < 2)  # False
l = (3 >= 2)  # True
m = (3 <= 2)  # False

# Logical Operators

n = True and True  # True
o = True or False  # True
r = not True  # False
a=10
b=12
# Bitwise Operators
s = a & b  # Bitwise AND 
t = a | b  # Bitwise OR 
u = a ^ b  # Bitwise XOR
v = ~a  # Bitwise NOT
w = a >> 1  # Right Shift
x = a << 2  # Left Shift

print("AND:",s, "\nOR:",t, "\nXOR:",u, "\nNOT:",v, "\nRight Shift:", w, "\nLeft Shift:",x)

# Unary Operators
y = -a1  # Negation
z = +a1  # Positive

print(y, z)

# Identity Operators

x=10
y=10
print(x is y)
print(x is not y)