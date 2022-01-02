# Using with and as will close the file automatically

with open("another.txt", "w") as f:
    f.write("Writing using with and as")

with open("another.txt", "r") as f:
    data = f.read()

print(data)