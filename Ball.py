class Ball:
    
    def __init__(self, px, py, vx, vy): #initial state of the Ball defined
        self._posX = px
        self._posY = py
        self._velX = vx
        self._velY = vy

    def getPositionX(self):
        return self._posX
    
    def getPositionY(self):
        return self._posY

    def getVelocityX(self):
        return self._velX

    def getVelocityY(self):
        return self._velY

    def advance(self, world):
        self._posX += self._velX
        g = world.getGravity() * -1
        self._posY += self._velY + g


