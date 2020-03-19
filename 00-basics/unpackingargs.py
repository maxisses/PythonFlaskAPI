
### args collects everything being passed
def multiply(*args):
    total = 1
    for arg in args:
        total = total *arg
    return total


print(multiply(1,3,5))


def add(x,y):
    return x+y

nums = [4,5]
print(add(*nums))


nums = {"x": 15, "y": 25}
print(add(x=nums["x"], y=nums["y"]))

print(add(**nums))

def add2(x,y,z ):
    return x+y+z

nums = {"x": 15, "y": 25, "z": 30}
print(add2(**nums))