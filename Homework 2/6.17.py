password = input()
new_password = ""
for letter in password:
    if letter == "i":
        new_password = new_password + "!"
    elif letter == "a":
        new_password = new_password + "@"
    elif letter == "m":
        new_password = new_password + "M"
    elif letter == "B":
        new_password = new_password + "8"
    elif letter == "o":
        new_password = new_password + "."
    else:
        new_password = new_password + letter
print(new_password + "q*s")
