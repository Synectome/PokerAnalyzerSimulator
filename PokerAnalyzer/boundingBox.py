# https://stackoverflow.com/questions/3698635/how-to-get-the-text-cursor-position-in-windows
from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}


def captureBoundingBox() -> [int,int]:
    # drag and drop mouse positions to get bounding box
    pass

queryMousePosition()