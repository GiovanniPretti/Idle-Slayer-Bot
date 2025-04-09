import cv2
import sys
from time import sleep
from .img_identifier import verifyImg
from .mouse import click, mouseOut
from .resource_path import resource_path


ChestHunt_Saver_img = cv2.imread(resource_path('img/ChestHunt_Saver.jpg'), cv2.IMREAD_UNCHANGED)  # Carrega a imagem do jeito que ela é, preservando os canais de cor e transparência.
if ChestHunt_Saver_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem ChestHunt_Saver. Verifique o caminho.")
ChestHunt_Chest_img = cv2.imread(resource_path('img/ChestHunt_Chest.jpg'), cv2.IMREAD_UNCHANGED)
if ChestHunt_Chest_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem ChestHunt_Chest. Verifique o caminho.")
ChestHunt_Fechar_img = cv2.imread(resource_path('img/ChestHunt_Fechar.jpg'), cv2.IMREAD_UNCHANGED)
if ChestHunt_Fechar_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem ChestHunt_Fechar. Verifique o caminho.")
ChestHunt_PerfectChest_img = cv2.imread(resource_path('img/ChestHunt_PerfectChest.jpg'), cv2.IMREAD_UNCHANGED)
if ChestHunt_PerfectChest_img is None:
    sys.exit("Erro: Não foi possível carregar a imagem ChestHunt_PerfectChest. Verifique o caminho.")

app = None
attack_thread = None
dash_thread = None

ChestHunt_count = 0
ChestHunt_PerfectChest_count = 0

def chestHunt(Crystal_Saver: bool, Saver: bool, Auto_PerfectChest: bool, Fast_ChestHunt: bool) -> None:
    '''Responsável pela identificação e execução da Caça ao Baú'''
    global ChestHunt_count, ChestHunt_PerfectChest_count

    if Saver:
        rectangles_saver = verifyImg(ChestHunt_Saver_img)
        if not len(rectangles_saver) > 0:  # Chest Hunt não encontrada
            return
    else:
        rectangles = verifyImg(ChestHunt_Chest_img)
        if not len(rectangles) > 0: # Chest Hunt não encontrada
            return
            
    # Chest Hunt confirmada
    app.log_message('Caça ao Baú iniciada! Aguarde a conclusão', fg='green')
    app.toggle_threads('Attack', 'OFF')
    app.toggle_threads('Dash', 'OFF')
        
    if Crystal_Saver:
        rectangles = verifyImg(ChestHunt_Chest_img)
        for (x, y, w, h) in rectangles[:2]:
            x_mid = int((x + (x + w)) / 2)
            y_mid = int((y + (y + h)) / 2)
            click(x_mid, y_mid)
            if Fast_ChestHunt:
                sleep(2)
            else:
                sleep(4)

    if Saver:
        for (x, y, w, h) in rectangles_saver:
            x_mid = int((x + (x + w)) / 2)
            y_mid = int((y + (y + h)) / 2)
            click(x_mid, y_mid)
        mouseOut()
    
    rectangles = verifyImg(ChestHunt_Chest_img)
    while len(rectangles) > 0:
        for (x, y, w, h) in rectangles:
            x_mid = int((x + (x + w)) / 2)
            y_mid = int((y + (y + h)) / 2)
            click(x_mid, y_mid)
        mouseOut()
        rectangles = verifyImg(ChestHunt_Chest_img)
        
    for i in range(10):
        rectangles = verifyImg(ChestHunt_Fechar_img)
        if len(rectangles) > 0: 
            for (x, y, w, h) in rectangles:
                x_mid = int((x + (x + w)) / 2)
                y_mid = int((y + (y + h)) / 2)
                click(x_mid, y_mid)
            mouseOut()
            ChestHunt_count += 1
            app.log_message('Caça ao Baú concluída!', fg='green')
            app.toggle_threads('Attack', 'ON')
            app.toggle_threads('Dash', 'ON')
            return
        sleep(0.5)

    if Auto_PerfectChest:
        sleep(3)
        for i in range(30):
            rectangles = verifyImg(ChestHunt_PerfectChest_img)
            if len(rectangles) > 0:
                for (x, y, w, h) in rectangles:
                    x_mid = int((x + (x + w)) / 2)
                    y_mid = int((y + (y + h)) / 2)
                    click(x_mid, y_mid)
                mouseOut()
                sleep(5)
                rectangles = []
                while len(rectangles) == 0:
                    rectangles = verifyImg(ChestHunt_Fechar_img, 0.8)
                    if len(rectangles) > 0:
                        for (x, y, w, h) in rectangles:
                            x_mid = int((x + (x + w)) / 2)
                            y_mid = int((y + (y + h)) / 2)
                            click(x_mid, y_mid)
                        mouseOut()
                        ChestHunt_PerfectChest_count += 1
                        app.log_message('Caça ao Baú Perfeita concluída!', fg='green')
                        app.toggle_threads('Attack', 'ON')
                        app.toggle_threads('Dash', 'ON')
                break
            sleep(0.5)