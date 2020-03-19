users = [
    (0, "Bob", "password"),
    (1, "Ralf", "password"),
    (2, "Henning", "password"),
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)

username_input = input("Enter your username: ")
username_pw = input("Give your pw: ")

# destructure it
_, username, password = username_mapping[username_input]

if username_pw == password:
    print("Details correct")
else:
    print("wrong")
    input(" again: ")