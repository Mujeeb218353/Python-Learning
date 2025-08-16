list = ["Rohan", "Coca Cola", "Pepsi", "Shezan"]
print(list)

def remove_item(list, word):
    n = []
    for item in list:
        if item != word:
            n.append(item.strip(word))
    return n


print(remove_item(list, "an"))