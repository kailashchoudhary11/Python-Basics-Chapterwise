with open("poem.txt", "r") as f:
    data = f.read()

data = data.lower()

if ("twinkle" in data):
    print("Yes the poem contains the word 'twinkle'")
else:
    print("No the poem does not contain the word 'twinkle'")
