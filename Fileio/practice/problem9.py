with open("this.txt") as f:
    content1 = f.read()

with open("copy_this.txt") as f:
    content2 = f.read()


if content1 == content2:
    print("Files are same")
else:
    print("Files are different")