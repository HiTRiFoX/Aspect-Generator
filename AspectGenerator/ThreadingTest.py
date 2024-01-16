import pywinauto, win32api


all = pywinauto.findwindows.find_elements()
print("all = ", all)

win = pywinauto.findwindows.find_window(title_re='StreamCraft | Magic')

print("win = ", win)



mouse_pos = win32api.GetCursorPos()

app = pywinauto.Application().connect(handle=win)
app.StreamCraft.click_input(coords=(900, 420))
#app.StreamCraft.minimize()

win32api.SetCursorPos(mouse_pos)

# 'StreamCraft | Magic'
# <win32_element_info.HwndElementInfo - 'StreamCraft | Magic', LWJGL, 4457582>
# process=2448