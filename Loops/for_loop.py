# range(start, stop, step_size)

for i in range(1, 5):
    print(i)

list = ["Mujeeb", "Ali", "Ahmed", "Farhan", False, 1, 23.4, None]

for item in list:
    print(item)

s = "Mujeeb"

for char in s:
    print(char)
else:
    print("Empty Character")

i=0

for i in range(5):
    if i == 3:
        break
    print(i)

i=0

for i in range(5):
    if i == 3:
        continue
    print(i)