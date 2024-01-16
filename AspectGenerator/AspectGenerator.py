import pyautogui as ag
import time as t
import keyboard as kb

# What I want to do:

# check if "There is no space in inventory" in minecraft

# def type //wand
# def if not in Inventory = so open it
# def press Shift + each block
# press Esc


def wand():
    for i in range(35):
        ag.press("t")
        ag.typewrite("//wand")
        ag.press("enter")
        t.sleep(1)


def openn():
    ag.rightClick()


def close():
    ag.press('esc')


def drop():
    ag.press("e")
    t.sleep(1)
    ag.moveTo(670, 800)  # the pos of the first wand
    ag.press("q")
    t.sleep(0.1)
    ag.press("q")
    t.sleep(0.1)
    
    ag.press("q")
    t.sleep(0.5)
    close()


def collect():
    for i in range(35):
        ag.click(900, 420)
        t.sleep(3)


def moveto_chest():
    ag.move(0, -200)


def moveto_craft():
    ag.move(0, 200)


def place_wand():
    ag.keyDown('shift')
    for y in range(4):
        for x in range(9):
            # t.sleep(0.1)
            ag.click(670 + x * 70, 680 + y * 70)
    ag.keyUp('shift')


t.sleep(2)
while not kb.is_pressed("a"):
    wand()
    drop()
    openn()
    t.sleep(0.5)
    place_wand()
    close()
    moveto_craft()
    openn()
    t.sleep(0.5)
    collect()
    close()
    moveto_chest()
