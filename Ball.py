from Pole import Pole


class Ball:
    
    def __init__(self, x, y, colour, poles):
        self.x = x
        self.y = y
        self.xs = PI/2400
        self.ys = PI/2400
        self.s = PI/2400
        self.a = 2*self.s
        self.gravity = 1
        self.c = colour
        self.poles = poles
        self.poleDistances = [10000,10000,10000,10000]
        self.isAttached = False
        self.poleAttached = 0
        self.d = dist(self.x, self.y, self.poles[self.poleAttached].x, self.poles[self.poleAttached].y)
        self.t = asin((self.y-self.poles[self.poleAttached].y)/self.d)
        self.downPressed = False
        self.score = 0
        
        
    def display(self):
        strokeWeight(1)
        self.d = dist(self.x, self.y, self.poles[self.poleAttached].x, self.poles[self.poleAttached].y)
        
        if self.isAttached:
            self.pole = self.poles[self.poleAttached]
            line(self.x, self.y, self.pole.x, self.pole.y)
            
            self.x = self.d*cos(self.t) + self.pole.x
        
            self.y = self.d*sin(self.t) + self.pole.y
        
            self.t += self.s
                        
            
            if self.t <= PI/2:
                self.s += self.a
            elif self.t > PI/2:
                
                self.s -= self.a
        elif not self.isAttached:
            
            self.x += 75*self.xs
            self.y += 75*self.ys + self.a
            
            if self.downPressed:
                self.ys += 2*self.a
            else:
                self.ys += self.a/2
            
        if self.t >= PI*3/2:
            self.t = TWO_PI - self.t
        
        fill(self.c)
        circle(self.x, self.y, 50)
        
    def attach(self):
        if self.d <= 500:
            self.t = asin((self.y-self.poles[self.poleAttached].y)/self.d) % TWO_PI
            if not self.isAttached: 
                for i in range(len(self.poles)):
                    self.poleDistances[i] = dist(self.x, self.y, self.poles[i].x, self.poles[i].y)
        
            
                
                self.poleAttached = self.poleDistances.index(min(self.poleDistances))
                self.isAttached = True
                self.score += 1

        
    def detach(self):
        if self.isAttached:
            self.isAttached = False
            self.p = cos(self.t-3*PI/2)
            self.q = sin(self.t-3*PI/2)
            self.xs = self.s*self.p
            self.ys = self.s*self.q
    
    def withinBounds(self):
        return self.y >= 0 and self.y <= 720 and self.x >= 0
