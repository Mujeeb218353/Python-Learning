'''
1 for snake
2 for water
3 for gun

Snake(1) wins over water(2)
Water(2) wins over gun(3)
Gun(3) wins over snake(1)
'''

import random

computer = random.randint(1,3)

user = int(input("1 for snake\n2 for water\n3 for gun\nEnter your choice: "))

dictionary = {
    1: "Snake",
    2: "Water",
    3: "Gun"
}

print(f"You choose {dictionary[user]}")
print(f"Computer choose {dictionary[computer]}")

if user == computer:
    print("Tie")

elif user == 1 and computer == 2:
    print("You win")

elif user == 1 and computer == 3:
    print("You lose")

elif user == 2 and computer == 1:
    print("You lose")

elif user == 2 and computer == 3:
    print("You win")

elif user == 3 and computer == 1:
    print("You win")

elif user == 3 and computer == 2:
    print("You lose")

else:
    print("Invalid input")