username = input("Enter username: ")

if len(username) < 10:
    print("Username contains less than 10 characters")
elif len(username) > 10:
    print("Username contains more than 10 characters")
elif len(username) == 10:
    print("Username contains exactly 10 characters")
else:
    print("Invalid username")