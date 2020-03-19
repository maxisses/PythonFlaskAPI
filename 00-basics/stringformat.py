name = "Bob"

print(f"Hello, {name}")

greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format("blabla")

print(with_name_two)

longer_phrase = "Hello, {}. And Hello {}."

print(longer_phrase.format("Scheisse", "blöd"))

name = input("Enter your Name: ")

print(name)

size_input = input("Wie groß bist du? (in cm)")

your_size = int(size_input)/100

size_template = "Hello, you are {} m tall."

print(size_template.format(your_size))

print(f"Hello {name}, you are {your_size:.2f} m tall.")