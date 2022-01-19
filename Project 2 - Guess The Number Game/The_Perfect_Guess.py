import random



playAgain = True
highestScore = 100
while(playAgain):
    numberToBeGuessed = random.randint(1, 100)

    guessedNumber = int(input("Please guess a number between 1 and 100: "))
    count = 1
    while (guessedNumber != numberToBeGuessed):
        if guessedNumber > numberToBeGuessed:
            guessedNumber = int(input("Please Guess A Smaller Number: "))

        else:
            guessedNumber = int(input("Please Guess A Greater Number: "))

        count += 1

    print(f"You guessed the Correct Number in {count} attempts")
    with open("highscore.txt") as f:
        fileHigh = f.read()
    if (fileHigh == "" or int(fileHigh) > count):
        with open("highscore.txt", "w") as f:
            f.write(str(count))
        print(f"Your New High Score is {count} attempts")

    if (highestScore > count):
        highestScore = count
    play = input("Press y to play again and e to exit: ")
    if (play != "y"):
        playAgain = False
    