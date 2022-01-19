# Detecting double spaces in a string 

str = "This  String Contains     double    spaces  "
print(str.find("  ")) #Returns the first occurrence of the double spaces
print(str.count("  ")) #Returns the total number of double spaces
