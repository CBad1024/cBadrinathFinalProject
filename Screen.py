class Screen:
    def __init__(self):
        pass
        
class StartScreen(Screen):
    def __init__(self):
        self.isActive = False
    
    def activate():
        self.isActive = True
        
    def deactivate():
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
        textSize(75)
        text("Swing Shot", 360, 180)
        
class SelectScreen(Screen):
    def __init__(self):
        pass
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
        textSize(50)
        text("Select Color:", 360, 180)
        
