import win32gui, win32ui
from ctypes import windll
from PIL import ImageTk, Image as PILImage
import tkinter as tk

def listWindows(visible = False):
    def enumHandler(hwnd, ctx):
        if visible:
            if win32gui.IsWindowVisible(hwnd):print(hex(hwnd), win32gui.GetWindowText(hwnd))
        else:
            print(hex(hwnd), win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(enumHandler, None)

def checkWindow(hwnd, layer):
        left, top, right, bot = win32gui.GetClientRect(hwnd)
        w = right - left
        h = bot - top

        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

        saveDC.SelectObject(saveBitMap)

        result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), layer)

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
            return None
        else:
            return img
    
        
def getImage(img, root):
    width, height = img.size
    img = img.resize((round(550/height*width) , round(550)))
    imgtk = ImageTk.PhotoImage(img,master = root)
    return imgtk

def selectWindow(windows: dict):
    i = 0
    res = None
    keyList=sorted(windows.keys())
    images = []
    root = tk.Tk()
    root.geometry("1200x680")
    for k in keyList:
        images.append(getImage(windows[k], root))
        
    def exitCallback():
        root.destroy()
        nonlocal res
        res = None
    root.protocol("WM_DELETE_WINDOW", exitCallback)    
    ltop = tk.Label(root, text="1/" + str(len(keyList)))
    label = tk.Label(root, image=images[0])
    lbot = tk.Label(root, text=keyList[i])
    info = tk.Label(root, text="Please select a window with the arrow keys/WASD and confirm with Space.")
    
    for c in root.children:
        root.children[c].pack(pady = 5)
        
    def on_resize(event):
        width = event.width
        height = event.height
        root.config(width=width, height=height)
        for im in images:
                im_width, im_height = im.size
                im = im.resize((round(550/im_height*im_width) , round(550)))
        label["image"] = images[i]

    def leftKey(event = None):
        nonlocal i
        i = i-1 if i > 0 else len(keyList)-1
        ltop["text"] = str(i+1) + "/" + str(len(keyList))
        label["image"] = images[i]
        lbot["text"] = keyList[i]

    def rightKey(event = None):
        nonlocal i
        i = i+1 if i < len(keyList)-1 else 0
        ltop["text"] = str(i+1) + "/" + str(len(keyList))
        label["image"] = images[i]
        lbot["text"] = keyList[i]
        
    def confirmCallback(event = None):
        root.destroy()
        nonlocal res
        res = keyList[i] #keyList[i]
    
    root.bind('<Left>', leftKey)
    root.bind('<Right>', rightKey)
    root.bind("a", leftKey)
    root.bind("d", rightKey)
    root.bind('<Return>', confirmCallback)
    # root.bind("<Configure>",on_resize)
    root.mainloop()
    if res != None:
        return res
    else:
        raise Exception("No window selected")
    
    
def checkWindowNames(name: str = "", layer = 1):
    handles = []
    def enumHandler(hwnd, ctx):
        if name in win32gui.GetWindowText(hwnd):
            handles.append(hwnd)
    win32gui.EnumWindows(enumHandler, None)
    if len(handles) == 0:
        raise Exception("No window with this name found.")
    if (len(handles)) == 1:
        return handles[0]
    if(len(handles)) > 1:
        res = {}
        for h in handles:
            res[hex(h)] = checkWindow(h, layer)
        return int(selectWindow(res),16)

if __name__ == "__main__":
    res = checkWindowNames("Edge", 3)
    print(hex(res))