from Screen import StartScreen, SelectScreen, InfoScreen, Screen
from GameScreen import GameScreen, WinScreen

startScreen = None
selectScreen = None
infoScreen = None
gameScreen = None
winScreen = None
screens = []
width_ = 0
height_ = 0

def setup():
    global startScreen, selectScreen, infoScreen, gameScreen, screens, winScreen, width_, height_
    size(720, 720)
    width_ = width
    height_ = height
    resetScreens()
    
    startScreen.activate()
    selectScreen.deactivate()
    gameScreen.deactivate()
    infoScreen.deactivate()
    winScreen.deactivate()

    
order = 0

    
def draw():
    global order
    if startScreen.isActive:
        startScreen.display()
    elif infoScreen.isActive:
        infoScreen.display()
    elif selectScreen.isActive:
        selectScreen.display()
        gameScreen.ball.c = selectScreen.c
    elif gameScreen.isActive:
        gameScreen.display()
        winScreen.score = gameScreen.ball.score
    elif winScreen.isActive:
        winScreen.display()
        
def mouseReleased():
    global order
    if startScreen.isActive:
        order = startScreen.buttonsClicked(mouseX, mouseY)
        checkScreens(order)
    elif selectScreen.isActive:
        order = selectScreen.buttonsClicked(mouseX, mouseY)
        checkScreens(order)    
    elif gameScreen.isActive:
        order = gameScreen.checkLoss()
        checkScreens(order)
        
def checkScreens(order):
    for screen in screens:
        screen.deactivate()
    
    if order == Screen.order0:
        startScreen.activate()
    elif order == Screen.order1:
        selectScreen.activate()
    elif order == Screen.order2:
        infoScreen.activate()
    elif order == Screen.order3:
        gameScreen.activate()
    elif order == Screen.order4:
        winScreen.activate()

def mouseMoved():
    if startScreen.isActive:
        startScreen.hover(mouseX, mouseY)
    elif selectScreen.isActive:
        selectScreen.hover(mouseX, mouseY)
    
started = False

def resetScreens():
    global startScreen, selectScreen, infoScreen, gameScreen, screens, winScreen, screens
    startScreen = StartScreen()
    selectScreen = SelectScreen()
    infoScreen = InfoScreen()
    gameScreen = GameScreen(None, width_, height_)
    winScreen = WinScreen(None)
    screens = [startScreen, selectScreen, infoScreen, gameScreen, winScreen]
    
def keyPressed():
    global started, gameScreen
    
    if key == " ":
        if infoScreen.isActive:
            checkScreens(Screen.order0)
        elif winScreen.isActive:
            resetScreens()
            checkScreens(Screen.order0)
        if gameScreen.isActive:
            if not gameScreen.gameOver:
                gameScreen.gameStart()
                started = True
            
                if gameScreen.ball.isAttached:
                    gameScreen.ball.detach()
                else:
                    gameScreen.ball.attach()
        
    
