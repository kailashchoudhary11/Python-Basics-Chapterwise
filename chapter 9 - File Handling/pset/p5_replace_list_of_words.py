words = ["donkey", "monkey", "dog"]

with open("sample2.txt", "r") as f:
    data = f.read()

for word in words:
    data = data.replace(word, "#$%&^#")

with open("sample2.txt", "w") as f:
    f.write(data)