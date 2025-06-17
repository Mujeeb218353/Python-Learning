marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.get("Alice")) # Print non-existing key returns None

copied_marks = marks.copy()
print(copied_marks)

marks.update({"Alice": 90, "David": 88})
print(marks)

removed_mark = marks.pop("Charlie") # Removes key-value pair for 'Charlie'
print(removed_mark)
print(marks)

removed_mark = marks.popitem() # Removes the last inserted key-value pair
print(removed_mark)
print(marks)

del marks["Alice"] # Removes key-value pair for 'Alice'
print(marks)

setdefault = marks.setdefault("Eve", 95) # Adds key 'Eve' with value 95 if not present
print(setdefault)

new_marks = dict.fromkeys(["Alice", "Bob", "Charlie"], 85)  # Returns a dictionary with the specified keys and value
print(new_marks)

marks.clear()
print(marks)