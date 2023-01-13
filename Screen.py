from Button import Button, CircleButton


class Screen(object):
    
    order0 = 0
    order1 = 1
    order2 = 2
    order3 = 3
    order4 = 4
    margin = 720/8
    margin2x = 2*margin
    margin6x = 6*margin
    margin4x = 4*margin
    
    
    def __init__(self):
        self.isActive = False
        self.buttons = []
        self.order = -1
        # 
        # 
    
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
        f = loadFont("Herculanum-48.vlw")
        fill(0)
        textFont(f)
        textAlign(CENTER, CENTER)
    
    
    
    def hover(self, mx, my):
        for button in self.buttons:
            button.hover(mx, my)
  
    def buttonsClicked(self, mx, my):
        return Screen.order0
        
    def buttonsDisplay(self):
        for button in self.buttons:
            button.display()
            
            
class StartScreen(Screen):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.startButton = Button.BlueButton(Screen.margin2x, Screen.margin6x, "Start")
        self.infoButton = Button.GreyButton(Screen.margin6x, Screen.margin6x, "Info")
        self.buttons = [self.startButton, self.infoButton]
        self.order = Screen.order0
        

    def buttonsClicked(self, mx, my):
        if self.startButton.isClicked(mx, my):
            self.deactivate()
            return Screen.order1
        elif self.infoButton.isClicked(mx, my):
            self.deactivate()
            return Screen.order2
        return Screen.order0

        
    def display(self):
        super(StartScreen, self).display()
        textSize(75)
        text("Swing Shot", 360, 180)
        self.buttonsDisplay()
    
    
class SelectScreen(Screen):
    
    def __init__(self):
        super(SelectScreen, self).__init__()
        offset  = Screen.margin
        self.redC = CircleButton(offset, 4*offset, Button.RED)
        self.blueC = CircleButton(2.5*offset, 4*offset, Button.PURPLE)
        self.orangeC = CircleButton(4*offset, 4*offset, Button.ORANGE)
        self.greyC = CircleButton(5.5*offset, 4*offset, Button.GREY)
        self.greenC = CircleButton(7*offset, 4*offset, Button.GREEN)
        self.playButton = Button.BlueButton(4*offset, 6*offset, "Play")
        self.c = 0
        self.buttons = [self.redC, self.blueC, self.orangeC, self.greyC, self.greenC]
        self.order = Screen.order1
    
    
    def buttonsClicked(self, mx, my):
        colorSelected = False
        order = Screen.order1
        for button in self.buttons:
            button.strokePermanent = False
            
        for button in self.buttons:
            if button.isClicked(mx, my):
                colorSelected = True
                button.setStrokePermanent()
                if isinstance(button, CircleButton):
                    self.c = button.c
                elif isinstance(button, Button):
                    order = Screen.order3
                
                    
                
        if colorSelected and not (self.playButton in self.buttons):
            self.buttons.append(self.playButton)
        
        return order
    
    def display(self):
        super(SelectScreen, self).display()
        textSize(50)
        text("Select Color:", 360, 180)
        self.buttonsDisplay()
            
            
class InfoScreen(Screen):
    
    def __init__(self):
        super(InfoScreen, self).__init__()
        self.order = 2
        
    def display(self):
        if self.isActive:
            super(InfoScreen, self).display()
            fill(0)
            k = loadFont("KoHo-ExtraLight-30.vlw")
            textFont(k)
            textSize(30)
            goal = "GOAL:  Survive as long as possible."
            text(goal, 360, 100)
            textSize(20)
            
            message = """You are a ball on the run. 
             
            You can attach and detach from poles using a rope (press spacebar)
            You move like a pendulum.
            Use your momentum to swing from pole to pole.
            You fail if you hit the ceiling or floor or lag behind. 
        
            
            Good luck, and enjoy the game. (Click the spacebar to continue)"""

            text(message, 360, 360)
            
    
    
     
        
