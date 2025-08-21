content = ""
word = ["donkey", "monkey", "elephant"]

with open("file2.txt") as f:
    content += f.read()

for i in range(len(word)):
    content =  content.replace(word[i], "#"*len(word[i]))

with open("file2.txt", "w") as f:
    f.write(content)