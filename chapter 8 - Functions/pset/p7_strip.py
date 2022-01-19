def removeWordAndStrip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

str = input("Enter a string: ")
print(removeWordAndStrip(str, "kai"))