import cv2
import numpy as np
from .color import Color
from .rect import Rect
from .helpers import parseCoordinates

class Image():
    def __init__(self, src):
        if isinstance(src, np.ndarray):
            self.img = src
        elif isinstance(src, str):
            self.img = cv2.imread(src)
        elif isinstance(src, Image):
            self.img = src.img.copy()
        assert(isinstance(self.img,np.ndarray)), "Something went wrong at Image initialization. Use other Image, ndarray or path as string"
        
    def save(self, name:str):
        cv2.imwrite(name, self.img)
        
    def getSize(self):
        return self.img.shape[0:2][::-1]
    
    @property
    def size(self):
        return self.img.shape[0:2][::-1]

    def getPixelColor(self, *args):
        (x,y), others = parseCoordinates(args)
        b,g,r = (self.img[y,x])
        return Color(r,g,b)
    
    def setPixelColor(self, *args):
        (x,y), others = parseCoordinates(args)
        if isinstance(others[0], Color):
            self.img[y,x] = others[0].bgr
        else:
            raise Exception("Couldn't parse Color, use point and color object", args)
        
    def copy(self, subimg: Rect = None):
        if subimg:
            return Image(self.img[subimg.y:subimg.y+subimg.height, subimg.x:subimg.x+subimg.width])
        else:
            return Image(self.img.copy())
         
    def show(self):
        cv2.imshow('Botpapy image',self.img)
        cv2.moveWindow('Botpapy image', 40,30)
        cv2.waitKey(0)
        try:
            cv2.destroyWindow('Botpapy image')
        except:
            pass
        
    def isolateColorRange(self, c1: Color, c2: Color, keep_color = False):
        if not c1.hsv or not c2.hsv:
            print("Use of HSV colors recommended, use crangeTester!")
        img_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        cmin, cmax = np.zeros(3), np.zeros(3)
        for i, cs in enumerate(zip(c1.hsv, c2.hsv)):
            cmin[i] = min(cs[0], cs[1])
            cmax[i] = max(cs[0], cs[1])
        if not keep_color:
            self.img = cv2.inRange(img_hsv, cmin, cmax)
        else:
            mask = cv2.inRange(img_hsv, cmin, cmax)
            self.img = cv2.bitwise_and(self.img, self.img, mask = mask)
        
