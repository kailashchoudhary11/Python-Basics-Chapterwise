myDict = {
    "pankha" : "fan",
    "dabba" : "box",
    "vastu" : "item",
    "angur" : "grapes"
}
print("Options for hindi words are:\n", myDict.keys())
key = input("Enter the Hindi Word\n")
print("The meaning of word " + key + " in english is", myDict.get(key))
