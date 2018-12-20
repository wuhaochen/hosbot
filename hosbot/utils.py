import ctypes
import numpy as np
import time
import win32api
import win32con
import win32gui


def get_hos_handler():
    keyword = '风暴英雄'
    hwnds = []
    def callback(hwnd, hwnds):
        if keyword in win32gui.GetWindowText(hwnd):
            hwnds.append(hwnd)
            return True

    win32gui.EnumWindows(callback, hwnds)
    if len(hwnds) > 0:
        return hwnds[0]
    else:
        return 0


def left_click(x, y, interval=50):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(interval/1000)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def keystroke(vkcode, interval=50):
    win32api.keybd_event(vkcode, 0, 0, 0)
    time.sleep(interval/1000)
    win32api.keybd_event(vkcode, 0, win32con.KEYEVENTF_KEYUP, 0)


def rgbint2rgbtuple(RGBint):
    blue =  RGBint & 255
    green = (RGBint >> 8) & 255
    red =   (RGBint >> 16) & 255
    return (red, green, blue)


def get_cursor_rgb():
    pos = win32api.GetCursorPos()
    return get_pixel_rgb(pos)


def sample_pixel():
    pos = win32api.GetCursorPos()
    rgb = get_pixel_rgb(pos)
    return pos, rgb


def get_pixel_rgb(pos):
    hwnd = get_hos_handler()
    x, y = pos
    dc = win32gui.GetDC(hwnd)
    rgbint = win32gui.GetPixel(dc, x, y)
    win32gui.ReleaseDC(hwnd, dc)
    return rgbint2rgbtuple(rgbint)


def cycle_pos(n, total=20):
    centerx = 1693
    centery = 947
    r = 85
    each = np.pi*2/total
    theta = (n % total) * each
    xd = int(r * np.cos(theta))
    yd = int(r * np.sin(theta))
    return (centerx + xd, centery + yd)


class CycledPos(object):
    def __init__(self, total=20):
        self.total = total
        self.count = 0

    def __call__(self):
        self.count = (self.count + 1) % self.total
        return cycle_pos(self.count, self.total)


get_attack_pos = CycledPos(30)


def is_keydown(vkcode):
    # https://stackoverflow.com/questions/6331868/using-getkeystate
    return win32api.GetKeyState(vkcode) < 0
