with open("file_functions.txt", "r") as f:
    text = f.read()
    if("Twinkle" in text):
        print("Twinkle is present in the file")
    else:
        print("Twinkle is not present in the file")