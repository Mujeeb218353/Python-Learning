marks = {
    "Mujeeb": 78,
    "Farhan": 89,
    0: 45
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Mujeeb": 90})

print(marks)

print(marks.get("Mujeeb2"))# return (None)
# print(marks["Mujeeb2"]) # error


print(len(marks))
