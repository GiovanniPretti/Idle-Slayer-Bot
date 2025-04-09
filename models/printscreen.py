import pyautogui
import numpy as np
import cv2
from typing import Tuple


def new_printscreen() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    '''Captura a tela e retorna a imagem em BGR, Canal Alfa e em Tela Cheia'''
    new_screenshot = pyautogui.screenshot()  # Printa a tela
    new_screenshot_np = np.array(new_screenshot)  # Converte pra NP
    new_screenshot_bgr = cv2.cvtColor(new_screenshot_np, cv2.COLOR_RGB2BGR)  # Converte NP em BGR (RGB em BGR)
    new_alpha_channel = np.ones((new_screenshot_bgr.shape[0], new_screenshot_bgr.shape[1]), dtype=np.uint8) * 255  # Criação canal Alfa
    new_fullscreen_img = cv2.cvtColor(new_screenshot_np, cv2.COLOR_RGB2BGR)
    return new_screenshot_bgr, new_alpha_channel, new_fullscreen_img