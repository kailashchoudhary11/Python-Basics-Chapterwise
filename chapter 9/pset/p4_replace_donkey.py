with open("sample.txt") as f:
    data = f.read()

data = data.replace("donkey", "$%@^##")

with open('sample.txt', "w") as f:
    f.write(data)