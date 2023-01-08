from Button import Button


class Screen(object):
    margin = 720/8
    margin2x = 2*margin
    margin6x = 6*margin
    margin4x = 4*margin
    
    def __init__(self):
        self.isActive = False
        self.buttons = []
    
    def activate(self):
        self.isActive = True
        
    def deactivate(self):
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
        # print("CirclesDrawn")
        f = loadFont("Herculanum-48.vlw")
        # print("Font created")
        fill(0)
        textFont(f)
        textAlign(CENTER, CENTER)
    
    
    def hover(self, mx, my):
        for button in self.buttons:
            button.hover(mx, my)
    
    def buttonsClicked(self, mx, my):
        for button in self.buttons:
            button.isClicked(mx, my)
            
    def buttonsDisplay(self):
        for button in self.buttons:
            button.display()
            
            
class StartScreen(Screen):
    def __init__(self):
        # print("Init")
        super(StartScreen, self).__init__()
        self.startButton = Button.BlueButton(Screen.margin2x, Screen.margin6x, "Start")
        self.infoButton = Button.GreyButton(Screen.margin6x, Screen.margin6x, "Info")
        self.buttons = [self.startButton, self.infoButton]
        
        
    
        
    def display(self):
        
        if self.isActive:
            # print("display")
            super(StartScreen, self).display()
            textSize(75)
            text("Swing Shot", 360, 180)
            self.buttonsDisplay()
    
    
        
class SelectScreen(Screen):
    def __init__(self):
        super(SelectScreen, self).__init__()
    
    def display(self):
        if self.isActive:
            super(SelectScreen, self).display()
            textSize(50)
            text("Select Color:", 360, 180)
        
