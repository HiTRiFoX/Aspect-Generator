import win32gui, win32ui, win32con, win32api
from time import sleep
import pyautogui
import keyboard

window_name = "StreamCraft | Magic"


def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)


def get_inner_windows(window_name):
    whndl = win32gui.FindWindow(None, window_name)
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds


def get_specific_inner_window(hwnd, inner_window_name='MSPaintView'):
    return win32ui.CreateWindowFromHandle(hwnd[inner_window_name])


def get_pixel(x, y):                                                                                     # get HEX color
    global window_name
    w = win32ui.FindWindow(None, window_name)
    dc = w.GetWindowDC()
    color = dc.GetPixel(x, y)
    return color


def click(x, y):
    global window_name
    hwnd = win32gui.FindWindow(0, window_name)
    print("hwnd in 'click' = ", hwnd)
    mouse_position = win32api.MAKELONG(x, y)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, mouse_position)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, mouse_position)


def clicktwo(x, y, hwnd):
    lParam = win32api.MAKELONG(x, y)
    hwnd1 = win32gui.FindWindowEx(hwnd, None, None, None)
    win32gui.PostMessage(hwnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.PostMessage(hwnd1, win32con.WM_LBUTTONUP, None, lParam)


def screenshot():
    global window_name
    if window_name:
        hwnd = win32gui.FindWindow(None, window_name)
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            im.show("lol")
            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im


def bot(x, y, color):
    if get_pixel(x, y) != color:
        click(x, y)


#hwnd = get_inner_windows(window_name)
#clicktwo(300, 300, hwnd['MSPaintView'])

list_window_names()
hwnd = win32gui.FindWindow(None, "")
print("hwnd = ", hwnd)
hwnd = get_inner_windows("")
print(hwnd)
while False:
    clicktwo(900, 400, hwnd)
    sleep(0.1)

while False:
    click(900, 500)
    sleep(1)

# print(get_pixel(900, 400))


# "StreamCraft | Magic"
# {
# Coordinates:
# x, y = 900, 400
#
# Aspects Color HEX:
# 790806 - nothing
# 593169 - fire
# 593169 - dark
# 527118 - air
# 658705 - water
# 593169 - earth
# 593169 - triangle
# }

# "APB Reloaded"
