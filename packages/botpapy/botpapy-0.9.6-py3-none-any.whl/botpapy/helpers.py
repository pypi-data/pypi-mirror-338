def parseCoordinates(args):
    rest = []
    sw = 0
    for e in args:
        if isinstance(e, tuple):
            if len(e) == 2:
                x,y = e
                sw+= 1
        else:
            rest.append(e)
    if sw == 1:
        return ((x,y),tuple(rest))
    else:
        raise Exception("Couldn't read coordinates from", args)

def is_hex(s):
    try:
        int(str(s), 16)
        return True
    except ValueError:
        return False
    
#https://stackoverflow.com/questions/3354952/python-win32-post-a-click-event-to-a-window    
def MAKELONG(low, high):
    return low | (high << 16)

def add(p1, p2):
    return (p1[0]+p2[0], p1[1]+p2[1])