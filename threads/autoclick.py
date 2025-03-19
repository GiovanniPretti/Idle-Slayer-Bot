import threading
import pyautogui
from time import sleep


app = None

class AutoClick:
    def __init__(self) -> None:
        self.stop_thread_flag = threading.Event()
        self.thread = None

    def start_thread(self) -> None:
        '''Inicia a thread se ela não estiver em execução'''
        if not self.thread or not self.thread.is_alive():
            self.stop_thread_flag.clear()
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()
            app.log_message(f'Thread "{self.__class__.__name__}" iniciada')
        else:
            app.log_message(f'Thread "{self.__class__.__name__}" já está em execução')

    def stop_thread(self) -> None:
        '''Finaliza a thread se estiver em execução'''
        try:
            if self.thread.is_alive():
                self.stop_thread_flag.set()
                app.log_message(f'Thread "{self.__class__.__name__}" finalizada')
            else:
                app.log_message(f'Thread "{self.__class__.__name__}" não está em execução')
        except AttributeError as e:
            app.log_message(f'Não é possível finalizar a thread "AutoClick" pois ela nunca foi inicializada')
        except Exception as e:
            app.log_message(f'Erro ao tentar finalizar a thread "{self.__class__.__name__}": {e}')

    def run(self) -> None:
        '''Executa o Loop principal da thread'''
        try:
            while not self.stop_thread_flag.is_set():
                pyautogui.click()
                sleep(0.03)
        except Exception as e:
            app.log_message(f'Erro na execução da thread {self.__class__.__name__}: {e}')