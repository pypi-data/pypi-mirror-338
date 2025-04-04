from .helpers import parseCoordinates

class Rect():
    def __init__(self, *args):
        c = 0
        others = []
        for e in args:
            if isinstance(e, tuple):
                if len(e) == 2:
                    self.x,self.y = e
                    c+=1
            else:
                others.append(e)
        if c < 1 or c > 2 or c == 1 and len(others)!=2 or c == 2 and len(others) != 0:
            raise Exception("Couldn't create Rect, use two points or one point and width, height")
        if c == 1:
            self.width = others[0]
            self.height = others[1]
        if c == 2:
            x1, y1 = args[0]
            x2, y2 = args[1]
            self.x = min(x1, x2)
            self.y = min(y1, y2)
            self.width = max(x1, x2) - self.x
            self.height = max(y1, y2) - self.y
            
    def getCenter(self):
        return (int(self.x + self.width/2), int(self.y + self.height/2))
    
    @property
    def center(self):
        return (int(self.x + self.width/2), int(self.y + self.height/2))
    
    def getTopLeft(self):
        return (self.x, self.y)
    
    @property
    def topleft(self):
        return (self.x, self.y)
    
    def __str__(self):
        return "Rect:" + str(((self.x, self.y), self.width, self.height))
    
    def __repr__(self):
        return self.__str__()
    