a='Mujeeb Ur Rahman'
b="Mujeeb Ur Rahman"
c='''Mujeeb Ur Rahman'''

print(a)

# String slicing

first_name1 = a[0:6] # (from index, to index) last one will not be included
print(first_name1)

first_name2 = a[:6] # (to index) last one will not be included
print(first_name2)

last_name = a[10:] # (from index) will go to end
print(last_name)

first_name1 = a[-16:-10]
print(first_name1)

# String slicing with skip value


alphabets = "abcdefghijklmnopqrstuvwxyz"
print(alphabets)

print(alphabets[1:6:2]) # (from index, to index, skip value)
print(alphabets[1::3])  # (from index, to end, skip value)
print(alphabets[1::])  # (from index, to index, default skip value 1)