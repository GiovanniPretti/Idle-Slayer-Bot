import cv2
import numpy as np
from .printscreen import new_printscreen
from typing import List


def verifyImg(Search_img: np.ndarray, threshold: float = 0.9) -> List[List[int]]:
    '''Recebe uma imagem e tenta encontra-la em uma captura da tela do monitor principal, retornando as coordenadas encontradas'''
    screenshot_bgr, alpha_channel, fullscreen_img = new_printscreen()

    if fullscreen_img.shape[2] != Search_img.shape[2]:
        print("Erro: O número de canais da imagem base e da imagem template não correspondem, verificar formatos.")
        return
    
    result = cv2.matchTemplate(fullscreen_img, Search_img, cv2.TM_CCOEFF_NORMED)
    
    height, width = Search_img.shape[:2]
    y_loc, x_loc = np.where(result >= threshold)
    rectangles = []
    for (x, y) in zip(x_loc, y_loc):
        rectangles.append([int(x), int(y), int(width), int(height)])
    
    if len(rectangles) > 1:
        fullscreen_img = cv2.merge([screenshot_bgr, alpha_channel])
        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)   
    return rectangles