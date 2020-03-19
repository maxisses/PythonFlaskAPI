a = []
b = a

# id returns the location in memory
print(id(a))
print(id(b))

a.append(35)

print(a)
print(b)