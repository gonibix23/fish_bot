import cv2 as cv
import numpy as np
from time import time
from PIL import ImageGrab
from windowcapture import WindowCapture
from pynput.keyboard import Key, Controller
from vision import Vision
import win32api
import pyautogui
import win32gui, win32ui, win32con, win32api
import tkinter

keyboard = Controller()

#WindowCapture.list_window_names()

vision_item = Vision("albion_cabbage7.jpg")

#vision_item.init_control_gui()
def startFishing():
    seleccionPantalla = 0
    xPos1, xPos2, yPos1, yPos2 = (0,0,0,0)
    state_left = win32api.GetKeyState(0x01)
    loop_time = time()
    cv.waitKey(3000)
    keyboard.press("2")
    keyboard.release("2")
    keyboard.press("1")
    keyboard.release("1")
    while(True):
        while(seleccionPantalla == 0):
            leftClick = win32api.GetKeyState(0x01)
            if leftClick != state_left:  # Button state changed
                state_left = leftClick
                print(leftClick)
                if leftClick < 0:
                    xPos1, yPos1 = pyautogui.position()
                else:
                    xPos2, yPos2 = pyautogui.position()
                    wincap = WindowCapture(None, xPos2-xPos1, yPos2-yPos1, xPos1, yPos1)
                    seleccionPantalla = 1

        screenshot = wincap.get_screenshot()

        #processed_image = vision_item.apply_hsv_filter(screenshot)

        rectangles = vision_item.find(screenshot, 0.8, xPos1, yPos1)

        output_image = vision_item.draw_rectangles(screenshot, rectangles)

        cv.imshow("Paint", output_image)
        #cv.imshow("Processed", processed_image)


        print("FPS {}".format(1/ (time() - loop_time)))
        loop_time = time()

        if cv.waitKey(1) == ord(str(entryExitKey.get())):
            cv.destroyAllWindows()
            break
        print(loop_time%int(entryBaitNum.get()))
        if loop_time%int(entryBaitNum.get()) < 2:
            win32api.SetCursorPos((xPos1+(xPos2-xPos1), yPos1+(yPos2-yPos1)))
            xPos, yPos = pyautogui.position()
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,xPos1+(xPos2-xPos1),yPos1+(yPos2-yPos1),0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,xPos1+(xPos2-xPos1),yPos1+(yPos2-yPos1),0,0)
            keyboard.press("2")
            keyboard.release("2")
            keyboard.press("1")
            keyboard.release("1")

    print("Done.")



ventana = tkinter.Tk()
ventana.geometry("400x200")
ventana.title("Paint 3D")

labelBait = tkinter.Label(ventana, text="Introduce Time Between Baits")
labelBait.pack()
entryBaitNum = tkinter.Entry(ventana)
entryBaitNum.pack()
labelExit = tkinter.Label(ventana, text="Introduce Key To Exit The Program Once Started")
labelExit.pack()
entryExitKey = tkinter.Entry(ventana)
entryExitKey.pack()
botonStart = tkinter.Button(ventana, text="START FISHING", bd=2 , command = startFishing)
botonStart.pack(pady=30)


ventana.mainloop()