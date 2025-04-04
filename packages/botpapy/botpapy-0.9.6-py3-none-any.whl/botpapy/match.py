from .rect import Rect

class Match():
    def __init__(self, rect: Rect, score):
        self.rect = rect
        self.score = score
    
    def getRect(self):
        return self.rect
    
    def getCenter(self):
        return self.rect.getCenter()
    
    def __str__(self):
        return "Match:" + str([self.rect, self.score])
    
    def __repr__(self):
        return self.__str__()
    
    @property
    def center(self):
        return self.rect.center
