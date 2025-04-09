import cv2
import sys
import pyautogui
from time import sleep
from .img_identifier import verifyImg
from .mouse import click, mouseOut
from .resource_path import resource_path


Minions1_img = cv2.imread(resource_path('img/Minions1.jpg'), cv2.IMREAD_UNCHANGED)  # Carrega a imagem do jeito que ela é, preservando os canais de cor e transparência.
if Minions1_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem Minions1. Verifique o caminho.")
Minions2_img = cv2.imread(resource_path('img/Minions2.jpg'), cv2.IMREAD_UNCHANGED)
if Minions2_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem Minions2. Verifique o caminho.")
Minions3_img = cv2.imread(resource_path('img/Minions3.jpg'), cv2.IMREAD_UNCHANGED)
if Minions3_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem Minions3. Verifique o caminho.")
Minions4_img = cv2.imread(resource_path('img/Minions4.jpg'), cv2.IMREAD_UNCHANGED)
if Minions4_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem Minions4. Verifique o caminho.")
Minions5_img = cv2.imread(resource_path('img/Minions5.jpg'), cv2.IMREAD_UNCHANGED)
if Minions5_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem Minions5. Verifique o caminho.")

app = None

def minions() -> None:
    '''Executa a coleta e reposição dos Vassalos'''
    rectangles = verifyImg(Minions1_img, 0.95)
    if len(rectangles) > 0:  # Vassalo finalizado confirmado
        for (x, y, w, h) in rectangles:
            x_mid = int((x + (x + w)) / 2)
            y_mid = int((y + (y + h)) / 2)
            click(x_mid, y_mid)
        sleep(1)

        rectangles = verifyImg(Minions2_img, 0.8)  # Botão da Aba dos Vassalos
        for (x, y, w, h) in rectangles:
            x_mid = int((x + (x + w)) / 2)
            y_mid = int((y + (y + h)) / 2)
            click(x_mid, y_mid)
        sleep(1)

        rectangles = verifyImg(Minions3_img, 0.5)  # Botão "Reivindicar Tudo"
        for (x, y, w, h) in rectangles:
            x_mid = int((x + (x + w)) / 2)
            y_mid = int((y + (y + h)) / 2)
            click(x_mid, y_mid)
        sleep(0.4)
        if len(rectangles) > 0:
            pyautogui.click()  # Botão "Enviar Todos"

        rectangles = verifyImg(Minions5_img)  # Botão "X" (Fechar)
        for (x, y, w, h) in rectangles:
            x_mid = int((x + (x + w)) / 2)
            y_mid = int((y + (y + h)) / 2)
            click(x_mid, y_mid)
        mouseOut()

        app.log_message('Vassalos recolhidos e reenviados!', fg='green')