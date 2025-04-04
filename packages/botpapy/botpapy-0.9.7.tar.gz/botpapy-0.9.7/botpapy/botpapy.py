import numpy as np
import cv2

# Window class imports
import win32gui
import win32ui
import win32api, win32con
from PIL import Image as PILImage
from ctypes import windll
import time
from .helpers import parseCoordinates, is_hex, MAKELONG, add
from .config import CLICK_TIMEOUT, SYNC_MSG

from .crangeTester import crangeTest
from .color import Color
from .rect import Rect
from .match import Match
from .image import Image
from .selectWindow import checkWindowNames, listWindows

class Window():
    def __init__(self, name, layer = 1):
        self.name = name
        self.layer = layer
        if is_hex(self.name) and not isinstance(self.name, str):
            self.hwnd = self.name
        else:
            self.hwnd = checkWindowNames(self.name, layer)
      
    def takeScreenshot(self):
        # <3 to hazzey
        # https://stackoverflow.com/questions/19695214/screenshot-of-inactive-window-printwindow-win32gui
        hwnd = self.hwnd
        if not hwnd:
            raise Exception("No Window handle found.")
        
        windll.user32.SetProcessDPIAware()
        left, top, right, bot = win32gui.GetClientRect(hwnd)
        w = right - left
        h = bot - top

        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

        saveDC.SelectObject(saveBitMap)

        result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), self.layer)

        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        img = PILImage.frombuffer('RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1) 

        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwndDC)

        if result != 1:
            print("Screenshot not successful.")
            return None
            
        return Image(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
            
    def mouseClick(self, *args, button="left"): #, synchronous=False
        (x,y), other = parseCoordinates(args)
        match button:
            case "left":
                win32buttondown = win32con.WM_LBUTTONDOWN
                win32buttonup = win32con.WM_LBUTTONUP
                win32msg = win32con.MK_LBUTTON
            case "right":
                win32buttondown = win32con.WM_RBUTTONDOWN
                win32buttonup = win32con.WM_RBUTTONUP
                win32msg = win32con.MK_RBUTTON
            case "middle":
                win32buttondown = win32con.WM_MBUTTONDOWN
                win32buttonup = win32con.WM_MBUTTONUP
                win32msg = win32con.MK_MBUTTON
            case _:
                raise Exception("Couldn't parse mouse button, use 'left', 'right' or 'middle'", args)

        if not SYNC_MSG:
            win32gui.PostMessage(self.hwnd,win32buttondown, win32msg, MAKELONG(x,y)) #win32con.MK_LBUTTON
            time.sleep(CLICK_TIMEOUT)
            win32gui.PostMessage(self.hwnd,win32buttonup, 0, MAKELONG(x,y))
        else:
            win32gui.SendMessage(self.hwnd,win32buttondown, win32msg, MAKELONG(x,y))
            time.sleep(CLICK_TIMEOUT)
            win32gui.SendMessage(self.hwnd,win32buttonup, 0, MAKELONG(x,y))
        
    def click(self, tpl, trsh):
        matches = findMatches(self.takeScreenshot(), tpl, trsh, 1)
        if len(matches) == 0:
            print("No match to click found.")
            return
        self.mouseClick(matches[0].center)
        
    def moveMouse(self, *args):
        x,y, other = parseCoordinates(args)
        # WM_MOUSEHOVER, WM_MOUSEMOVE
        if not SYNC_MSG:
            win32gui.PostMessage(self.hwnd,win32con.WM_MOUSEMOVE, 0, MAKELONG(x,y))
        else:
            win32gui.SendMessage(self.hwnd,win32con.WM_MOUSEMOVE, 0, MAKELONG(x,y))

    def hoverMouse(self, *args):
        (x,y), other = parseCoordinates(args)
        if isinstance(other[0], int):
            iter = other[0]
        else:
            raise Exception("Couldn't parse hoverMouse input, use (x,y), iters", args)
        for _ in range(0,iter):
            for d in [(0,-1), (1,0), (0,1), (-1,0)]:
                win32gui.PostMessage(self.hwnd,win32con.WM_MOUSEMOVE, 0, MAKELONG(x+d[0],y+d[1]))
                win32gui.PostMessage(self.hwnd,win32con.WM_MOUSEMOVE, 0, MAKELONG(x,y))
                
    def pressButtons(self, s: str):
        for c in s:
            c = win32api.VkKeyScan(c)
            #WM_CHAR
            # up or down?
            if not SYNC_MSG:
                win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, c, 0)
            else:
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, c, 0)

    def holdButton(self, c: str, time):
        # is blocking -> this bad?
        if len(c) != 1:
            raise Exception("Only can hold one button.", c)
        c = win32api.VkKeyScan(c)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, c, 0)
        time.sleep(time)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, c, 0)
        

def findMatches(img:Image, tpl:Image, trsh, max:int):
    matches = []
    res = cv2.matchTemplate(img.img,tpl.img,cv2.TM_CCOEFF_NORMED)
    res_1d = res.flatten()
    idx_1d = np.argpartition(res_1d, -max)[-max:]
    y_idx, x_idx = np.unravel_index(idx_1d, res.shape)
    for e in zip(x_idx, y_idx):
        if (c:= res[e[::-1]]) > trsh:
            r = Rect(e, *tpl.getSize())
            matches.append(Match(r, c))
    return matches
        
def markMatches(img:Image, matches, color:Color, thickness:int = 2):
    for m in matches:
        p = m.rect.getTopLeft()
        cv2.rectangle(img.img, p, (p[0]+m.rect.width, p[1]+m.rect.height), color.bgr, thickness)
