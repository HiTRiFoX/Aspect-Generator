import pyautogui as ag
import keyboard as kb
import time as t

ag.FAILSAFE = False

q = 0
while True:
    if kb.is_pressed("q"):
        q += 1
        print(f"q = {q}")
        t.sleep(0.3)
    if q % 2 == 1:
        if ag.pixel(896, 423) != (40, 31, 24):
            ag.click(896, 423)


"""
while not kb.is_pressed("q"):
    if ag.pixel(896, 423) != (40, 31, 24):
        ag.click(896, 423)
"""
