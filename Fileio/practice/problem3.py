def generate_table(n):
    table = ""
    for i in range(0, 11):
        if(i == 0):
            table += f"Table of {n}:\n"
        table += f"{n} x {i} = {n*i}\n"
    table+= "\n"
    return table

for i in range(2, 21):
    table = generate_table(i)
    with open("tables.txt", "a") as f:
        f.write(table)