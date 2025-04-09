import cv2
import sys
import pyautogui
from time import sleep
from .img_identifier import verifyImg
from .buttons import minigames_Fechar
from .resource_path import resource_path


BonusStage_SpiritBoost_img = cv2.imread(resource_path('img/BonusStage_SpiritBoost.jpg'), cv2.IMREAD_UNCHANGED)
if BonusStage_SpiritBoost_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem BonusStage_SpiritBoost. Verifique o caminho.")

# Segmento 1
BonusStage2_Seg1_1_img = cv2.imread(resource_path('img/BonusStage2_Seg1_1.jpg'), cv2.IMREAD_UNCHANGED)
if BonusStage2_Seg1_1_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem BonusStage2_Seg1_1. Verifique o caminho.")

# Segmento 2
BonusStage2_Seg2_1_img = cv2.imread(resource_path('img/BonusStage2_Seg2_1.jpg'), cv2.IMREAD_UNCHANGED)
if BonusStage2_Seg2_1_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem BonusStage2_Seg2_1. Verifique o caminho.")

# Segmento 3
BonusStage2_Seg3_1_img = cv2.imread(resource_path('img/BonusStage2_Seg3_1.jpg'), cv2.IMREAD_UNCHANGED)
if BonusStage2_Seg3_1_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem BonusStage2_Seg3_1. Verifique o caminho.")

# Segmento 4
BonusStage2_Seg4_1_img = cv2.imread(resource_path('img/BonusStage2_Seg4_1.jpg'), cv2.IMREAD_UNCHANGED)
if BonusStage2_Seg4_1_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem BonusStage2_Seg4_1. Verifique o caminho.")


def attack_floor(attacks: int=1, jumps: int=1) -> None:
    '''Executa os movimentos e ataques nos goblins nas recompensas do Estágio Bônus'''
    pyautogui.keyDown('w')
    sleep(0.05)
    pyautogui.keyUp('w')
    sleep(0.5)
    pyautogui.press('w')  # Ataque
    sleep(0.6)
    for i in range(jumps):
        pyautogui.press('w')  # Pegar caixa
        sleep(0.6)
    for i in range(attacks):
        pyautogui.keyDown('w')
        sleep(0.05)
        pyautogui.keyUp('w')
        sleep(0.5)
        pyautogui.press('w')  # Ataque
        sleep(0.6)


def bonusStage_run2() -> bool:
    '''Executa uma sequência de funções para conclusão do Estágio Bônus 2'''
    sleep(11.5)
    SpiritBoost = bonusStage_run2_seg1()
    sleep(6.5)
    if not bonusStage_run2_seg2(SpiritBoost):
        return False
    sleep(7)
    if not bonusStage_run2_seg3(SpiritBoost):
        return False
    sleep(9)
    if not bonusStage_run2_seg4(SpiritBoost):
        return False
    sleep(5)
    return True


def bonusStage_run2_seg1() -> bool:
    '''Executa os movimentos do Segmento 1 do Estágio Bônus 2'''
    SpiritBoost = False
    for i in range(2):
        for y in range(30):
            rectangles = verifyImg(BonusStage2_Seg1_1_img, 0.7)
            if len(rectangles) > 0:
                pyautogui.keyDown('w')
                sleep(0.2)
                pyautogui.keyUp('w')
                break
        sleep(1.3)
        pyautogui.press('w')  # Sair do buraquinho
        sleep(1)
        pyautogui.keyDown('w')  # Subir na montanha
        sleep(0.2)
        pyautogui.keyUp('w')
        sleep(0.5)
        for y in range(2):
            rectangles = verifyImg(BonusStage_SpiritBoost_img, 0.7)
            if len(rectangles) > 0:
                SpiritBoost = True
                break
        pyautogui.keyDown('w')  # Subir no topo da montanha
        sleep(0.2)
        pyautogui.keyUp('w')
        sleep(1.2)
        pyautogui.keyDown('w')  # Cair na plataforma central
        sleep(0.2)
        pyautogui.keyUp('w')
        sleep(1.9)
        pyautogui.press('w')  # Pular o segundo buraco
        sleep(0.5)
    for i in range(30):
        rectangles = verifyImg(BonusStage2_Seg1_1_img, 0.8)
        if len(rectangles) > 0:
            pyautogui.keyDown('w')
            sleep(0.2)
            pyautogui.keyUp('w')
            break
    sleep(1.3)
    pyautogui.press('w')  # Sair do buraquinho
    sleep(1)
    pyautogui.keyDown('w')  # Subir na montanha
    sleep(0.2)
    pyautogui.keyUp('w')
    sleep(0.5)
    pyautogui.keyDown('w')  # Subir no topo da montanha
    sleep(0.2)
    pyautogui.keyUp('w')
    sleep(1.2)
    pyautogui.keyDown('w')  # Cair na plataforma central
    sleep(0.2)
    pyautogui.keyUp('w')
    sleep(1.9)
    pyautogui.press('w')  # Pular o segundo buraco
    sleep(2.5)
    attack_floor(3)
    return SpiritBoost


