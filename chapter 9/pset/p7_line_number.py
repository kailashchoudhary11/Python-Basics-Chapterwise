isPresent = False
lineNumber = 1

with open("log.txt") as f:
    data = f.readline()

    while data:
        if "python" in data.lower():
            isPresent = True
            print("python is present at line number", lineNumber)

        data = f.readline()
        lineNumber += 1

if not isPresent:
    print("python is not present")