o = { 1, 3, 5, 7, 9, 10 }
e = { 2, 4, 6, 8, 10 }

print(o.union(e))

print(e.intersection(o))

print(o.intersection(e))

print(o-e)

print(o.symmetric_difference(e))
print(e.symmetric_difference(o))