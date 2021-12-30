message = input("Enter the message\n")

spam1 = "make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

if (spam1 in message or spam2 in message or spam3 in message or spam4 in message):
    print("Your message is a spam")
else:
    print("Your message is not a spam")



