name = ["Mujeeb Ur Rahman", "Farhan", "Huzaifa", "Yousuf"]

user_input = input("Enter name: ")

user_input = user_input.lower().strip()
name[0] = name[0].lower().strip()
name[1] = name[1].lower().strip()
name[2] = name[2].lower().strip()
name[3] = name[3].lower().strip()

if user_input in name:
    print("User is in list")
else:
    print("User is not in list")