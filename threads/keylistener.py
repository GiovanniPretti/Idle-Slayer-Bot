import threading
from pynput import keyboard
from pynput.keyboard import KeyCode
from models.statistics import statistics


app = None
img_search_thread = None
attack_thread = None
dash_thread = None
auto_click_thread = None

class KeyListener:
    def __init__(self) -> None:
        self.stop_thread_flag = threading.Event()
        self.thread = None
        
    def start_thread(self) -> None:
        '''Inicia a thread se ela não estiver em execução'''
        if not self.thread or not self.thread.is_alive():
            self.stop_thread_flag.clear()
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()
            # app.log_message(f'Thread "{self.__class__.__name__}" iniciada')  # Ativar se necessário
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
            app.log_message(f'Não é possível finalizar a thread "KeyListener" pois ela nunca foi inicializada')
        except Exception as e:
            app.log_message(f'Erro ao tentar finalizar a thread "{self.__class__.__name__}": {e}')

    def run(self) -> None:
        '''Executa o listener do teclado'''
        try:
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
        except Exception as e:
            app.log_message(f'Erro na execução da thread {self.__class__.__name__}: {e}')

    def on_press(self, key: KeyCode) -> None:
        '''Método para tratar pressionamento de teclas'''
        try:
            if hasattr(key, 'vk') and key.vk == 97:  # Numpad1. Ligar Attack
                app.toggle_threads('Attack', 'ON')
            elif hasattr(key, 'vk') and key.vk == 100:  # Numpad4. Desligar Attack
                app.toggle_threads('Attack', 'OFF')
                
            if hasattr(key, 'vk') and key.vk == 98:  # Numpad2. Ligar Dash
                app.toggle_threads('Dash', 'ON')
            elif hasattr(key, 'vk') and key.vk == 101:  # Numpad5. Desligar Dash
                app.toggle_threads('Dash', 'OFF')
                
            elif hasattr(key, 'vk') and key.vk == 99:  # Numpad7. Ligar Verificação de Imagem
                app.toggle_threads('Verificação de Imagem', 'ON')
            elif hasattr(key, 'vk') and key.vk == 102:  # Numpad8. Desligar Verificação de Imagem
                app.toggle_threads('Verificação de Imagem', 'OFF')

            elif hasattr(key, 'vk') and key.vk == 103:  # Numpad3. Ligar AutoClick
                app.toggle_threads('Auto Click', 'ON')
            elif hasattr(key, 'vk') and key.vk == 104:  # Numpad6. Desligar AutoClick
                app.toggle_threads('Auto Click', 'OFF')
                
            elif hasattr(key, 'vk') and key.vk == 105:  # Numpad9. Exibir Estatísticas
                statistics()
        except Exception as e:
            app.log_message(f"Erro ao pressionar tecla: {e}")