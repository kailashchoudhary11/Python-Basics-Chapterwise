with open("this.txt") as f:
    data1 = f.read()

with open("this_copy.txt") as f:
    data2 = f.read()

if data1 == data2:
    print("Both the files are same")
else:
    print("Both the files are different")