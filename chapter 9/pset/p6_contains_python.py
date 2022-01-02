with open("log.txt") as f:
    data = f.read()

if ("python" in data.lower()):
    print("The log file contains python")
else:
    print("The log file does not contain python")