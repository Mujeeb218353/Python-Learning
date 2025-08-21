content = ""

with open("file1.txt") as f:
    content += f.read()

word = "donkey"
content =  content.replace(word, "#"*len(word))

with open("file1.txt", "w") as f:
    f.write(content)