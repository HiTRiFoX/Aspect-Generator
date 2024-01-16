from time import sleep
import win32gui
import win32api
import win32con

hwndMain = win32gui.FindWindow(None, 'StreamCraft | Magic')

#while True:
temp = win32api.PostMessage(hwndMain, win32con.WM_CHAR, 0x44, 0)
lParam = win32api.MAKELONG(940, 400)
win32api.PostMessage(hwndMain, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
win32api.PostMessage(hwndMain, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)
# print(temp) prints the returned value of temp, into the console
print(temp)
# sleep(1) this waits 1 second before looping through again
sleep(1)
