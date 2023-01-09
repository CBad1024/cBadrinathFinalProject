from Screen import StartScreen, SelectScreen, InfoScreen, Screen


startScreen = StartScreen()
selectScreen = SelectScreen()

infoScreen = InfoScreen()
def setup():
    size(720, 720)
    startScreen.activate()
    
def draw():
    startScreen.display()
    selectScreen.display()
    infoScreen.display()

def mouseReleased():
    
    if startScreen.isActive:
        order = startScreen.buttonsClicked(mouseX, mouseY)
        activateScreens(order)
    
    
    if selectScreen.isActive:
        order = selectScreen.buttonsClicked(mouseX, mouseY)
        activateScreens(order)
        
 
def activateScreens(order):
    if order == Screen.order1:
        selectScreen.activate()
    elif order == Screen.order2:
        infoScreen.activate()
    elif order == Screen.order0:
        startScreen.activate()

def mouseMoved():
    startScreen.hover(mouseX, mouseY)
    selectScreen.hover(mouseX, mouseY)
