from Screen import Screen, SelectScreen
from Pole import PoleLines
from Ball import Ball

class GameScreen(Screen):
    
    def __init__(self, c, width_, height_):
        super(GameScreen, self).__init__()
        self.order = Screen.order3
        self.poleLines = PoleLines()
        self.ball = Ball(50, 200, c, self.poleLines.poles)
        self.ball.attach()
        self.width_ = width_
        self.height_ = height_
        self.ballAttachedToPoleOnScreen = True
        self.gameOver = False
        self.started = False
        self.isActive = False
        
    def display(self):
        background(255)
        fill("#FFF2B2")
        
        noStroke()
        circle(0, 0, 400)
        circle(200, 0, 200)
        circle(540, 45, 200)
        circle(720, 45, 200)
        circle(630, 70, 200)
        stroke(100)
        fill(0)
        textSize(20)
        text("Score: " + str(self.ball.score), 50, 50)
        
        
        if not self.gameOver:
            self.ball.display()
        if self.started:
            self.ball.x -= 1
        self.drawPoles()
        if self.checkLoss() != Screen.order3:
            textSize(50)
            fill(0)
            textAlign(CENTER)
            text("Click to continue...", 360, 360)
    
    
    def drawPoles(self):
        lnOff = self.width_/4
        for l in range(4):
            line(0, l*lnOff, self.width_, l*lnOff)
        
        self.ballAttachedToPoleOnScreen = self.poleLines.display(self.ball.poleAttached)

    def gameStart(self):
        self.poleLines.start()
        self.started = True
   
    def gameStop(self):
        self.poleLines.stop()
        self.started = False
        self.gameOver = True
    
    def checkLoss(self):
        if not self.ball.withinBounds() and not self.ballAttachedToPoleOnScreen:
            self.gameStop()
            self.order = Screen.order4
        return self.order
    
    

class WinScreen(Screen):
    def __init__(self, score):
        super(WinScreen, self).__init__()
        self.order = Screen.order4
        self.score = score
        self.isActive = False
    
    def display(self):
        super(WinScreen, self).display()
        fill(0)
        textAlign(CENTER)
        textSize(25)
        text("Your score is", 360, 120)
        textSize(200)
        text(str(self.score), 360, 360)
        textSize(25)
        text("Click spacebar to continue", 360, 500)
        
        
        
