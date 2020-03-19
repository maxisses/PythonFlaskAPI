class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"This object contains the user {self.name} with his age {self.age}"

    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

bob = Person("Bob", 35)

print(bob)