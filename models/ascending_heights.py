import cv2
import sys
import keyboard
from time import sleep
from .img_identifier import verifyImg
from .mouse import dragClick, mouseOut
from .resource_path import resource_path


AscendingHeights_img = cv2.imread(resource_path('img/AscendingHeights.jpg'), cv2.IMREAD_UNCHANGED)
if AscendingHeights_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem AscendingHeights. Verifique o caminho.")
Left_to_Right_img = cv2.imread(resource_path('img/Left_to_Right.jpg'), cv2.IMREAD_UNCHANGED)
if Left_to_Right_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem Left_to_Right. Verifique o caminho.")
Right_to_Left_img = cv2.imread(resource_path('img/Right_to_Left.jpg'), cv2.IMREAD_UNCHANGED)
if Right_to_Left_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem Right_to_Left. Verifique o caminho.")

app = None
img_search_thread = None
attack_thread = None
dash_thread = None
AscendingHeights_count = 0

def ascendingHeights() -> bool:
    global AscendingHeights_count

    rectangles = verifyImg(AscendingHeights_img)
    if len(rectangles) > 0:  # Ascending Heights encontrado
        rectangles = verifyImg(Left_to_Right_img)
        if len(rectangles) > 0:  # Esquerda p Direita encontrado
            for (x, y, w, h) in rectangles:
                fromX = x + int(w * 0.1)  # Ajuste pra 10% da largura do retângulo
                toX = x + int(w * 0.9)  # Ajuste pra 90% da largura do retângulo
                y = int((y + (y + h)) / 2)
                dragClick(fromX, y, toX, y)
            mouseOut()
            app.toggle_threads('Attack', 'OFF')
            app.toggle_threads('Dash', 'OFF')
            AscendingHeights_count += 1
            app.log_message('Alturas Ascendentes iniciada. Threads desativadas para conclusão manual\n', fg='green')
            return True
        
        rectangles = verifyImg(Right_to_Left_img)
        if len(rectangles) > 0:  # Direita p Esquerda encontrado
            for (x, y, w, h) in rectangles:
                fromX = x + int(w * 0.9) # Ajuste pra 90% da largura do retângulo
                toX = x + int(w * 0.1)  # Ajuste pra 10% da largura do retângulo
                y = int((y + (y + h)) / 2)
                dragClick(fromX, y, toX, y)
            mouseOut()
            app.toggle_threads('Attack', 'OFF')
            app.toggle_threads('Dash', 'OFF')
            AscendingHeights_count += 1
            app.log_message('Alturas Ascendentes iniciada. Threads desativadas para conclusão manual\n', fg='green')
            return True
    return False