import ctypes
import numpy as np
import time
import win32api
import win32con
import win32gui

import hoscon


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


def guess_state():
    possible_states = ['STARTMENU',
                       'SELECTIONMENU',
                       'ENDMENU',
                       'EXPMENU',
                       'INACTIVE']
    for state in possible_states:
        conditions = getattr(hoscon.states, state)
        if all([get_pixel_rgb(pos) == rgb for pos, rgb in conditions]):
            return state

    return 'OTHER'


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


def do_at_start_menu():
    x, y = hoscon.pos.SELECTION
    left_click(x, y)


def do_at_selection_menu():
    x, y = hoscon.pos.SORTLVLUP
    left_click(x, y)
    time.sleep(0.5)
    x, y = hoscon.pos.FIRSTHERO
    left_click(x, y)
    time.sleep(0.5)
    x, y = hoscon.pos.START
    left_click(x, y)
    time.sleep(2)


def do_at_end_menu():
    x, y = hoscon.pos.LEAVEEND
    left_click(x, y)


def do_at_exp_menu():
    x, y = hoscon.pos.LEAVEEXP
    left_click(x, y)


def do_at_inactive():
    x, y = hoscon.pos.REJOIN
    left_click(x, y)

def do_at_other():
    x, y = get_attack_pos()
    left_click(x, y)
    time.sleep(0.2)
    keystroke(ord('Z'))
    time.sleep(0.5)
    keystroke(ord('A'))
    time.sleep(0.5)
    left_click(x, y)


def is_enabled():
    return not bool(win32api.GetKeyState(win32con.VK_LCONTROL))


def shady_bot():
    x, y = hoscon.pos.GAMEMENU
    left_click(x, y)
    while is_enabled():
        state = guess_state()
        if state == 'STARTMENU':
            do_at_start_menu()
        elif state == 'SELECTIONMENU':
            do_at_selection_menu()
        elif state == 'ENDMENU':
            do_at_end_menu()
        elif state == 'EXPMENU':
            do_at_exp_menu()
        elif state == 'INACTIVE':
            do_at_inactive()
        else:
            do_at_other()
        time.sleep(1)