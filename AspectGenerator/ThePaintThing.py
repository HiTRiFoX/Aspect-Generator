import win32gui, win32ui, win32con, win32api
from time import sleep
import ctypes


def main():
    # list_window_names()
    # ['MSPaintView']
    window_name = "Untitled - Paint"
    hwnd = win32gui.FindWindow(None, window_name)
    print("hwnd = ", hwnd)
    hwnds = get_inner_windows(hwnd)
    print("hwnds = ", hwnds)
    print("ms = ", hwnds['MSPaintView'])
    win = win32ui.CreateWindowFromHandle(hwnds['MSPaintView'])
    sleep(2)
    clicktwo(500, 500, hwnds['MSPaintView'])
    clicktwo(940, 400, 2448)

'''
    win.SendMessage(win32con.WM_CHAR, ord('A'), 0)
    #win.PostMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    #win.PostMessage(win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    sleep(0.01)
    win.SendMessage(win32con.WM_CHAR, ord('B'), 0)
'''


def click(x, y, hwnd):
    #hwnd = win32gui.FindWindow(0, "Untitled - Paint")
    mouse_position = win32api.MAKELONG(x, y)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, mouse_position)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, mouse_position)


def clicktwo(x, y, hwnd):
    lParam = win32api.MAKELONG(x, y)
    hwnd1 = win32gui.FindWindowEx(hwnd, None, None, None)
    win32gui.SendMessage(hwnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hwnd1, win32con.WM_LBUTTONUP, None, lParam)


def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)


def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds


main()
