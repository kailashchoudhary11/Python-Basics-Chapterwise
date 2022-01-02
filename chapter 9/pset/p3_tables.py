from os import name


for i in range(2, 21):
    name = "Table of " + str(i) + ".txt"
    with open("Tables\\" + name, "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")
