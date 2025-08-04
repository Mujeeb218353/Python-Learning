n = int(input("Enter a number to print pattern: "))

for i in range(1, n+1):
    line = ""
    for j in range(1, n+1):
        if i == 1 or i == n or j ==1 or j==n:
            line += "*"
        else:
            line += " "
    print(line)

'''
*****
*   *
*   *
*   *
*****

n=5
'''

for i in range(1, n+1):
    line = ""
    for j in range(1, n+1):
        if i == 1 or i == n or j ==1 or j==n:
            line += "* "
        else:
            line += "  "
    print(line)

''''
**********
*        *
*        *
*        *
**********
n=10
'''