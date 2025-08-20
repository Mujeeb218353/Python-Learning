f = open("file_functions.txt", )

# print(f.read())
# print(f.readline())
print(f.readlines())

print()

line = f.readline()
while line != "":
    print(line)
    line = f.readline()



f.close()

