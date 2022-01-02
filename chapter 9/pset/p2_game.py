def game():
    score = 39
    return score

with open("highscore.txt") as f:
    highScore = f.readline()

gameScore = game()
if (highScore == "" or gameScore > int(highScore)):
    with open("highscore.txt", "w") as f:
        f.write(str(gameScore)) 

