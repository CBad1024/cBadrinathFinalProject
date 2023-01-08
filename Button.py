class Button(object):
    
    BLUE = "#B2BFFF"
    RED = "#FA88AA"
    
    def __init__(self, xPos, yPos, xLen, yLen, kolor , message):
        self.x = xPos
        self.y = yPos
        self.xl = xLen
        self.yl = yLen
        self.c = kolor
        self.m = message
        self.strColor = "#FFFFFF"
        self.strWt = 0
    
    @classmethod
    def BlueButton(cls, xPos, yPos, xLen, yLen, message):
        return cls(xPos, yPos, xLen, yLen, Button.BLUE, message)
            
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

    # def hover(self, mx, my):
    #     return  mx > (self.x - 0.5*self.xl) and mx < (self.x + 0.5*self.xl) and my > (self.y - 0.5*self.yl) and my < (self.y + 0.5*self.yl)

    # def setStroke(self):
    #     self.strColor = "#B2BFFF"
    #     self.strWt = 10
        
    # def unsetStroke(self):
    #     self.strColor = "#FFFFFF"
    #     self.strWt = 0
    
        
        
    
