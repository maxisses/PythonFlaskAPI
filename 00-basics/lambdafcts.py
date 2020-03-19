## lambda functions

def add(x,y):
    return x+y

print(add(5,7))

add = lambda x, y: x+y

print(add(5,6))


(lambda x, y: x+y)


def double(x):
    return x*2

sequence = [1,2,3,4,5]

doubled = [double(x) for x in sequence]
print(doubled)

doubled = map(double, sequence)
print(list(doubled))

doubled = [(lambda x: x*2)(x) for x in sequence]
print(doubled)
