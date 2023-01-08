from Screen import StartScreen, SelectScreen

startScreen = StartScreen()
selectScreen = SelectScreen()
def mouseReleased():
    #Fix
    startScreen.buttonsClicked(mouseX, mouseY)
    if not startScreen.isActive:
        selectScreen.activate()
        selectScreen.buttonsClicked(mouseX, mouseY)

 


def mouseMoved():
    startScreen.hover(mouseX, mouseY)
    selectScreen.hover(mouseX, mouseY)
    
def setup():
    size(720, 720)
    startScreen.activate()

def draw():
    startScreen.display()
    selectScreen.display()
    

    
