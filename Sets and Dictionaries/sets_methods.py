s = {1, 2, 3, 4, 5, 6, "Mujeeb"}
print(s)
print(len(s))

s.add(7)
print(s)

s.remove(3)
print(s)

s.discard(10)  # Removes the specified element. Does not raise an error if the element is not found
print(s)

s.pop()  # Removes and returns an arbitrary element from the set
print(s)

s.update([8, 9, 10])
print(s)

s1 = {1, 2, 3}
s2 = {4, 5, 6}
s1.update(s2)  # Updates the set by adding elements from another set
print(s1)

s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = s1.union(s2)  # Returns a new set with all items from both sets
print(s3)

s1 = {1, 2, 3}
s2 = {4, 5, 6}
s1.intersection(s2)  # Returns a new set with elements common to both sets
print(s1)

s1 = {1, 2, 3}
s2 = {4, 5, 6}
s1.intersection_update(s2)  # Updates the set by keeping only the elements that are also in another set
print(s1)

s1 = {1, 2, 3, 4, 5, 6, 10}
s2 = {4, 5, 6 , 7, 8, 9}
s1.difference(s2)  # Returns a new set with elements in the set that are not in the other set
print(s1)

s1 = {1, 2, 3, 4, 5, 6, 10}
s2 = {4, 5, 6 , 7, 8, 9}
s1.difference_update(s2)  # Updates the set by removing elements that are also in another set
print(s1)

print(s1-s2)

s1 = {1, 2, 3, 4, 5, 6, 10}
s2 = {4, 5, 6 , 7, 8, 9}
s1.symmetric_difference(s2)  # Returns a new set with elements in either set, but not both
print(s1)

s1 = {1, 2, 3, 4, 5, 6, 10}
s2 = {4, 5, 6 , 7, 8, 9}
s1.symmetric_difference_update(s2)  # Updates the set by keeping only elements found in either set, but not in both
print(s1)

s.clear()  # Removes all elements from the set
print(s)