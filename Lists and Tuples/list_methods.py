friends = ["Apple", 1, False, 1.43]
print(friends)

friends.append("Banana")
print(friends)

numbers = [3,5,3,2,8,1]
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.insert(2, 99) # (index, value)
print(numbers)

numbers.remove(99)
print(numbers)

popped_item = numbers.pop()
print(popped_item)
print(numbers)

numbers.extend([7, 4, 6])
print(numbers)

count_of_3 = numbers.count(3) # Returns the number of elements with the specified value
print(count_of_3)
print(numbers)

index_of_3 = numbers.index(3) # Returns the index of the first element with the specified value
print(index_of_3)

print(len(numbers))

numbers.clear()
print(numbers)