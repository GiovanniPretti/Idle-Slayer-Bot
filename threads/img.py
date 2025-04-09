import threading
from time import sleep
from models.chest_hunt import chestHunt
from models.bonus_stage import bonusStage
from models.ascending_heights import ascendingHeights
from models.minions import minions
from models.buttons import silverChest, rage, minigames_Fechar


app = None

class ImgSearch:
    def __init__(self) -> None:
        self.stop_thread_flag = threading.Event()
        self.thread = None
        self.Crystal_Saver = False
        self.Saver = False
        self.Auto_PerfectChest = False
        self.Fast_ChestHunt = False
        self.Auto_Minions = False
        self.Auto_Rage = False 
        self.Auto_BonusStage = False
        self.Wait_AscendingHeights = False

    def start_thread(self) -> None:
        '''Inicia a thread se ela não estiver em execução'''
        if not self.thread or not self.thread.is_alive():
            self.stop_thread_flag.clear()
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()
            app.log_message(f'Thread "Verificação de Imagem" iniciada')
        else:
            app.log_message(f'Thread "Verificação de Imagem" já está em execução')

    def stop_thread(self) -> None:
        '''Finaliza a thread se estiver em execução'''
        try:
            if self.thread.is_alive():
                self.stop_thread_flag.set()
                if self.thread is not None:
                    self.thread.join()
                app.log_message(f'Thread "Verificação de Imagem" finalizada')
            else:
                app.log_message(f'Thread "Verificação de Imagem" não está em execução')
        except AttributeError as e:
            app.log_message(f'Não é possível finalizar a thread "Verificação de Imagem" pois ela nunca foi inicializada')
        except Exception as e:
            app.log_message(f'Erro ao tentar finalizar a thread "Verificação de Imagem": {e}')

    def run(self) -> None:
        '''Executa o Loop principal da thread'''
        try:
            while not self.stop_thread_flag.is_set():
                chestHunt(self.Crystal_Saver, self.Saver, self.Auto_PerfectChest, self.Fast_ChestHunt)
                bonusStage(self.Auto_BonusStage)
                minigames_Fechar()
                if self.Wait_AscendingHeights:
                    if ascendingHeights():
                        self.stop_thread_flag.set()
                        app.toggle_threads('Verificação de Imagem', 'OFF', False)
                silverChest()
                if self.Auto_Minions:
                    minions()
                if self.Auto_Rage:
                    rage()
                sleep(1)
        except Exception as e:
            app.log_message(f'Erro na execução da thread {self.__class__.__name__}: {e}')