from Button import Button


class Screen(object):
    margin = 720/8
    margin2x = 2*margin
    margin6x = 6*margin
    margin4x = 4*margin
    
    def __init__(self):
        self.isActive = False
        
    
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
        
class StartScreen(Screen):
    def __init__(self):
        # print("Init")
        super(StartScreen, self).__init__()
        self.startButton = Button.BlueButton(Screen.margin2x, Screen.margin6x, "Start")
        self.infoButton = Button.GreyButton(Screen.margin6x, Screen.margin6x, "Info")
        
        
    
        
    def display(self):
        
        if self.isActive:
            # print("display")
            super(StartScreen, self).display()
            textSize(75)
            text("Swing Shot", 360, 180)
            self.displayButtons()
    
    def displayButtons(self):
        # print("Display Buttons")
        self.startButton.display()
        self.infoButton.display()
    
    def hover(self, mx, my):
        if self.isActive:
            self.startButton.hover(mx, my)
            self.infoButton.hover(mx, my)
        
class SelectScreen(Screen):
    def __init__(self):
        super(SelectScreen, self).__init__()
    
    def display(self):
        if self.isActive:
            super(SelectScreen, self).display()
            textSize(50)
            text("Select Color:", 360, 180)
        
