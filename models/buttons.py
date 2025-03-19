import cv2
import sys
from .img_identifier import verifyImg
from .mouse import click, mouseOut
from .resource_path import resource_path


SilverChest_img = cv2.imread(resource_path('img/SilverChest.jpg'), cv2.IMREAD_UNCHANGED)  # Carrega a imagem do jeito que ela é, preservando os canais de cor e transparência.
if SilverChest_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem SilverChest. Verifique o caminho.")

Rage_img = cv2.imread(resource_path('img/Rage.jpg'), cv2.IMREAD_UNCHANGED)
if Rage_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem Rage. Verifique o caminho.")

Minigames_Fechar_img = cv2.imread(resource_path('img/Minigames_Fechar.jpg'), cv2.IMREAD_UNCHANGED)
if Minigames_Fechar_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem Minigames_Fechar. Verifique o caminho.")

app = None
SilverChest_count = 0
Rage_count = 0
BonusStage_Failed_count = 0

def silverChest() -> None:
    '''Executa uma verificação de imagem para identificação e execução do Baú Prata'''
    global SilverChest_count

    rectangles = verifyImg(SilverChest_img)
    if len(rectangles) > 0:
        for (x, y, w, h) in rectangles:
            x_mid = int((x + (x + w)) / 2)
            y_mid = int((y + (y + h)) / 2)
            click(x_mid, y_mid)
        mouseOut()
        SilverChest_count += 1
        app.log_message('Baú de Prata resgatado!', fg='green')


def rage() -> None:
    '''Executa uma verificação de imagem para identificação e execução do Modo Fúria'''
    global Rage_count

    rectangles = verifyImg(Rage_img)
    if len(rectangles) > 0:
        for (x, y, w, h) in rectangles:
            x_mid = int((x + (x + w)) / 2)
            y_mid = int((y + (y + h)) / 2)
            click(x_mid, y_mid)
        mouseOut()
        Rage_count += 1
        app.log_message('Modo Fúria ativado!', fg='green')


def minigames_Fechar() -> bool:
    '''Executa uma verificação de imagem para identificação do fechamento por falha nos Minigames'''
    global BonusStage_Failed_count

    rectangles = verifyImg(Minigames_Fechar_img)
    if len(rectangles) > 0:  # Fechar encontrado
        for (x, y, w, h) in rectangles:
            x_Fechar = x + 250
            y_Fechar = y + 32
            click(x_Fechar, y_Fechar)
        mouseOut()
        BonusStage_Failed_count += 1
        app.log_message('Estágio Bônus incompleto!', fg='red')
        return True
    return False