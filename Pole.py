class Pole(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = False
        
    def display(self):
        fill(0)
        circle(self.x, self.y, 10)
        if self.active:
            self.x -= 1
    

class PoleLines(object):
    def __init__(self):
        self.setValues()
    
    def setValues(self):
        self.poleCount = 3
        self.y = 720/4
        self.x = 180
        self.offset = 180
        self.poles = [Pole(self.x, self.y)]

    
    def start(self):
        for pole in self.poles:
            pole.active = True
    
    def stop(self):
        for pole in self.poles:
            pole.active = False
        
        
    def display(self, poleAttached):
        #Determine spacing & spread of poles

        if len(self.poles) <= self.poleCount:
            self.poles.append(Pole(self.poles[-1].x + self.offset, self.y))
            self.y = int(random(3)+1)*720/4
        
        for i in range(len(self.poles)):
            if self.poles[i].x < 0:
                if poleAttached == i:
                    return False
                else:
                    self.poles[i] = Pole(720, int(random(3)+1)*720/4)
                    self.poles[i].active = True
        
        for pole in self.poles:
            pole.display()
                
        
        
        
    
