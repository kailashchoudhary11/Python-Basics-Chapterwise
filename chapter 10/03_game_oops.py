class Remote:
    def isLeftPressed(self):
        pass
    def isRightPressed(self):
        pass
    def isUpPressed(self):
        pass
    def isDownPressed(self):
        pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveForward(self):
        pass
    def moveBackward(self):
        pass

player1 = Player()
remote1 = Remote()

if (remote1.isLeftPressed()):
    player1.moveLeft()
elif (remote1.isRightPressed()):
    player1.moveRight()
elif (remote1.isUpPressed()):
    player1.moveForward()()
elif (remote1.isDownPressed()):
    player1.moveBackward()