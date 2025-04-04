import numpy as np
import cv2

class Color():
    def __init__(self, *args, **kwargs):
        self.ishsv = kwargs.get("hsv", False)
        if self.ishsv:
            if len(args) == 1 and len(args[0]) == 3:
                self.h, self.s, self.v = args[0]
            elif len(args) == 3:
                self.h, self.s, self.v = args
            else:
                raise Exception("Couldn't create color, use 3 ints.", args)
            self.r, self.g, self.b = cv2.cvtColor(np.uint8([[self.hsv]]), cv2.COLOR_HSV2RGB)[0][0]
        elif len(args) == 1:
            if isinstance(args[0], str):
                self.r = 0
                self.g = 0
                self.b = 0
                match args[0]:
                    case "black":
                        pass
                    case "red":
                        self.r = 255
                    case "blue":
                        self.b = 255
                    case "green":
                        self.g = 255
                    case "white":
                        self.r, self.g, self.b = (255, 255, 255)
            elif len(args[0]) == 3:
                self.r, self.g, self.b = args[0]
        elif len(args) == 3:
            self.r, self.g, self.b = args
        else:
            raise Exception("Couldn't create color, use 3 ints.", args)
            self.h, self.s, self.v = cv2.cvtColor(np.uint8([[self.rgb]]), cv2.COLOR_RGB2HSV)[0][0]
                    
    def getRGB(self):
        return (self.r, self.g, self.b)
    
    @property 
    def rgb(self):
        return (self.r, self.g, self.b)
    
    @property
    def bgr(self):
        return (self.b, self.g, self.r)
    
    @property
    def hsv(self):
        return (self.h, self.s, self.v)        
    
    def getBGR(self):
        return (self.b, self.g, self.r)
    
    def __str__(self):
        if self.ishsv:
            return "Color(HSV):" + str(self.hsv)
        else:
            return "Color:" + str(self.rgb)
