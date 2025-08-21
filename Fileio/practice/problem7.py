with open("log.txt") as f:  
    content =  f.readlines()
    lineno = 1
    for line in content:
        if "python" in line:
            print(f"python is present in line number {lineno}")
            break
        lineno += 1
    else:
        print("python is not present in file")


    
