name = "Harry"
string = input("Enter a string: ")

name = name.lower().strip()
string = string.lower().strip()

if name in string:
    print("This post is talking about", name.capitalize())
else:
    print("This post isn't talking about", name.capitalize())