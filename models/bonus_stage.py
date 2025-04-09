import cv2
import sys
from time import sleep
from .img_identifier import verifyImg
from .mouse import dragClick, mouseOut
from .bonus_stage_run2 import bonusStage_run2
from .resource_path import resource_path


BonusStage_img = cv2.imread(resource_path('img/BonusStage.jpg'), cv2.IMREAD_UNCHANGED)
if BonusStage_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem BonusStage. Verifique o caminho.")
Left_to_Right_img = cv2.imread(resource_path('img/Left_to_Right.jpg'), cv2.IMREAD_UNCHANGED)
if Left_to_Right_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem Left_to_Right. Verifique o caminho.")
Right_to_Left_img = cv2.imread(resource_path('img/Right_to_Left.jpg'), cv2.IMREAD_UNCHANGED)
if Right_to_Left_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem Right_to_Left. Verifique o caminho.")

app = None
attack_thread = None
dash_thread = None

BonusStage_Success_count = 0

def bonusStage(Auto_BonusStage: bool) -> None:
    '''Executa verificações de imagem para identificação e execução do Estágio Bônus'''
    global BonusStage_Success_count

    rectangles = verifyImg(BonusStage_img)
    if len(rectangles) > 0:  # Bonus Stage encontrado
        rectangles = verifyImg(Left_to_Right_img)
        if len(rectangles) > 0:  # Esquerda p Direita encontrado
            for (x, y, w, h) in rectangles:
                fromX = x + int(w * 0.1)  # Ajuste pra 10% da largura do retângulo
                toX = x + int(w * 0.9)  # Ajuste pra 90% da largura do retângulo
                y = int((y + (y + h)) / 2)
                dragClick(fromX, y, toX, y)
            mouseOut()
            if Auto_BonusStage:
                app.log_message('Estágio Bônus iniciado! Aguarde a conclusão', fg='green')
                app.toggle_threads('Attack', 'OFF')
                app.toggle_threads('Dash', 'OFF')
                if bonusStage_run2():
                    BonusStage_Success_count += 1
                    app.log_message('Estágio Bônus concluído!', fg='green')
                sleep(2)
                app.toggle_threads('Attack', 'ON')
                app.toggle_threads('Dash', 'ON')
            else:
                app.toggle_threads('Attack', 'OFF')
                app.toggle_threads('Dash', 'OFF')
                sleep(45)
                app.toggle_threads('Attack', 'ON')
                app.toggle_threads('Dash', 'ON')
            return
        
        rectangles = verifyImg(Right_to_Left_img)
        if len(rectangles) > 0:  # Direita p Esquerda encontrado
            for (x, y, w, h) in rectangles:
                fromX = x + int(w * 0.9) # Ajuste pra 90% da largura do retângulo
                toX = x + int(w * 0.1)  # Ajuste pra 10% da largura do retângulo
                y = int((y + (y + h)) / 2)
                dragClick(fromX, y, toX, y)
            mouseOut()
            if Auto_BonusStage:
                app.log_message('Estágio Bônus iniciado! Aguarde a conclusão', fg='green')
                app.toggle_threads('Attack', 'OFF')
                app.toggle_threads('Dash', 'OFF')
                if bonusStage_run2():
                    BonusStage_Success_count += 1
                    app.log_message('Estágio Bônus concluído!', fg='green')
                sleep(2)
                app.toggle_threads('Attack', 'ON')
                app.toggle_threads('Dash', 'ON')
            else:
                app.toggle_threads('Attack', 'OFF')
                app.toggle_threads('Dash', 'OFF')
                sleep(45)
                app.toggle_threads('Attack', 'ON')
                app.toggle_threads('Dash', 'ON')
            return