def bonusStage_run2_seg2(SpiritBoost: bool) -> bool:
    '''Executa os movimentos do Segmento 2 do Estágio Bônus 2'''
    if SpiritBoost:
        sleep(2)
        pyautogui.keyDown('w')  # Entrar na caverna
        sleep(0.2)
        pyautogui.keyUp('w')
        sleep(1)
    else:
        sleep(0.4)
        pyautogui.press('w')  # Pular o primeiro buraco
        sleep(1.35)
        pyautogui.keyDown('w')  # Pular o segundo buraco entrando na caverna
        sleep(0.2)
        pyautogui.keyUp('w')
        sleep(1)
    for i in range(3):
        for y in range(30):
            rectangles = verifyImg(BonusStage2_Seg2_1_img, 0.5)
            if len(rectangles) > 0:
                pyautogui.press('w')  # Pular pro degrau do meio da caverna
                break
        sleep(0.5)
        pyautogui.press('w')  # Sair da caverna
        sleep(0.8)
        pyautogui.keyDown('w')  # Subir na montanha
        sleep(0.2)
        pyautogui.keyUp('w')
        sleep(0.65)
        pyautogui.keyDown('w')  # Subir no topo da montanha
        sleep(0.2)
        pyautogui.keyUp('w')
        sleep(0.75)
        pyautogui.keyDown('w')  # Cair na plataforma central
        sleep(0.2)
        pyautogui.keyUp('w')
        sleep(1)
        pyautogui.press('w')  # Pegar moedas
        sleep(0.63)
        pyautogui.keyDown('w')  # Pular o segundo buraco entrando na caverna
        sleep(0.2)
        pyautogui.keyUp('w')
        sleep(1)
    for i in range(30):
        rectangles = verifyImg(BonusStage2_Seg2_1_img, 0.5)
        if len(rectangles) > 0:
            pyautogui.press('w')  # Pular pro degrau do meio da caverna
            break
    sleep(0.5)
    pyautogui.press('w')  # Sair da caverna
    sleep(0.8)
    pyautogui.keyDown('w')  # Subir na montanha
    sleep(0.2)
    pyautogui.keyUp('w')
    sleep(0.65)
    if minigames_Fechar():
        return False
    pyautogui.keyDown('w')  # Subir no topo da montanha
    sleep(0.2)
    pyautogui.keyUp('w')
    sleep(2)
    attack_floor(3)
    return True


def bonusStage_run2_seg3(SpiritBoost: bool) -> bool:
    '''Executa os movimentos do Segmento 3 do Estágio Bônus 2'''
    if SpiritBoost:
        for i in range(30):
            rectangles = verifyImg(BonusStage2_Seg3_1_img, 0.8)
            if len(rectangles) > 0:
                pyautogui.keyDown('w')
                sleep(0.1)
                pyautogui.keyUp('w')
                break
        sleep(0.8)
        pyautogui.press('w')  # Sair do buraquinho
        sleep(2)
        for i in range(6):
            for y in range(30):
                rectangles = verifyImg(BonusStage2_Seg3_1_img, 0.8)
                if len(rectangles) > 0:
                    pyautogui.keyDown('w')
                    sleep(0.2)
                    pyautogui.keyUp('w')
                    break
            sleep(1.25)
        attack_floor(3)
        return True
    else:
        for i in range(5):
            if i == 4:
                if minigames_Fechar():
                    return False
            for y in range(30):
                rectangles = verifyImg(BonusStage2_Seg3_1_img, 0.8)
                if len(rectangles) > 0:
                    pyautogui.keyDown('w')
                    sleep(0.1)
                    pyautogui.keyUp('w')
                    break
            sleep(0.8)
            pyautogui.press('w')  # Sair do buraquinho
            if i != 4:
                sleep(0.75)
                pyautogui.press('w')  # Pegar Moedas
                sleep(1.6)
                pyautogui.press('w')  # Pegar Moedas
                sleep(1.2)
        sleep(1)
        attack_floor(3)
        return True


def bonusStage_run2_seg4(SpiritBoost: bool) -> None:
    '''Executa os movimentos do Segmento 4 do Estágio Bônus 2'''
    if SpiritBoost:
        sleep(1)
        for y in range(50):
            rectangles = verifyImg(BonusStage2_Seg4_1_img, 0.8)
            if len(rectangles) > 0:
                sleep(2.5)
                pyautogui.keyDown('w')  # Pular buraquinho
                sleep(0.1)
                pyautogui.keyUp('w')
                break
        sleep(2.88)
        pyautogui.keyDown('w')  # Pular buraquinho
        sleep(0.2)
        pyautogui.keyUp('w')
        for i in range(5):
            sleep(2.25)
            pyautogui.keyDown('w')  # Pular buraquinho
            sleep(0.2)
            pyautogui.keyUp('w')
            sleep(0.08)
        sleep(2)
        attack_floor(3, 1)
        if minigames_Fechar():
            return False
        return True
    else:
        sleep(2)
        for i in range(3):
            for y in range(30):
                rectangles = verifyImg(BonusStage2_Seg4_1_img, 0.8)
                if len(rectangles) > 0:
                    pyautogui.press('w')
                    break
            sleep(0.9)
            pyautogui.press('w')  # Pegar moedas
            sleep(1.4)
            pyautogui.press('w')  # Pegar moedas
            sleep(1.45)
            pyautogui.keyDown('w')  # Pegar moedas altas
            sleep(0.2)
            pyautogui.keyUp('w')
            if i != 2:
                sleep(1.2)
                pyautogui.press('w')  # Pegar moedas
                sleep(1.4)
                pyautogui.press('w')  # Pegar moedas
                sleep(1.4)
        sleep(2.6)
        attack_floor(3, 2)
        if minigames_Fechar():
            return False
        return True