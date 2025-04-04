import numpy as np
import cv2
import tkinter as tk
import tkinter.filedialog

def exitCallback():
    global filename 
    filename = None
    cv2.destroyAllWindows()
    
def setText():
    c1 = (c1min.get(), c2min.get(), c3min.get())
    c2 = (c1max.get(), c2max.get(), c3max.get())
    w.delete(1.0, tk.END)
    w.insert(tk.END, "import botpapy.botpapy as bp\n")
    w.insert(tk.END, "img = bp.Image('"+filename+"')\n")
    w.insert(tk.END, "c1 = bp.Color("+str(c1)+", hsv=True)\n")
    w.insert(tk.END, "c2 = bp.Color("+str(c2)+", hsv=True)\n")
    w.insert(tk.END, "img.isolateColorRange(c1, c2, keep_color=True)\n")
    w.insert(tk.END, "img.show()")

def updateImg(event=None):
    c1 = [c1min.get(), c2min.get(), c3min.get()]
    c2 = [c1max.get(), c2max.get(), c3max.get()]
    # c1 = cv2.cvtColor(np.uint8([[c1]]), cv2.COLOR_BGR2HSV)[0][0]
    # c2 = cv2.cvtColor(np.uint8([[c2]]), cv2.COLOR_BGR2HSV)[0][0]
    for i, cs in enumerate(zip(c1, c2)):
        c1[i] = min(cs[0], cs[1])
        c2[i] = max(cs[0], cs[1])
    global filename
    if filename != None:
        hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsvimg, np.asarray(c1), np.asarray(c2))
        res = cv2.bitwise_and(img, img, mask = mask)
        cv2.imshow('image',res)
        setText()

def setupTk(master):
    master.title('Color Picker')
    master.protocol("WM_DELETE_WINDOW", exitCallback)
    master.geometry("650x475")
    
    c1min = tk.Scale(master, from_=0, to=255, length = 300, orient="horizontal", label="minhue", command=updateImg)
    c2min = tk.Scale(master, from_=0, to=255, length = 300, orient="horizontal", label="minsat", command=updateImg)
    c3min = tk.Scale(master, from_=0, to=255, length = 300, orient="horizontal", label="minval", command=updateImg)

    c1max = tk.Scale(master, from_=0, to=180, length = 300, orient="horizontal", label="maxhue", command=updateImg)
    c2max = tk.Scale(master, from_=0, to=255, length = 300, orient="horizontal", label="maxsat", command=updateImg)
    c3max = tk.Scale(master, from_=0, to=255, length = 300, orient="horizontal", label="maxval", command=updateImg)
    c1max.set(180)
    c2max.set(255)
    c3max.set(255)

    w = tk.Text(master, height=7, borderwidth=2)

    for c in master.children:
        master.children[c].pack()
        
    return c1min,c2min,c3min,c1max,c2max,c3max,w
    
def setupCV(filename):
    img = cv2.imread(filename)
    cv2.imshow('image',img)
    cv2.moveWindow('image', 40,30)
    return img

c1min,c2min,c3min,c1max,c2max,c3max,w,filename,img = [None]*9

def crangeTest(file = None):
    master = tk.Tk()
    global c1min,c2min,c3min,c1max,c2max,c3max,w,img,filename
    c1min,c2min,c3min,c1max,c2max,c3max,w = setupTk(master)
    if file: filename = file
    else: filename = tk.filedialog.askopenfilename()
    img = setupCV(filename)
    setText()
    while filename != None:
        master.update_idletasks()
        master.update()
    master.destroy()

if __name__ == "__main__":
    crangeTest()
