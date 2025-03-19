import pyautogui
import win32api, win32con
from time import sleep


def click(x: int, y: int) -> None:
    '''Executa um clique no X e Y informado'''
    win32api.SetCursorPos((x, y))
    sleep(0.1)
    pyautogui.click() 
    sleep(0.1)  # Para não spammar tão rapido na Caça ao Baú


def dragClick(fromX: int, fromY: int, toX: int, toY: int) -> None:
    '''Executa um drag click (arrastar e soltar) entre as coordenadas iniciais e finais'''
    win32api.SetCursorPos((fromX, fromY))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    pyautogui.moveTo(toX, toY, duration=0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def mouseOut() -> None:
    '''Move o mouse para coordenada (0, 0) para evitar conflitos'''
    win32api.SetCursorPos((0, 0))