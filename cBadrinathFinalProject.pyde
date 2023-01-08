from Screen import StartScreen, SelectScreen

startScreen = StartScreen()
# selectScreen = SelectScreen()
def mouseMoved():
    startScreen.hover(mouseX, mouseY)
    
def setup():
    size(720, 720)
    startScreen.activate()

def draw():
    startScreen.display()
    

    
