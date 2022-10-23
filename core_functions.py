import cv2 as cv
import time
from windowcapture import WindowCapture
from pynput.keyboard import Controller
from vision import Vision
import win32api
import pyautogui
import win32gui, win32ui, win32con, win32api
import threading
import sys

class thread_with_trace(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False
        self._return = None
 
    def start(self):
        self.__run_backup = self.run
        self.run = self.__run     
        threading.Thread.start(self)
 
    def __run(self):
        sys.settrace(self.globaltrace)
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
    
    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:
            return None
    
    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit()
            return self.localtrace
    
    def kill(self):
        self.killed = True
    
    def join(self, *args):
            threading.Thread.join(self, *args)
            return self._return

    def func():
        while True:
            print('thread running')

def fishing_setup():
    dc = win32gui.GetDC(0)
    dcObj = win32ui.CreateDCFromHandle(dc)
    hwnd = win32gui.WindowFromPoint((0,0))
    monitor = (0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))
    state_left = win32api.GetKeyState(0x01)  # Left button up = 0 or 1. Button down = -127 or -128
    done = False
    pressed = False
    while done == False:
        a = win32api.GetKeyState(0x01)
        if a != state_left:  # Button state changed
            state_left = a
            print(a)
            if a < 0:
                print('Left Button Pressed')
                xPosIn, yPosIn = pyautogui.position()
                pressed = True
            else:
                print('Left Button Released')
                xPosFin, yPosFin = pyautogui.position()
                done = True
        if(pressed):
            brush = win32ui.CreateBrush()
            brush.CreateSolidBrush(255)
            dcObj.FrameRect((xPosIn, yPosIn, pyautogui.position().x, pyautogui.position().y), brush)
            win32gui.InvalidateRect(hwnd, monitor, False) # Refresh the entire monitor
        time.sleep(0.001)
    red_nox_thread = thread_with_trace(target = render_rectangle, args = (xPosIn, yPosIn, xPosFin, yPosFin))
    red_nox_thread.start()
    start_fishing_thread = thread_with_trace(target = start_fishing, args = (300 , xPosIn, yPosIn, xPosFin - xPosIn, yPosFin - yPosIn))
    start_fishing_thread.start()
    return [red_nox_thread, start_fishing_thread]

def render_rectangle(xPosIn, yPosIn, xPosFin, yPosFin):
    dc = win32gui.GetDC(0)
    dcObj = win32ui.CreateDCFromHandle(dc)
    hwnd = win32gui.WindowFromPoint((0,0))
    monitor = (0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))
    brush = win32ui.CreateBrush()
    brush.CreateSolidBrush(255)
    while True:
        dcObj.FrameRect((xPosIn, yPosIn, xPosFin, yPosFin), brush)
        win32gui.InvalidateRect(hwnd, monitor, False) # Refresh the entire monitor

def start_fishing(bait_time = 300, xPos = 0, yPos = 0, width = 0, height = 0, red_nox_thread = None):
    keyboard = Controller()
    vision_item = Vision("bait.jpg")
    wincap = WindowCapture(None, xPos, yPos, width, height)
    loop_time = time.time()
    #cv.waitKey(3000)
    #keyboard.press("2")11
    #keyboard.release("2")
    #keyboard.press("1")
    #keyboard.release("1")

    while(True):
        screenshot = wincap.get_screenshot()
        rectangles = vision_item.find(screenshot, 0.8,)
        output_image = vision_item.draw_rectangles(screenshot, rectangles)
        #cv.imshow("Paint", output_image)
        loop_time = time.time()
        
        if cv.waitKey(1) == ord("g"):
            cv.destroyAllWindows()
            break

        if loop_time%int(bait_time) < 2:
            win32api.SetCursorPos(0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
            keyboard.press("2")
            keyboard.release("2")
            keyboard.press("1")
            keyboard.release("1")
    print("End")