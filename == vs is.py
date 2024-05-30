l1 = [1, 2, 3]

l2 = l1

print(id(l1))
print(id(l2))
print(id(l1) == id(l2))
print(l1 is l2)
print((l1 is l2) == (id(l1) == id(l2)))