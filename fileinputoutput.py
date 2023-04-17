name = input("what is your name?")

with open("name.txt", "a")as file

file = open("names.txt", "a")
file.write(f"{name}\n")
