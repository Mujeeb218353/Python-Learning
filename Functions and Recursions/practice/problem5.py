def print_pattern(n):
    for i in range(n):
        print("*" * (n-i))

print_pattern(5)

def print_pattern_recursion(n):
    if n == 0:
        return
    print("*" * n)
    print_pattern_recursion(n-1)

print_pattern_recursion(10)