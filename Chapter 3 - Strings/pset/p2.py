name = input("Enter Name\n")
date = input("Enter Date\n")

letter = '''
Dear <|Name|>,
Greetings from Kai the Coder! I am happy to let you know that,
you are selected as a developer in our company.
Have a great day ahead!

Thanks and regards,
kai

Date: <|Date|>
'''

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)