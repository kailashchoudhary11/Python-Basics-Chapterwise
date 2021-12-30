story = "Once upon a time there was a boy named kai and he was really awesome. he loves programming"

# print(story[0])
# print(story[0:5])


# String functions

# print(len(story)) # This will print the length of the string story

# print(story.endswith("kai")) # This will return false # Returns true if the string ends with the given string and false otherwise
# print(story.endswith("awesome")) # This will return true # Returns true if the string ends with the given string and false otherwise

# print(story.count("O")) # This will count the occurrences of the given substring in the string
# print(story.count("o")) # 'o' is occuring 3 times in the string story
# print(story.count("e")) # 'e' is occuring 9 times in the string story
# print(story.count("was")) # "was" is occuring 2 times in the string

# story = "once upon a time there was a boy named kai and he was really awesome. he loves programming"
# print(story.capitalize()) # This will capitalize the first letter of the string story


# print(story.find("kai")) # Will return the starting position of the string if it's present in the given string 
# print(story.find("ak")) # Will return -1 if the string is not present in the given string
# print(story.find("was")) # This will return only the first occurrence

# print(story.replace("kai", "unknown")) # This will replace the first string with the second string in the given string. It will replace all the occurrences

# print(story.startswith("how")) # Checks whether the string starts with given string or not 
# print(story.startswith("Once")) # Checks whether the string starts with given string or not 

str = "HELLO everyone HOW are you all"

# print(str.casefold())  # Will convert all the characters in the string to lowercase

# str = "kai"

# print(str.isalnum())  # This will return true if all the characters in the string are either alphabets or numeric

# If there are spaces or any kind of symbols then the function will return false

# print(str.isalpha()) # This will return true if all the characters are alphabets in the string

# str = "kai. how are you?"

# print(str.islower()) # Returns true if there is no uppercase alphabet in the string

# str = "KAI IS HERE!"

# print(str.isupper()) # Returns true if there is no lowercase character in the string

# str = "hey guys! how are you'll?"
# print(str.upper())  #Converts all the characters in the string to uppercase 

# str = "HEY GUYS! HOW ARE YOU'LL?"
# print(str.lower()) # Converts all the characters in the string to lowercase

print(story.title()) # Converts the first character of every word to uppercase