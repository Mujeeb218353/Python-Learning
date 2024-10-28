spam = ["Make a lot of money", "Buy now", "Subscribe this", "Click this"]

message = input("Enter your message: ")

if message in spam:
    print("This message contains spam")
else:
    print("This message is not spam")