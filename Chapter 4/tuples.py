a = (1, 2, 5, 8)
print(type(a))
print(a)

b = (1) # int
print(type(b))

b = (1,)
print(type(b))

c= a.count(8)
print(c)

print(a)

print(a.index(8))

d = a + b # concat tuple
print(d)

print(len(d))

e = d[1:3] # return new tuple
print(e)

