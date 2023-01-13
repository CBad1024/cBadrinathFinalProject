class Button(object):
    
    BLUE = "#B2BFFF"
    RED = "#FA88AA"
    YELLOW = "#FFF2B2"
    GREY = "#C6C6C6"
    WHITE = "#FFFFFF"
    GREEN = "#94CE97"
    ORANGE = "#F79B5C"
    PURPLE = "#E6E6FA"
    
    
    def __init__(self, xPos, yPos, xLen, yLen, kolor , message = ""):
        self.x = xPos
        self.y = yPos
        self.xl = xLen
        self.yl = yLen
        self.c = kolor
        self.m = message
        self.strColor = "#FFFFFF"
        self.strWt = 0
        self.strokePermanent = False
        
    
   
    
    @classmethod
    def BlueButton(cls, xPos, yPos, message):
        return cls(xPos, yPos, 180, 90, Button.BLUE, message)
            
            
    @classmethod
    def GreyButton(cls, xPos, yPos, message):
        return cls(xPos, yPos, 180, 90, Button.GREY, message)
   
    def display(self):
        rectMode(CENTER)
        textAlign(CENTER, CENTER)
        textSize(40)
        fill(self.c)
        strokeWeight(self.strWt)
        stroke(self.strColor)
        rect(self.x, self.y, self.xl, self.yl)
        fill(255)
        text(str(self.m), self.x, self.y)
        
    def isClicked(self, mx, my):
        return  mx > (self.x - 0.5*self.xl) and mx < (self.x + 0.5*self.xl) and my > (self.y - 0.5*self.yl) and my < (self.y + 0.5*self.yl)

    def hover(self, mx, my):
        if  mx > (self.x - 0.5*self.xl) and mx < (self.x + 0.5*self.xl) and my > (self.y - 0.5*self.yl) and my < (self.y + 0.5*self.yl):
            self.setStroke()
        else:
            self.unsetStroke()

    def setStroke(self):
        self.strColor = "#FFF2B2"
        self.strWt = 10
    
    def setStrokePermanent(self):
        pass
        
    def unsetStroke(self):
        if not self.strokePermanent:
            self.strColor = "#FFFFFF"
            self.strWt = 0
    


class CircleButton(Button):
    def __init__(self, xPos, yPos, colour):
        super(CircleButton, self).__init__(xPos, yPos, 60, 60, colour)
        
    def display(self):
        fill(self.c)
        strokeWeight(self.strWt)
        stroke(self.strColor)
        circle(self.x, self.y, self.xl)
        
    def setStrokePermanent(self):
        self.strokePermanent = True
        self.setStroke()
        
    def hover(self, mx, my):
        
        if  dist(mx, my, self.x, self.y) <= self.xl/2:
            self.setStroke()
        else:
            self.unsetStroke()
    
    
        
        
    
