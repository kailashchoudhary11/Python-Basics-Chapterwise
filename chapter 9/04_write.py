# f = open("another.txt", "w")

# f.write("I am writing this to a newly made file. This will be overwritten as I have opened file in write mode.")

f = open("another.txt", "a")

f.write("\nThis will be appended at the end of the file")

f.close()