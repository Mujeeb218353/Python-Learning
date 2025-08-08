n = int(input("Enter a number to print pattern: "))

for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))
    print()

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(" ", end="")
#     for k in range(1, i+1):
#         print("*", end="")
#     for l in range(1, i):
#         print("*", end="")
#     print()

# for i in range(1, n+1):
#     line = ""
#     for j in range(n-i):
#         line += " "
#     for k in range(2*i-1):
#         line += "*"
#     print(line)

# '''
#    *      i=1, 5 space, 1 star
#   ***     i=2, 4 space, 3 star
#  *****    i=3, 3 space, 5 star
# *******   i=4, 2 space, 7 star
#*********  i=5, 1 space, 9 star
# n=5

# *      i=1, 5 space, 1 star
#***     i=2, 4 space, 3 star
# n=2

#  *      i=1, 5 space, 1 star
# ***     i=2, 4 space, 3 star
#*****    i=3, 3 space, 5 star
# n=3
# '''