import sys
import os
import json
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from datetime import datetime
from models.resource_path import resource_path


img_search_thread = None
attack_thread = None
dash_thread = None
auto_click_thread = None

class MainWindow:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry("+0+0")
        self.window.protocol('WM_DELETE_WINDOW', self.on_close)  # Executa a função "on_close" ao fechar a janela do TKInter
        
        # Design
        self.window.title('Idle Slayer - Painel de Controle')
        self.window.iconbitmap(resource_path('img/icon.ico'))
        self.window.configure(bg='#101010')
        style = ttk.Style()
        style.configure('TCheckbutton',
                        background='#101010',
                        foreground='white')
        self.label_names = {'Crystal_Saver': 'Salvador de Cristal', 'Saver': 'Salvador', 'Auto_PerfectChest': 'Baú Perfeito automático', 'Fast_ChestHunt': 'Caça ao Baú 2x velocidade', 'Auto_Minions': 'Vassalos automáticos', 
                            'Auto_Rage': 'Modo Fúria automático', 'Auto_BonusStage': 'Estágio Bônus automático', 'Wait_AscendingHeights': 'Alturas Ascendentes Manual'}
        self.help_texts = ['Numpad1 / Numpad4 = Ativa / Desativa o Attack', 'Numpad2 / Numpad5 = Ativa / Desativa o Dash', 'Numpad3 / Numpad6 = Ativa / Desativa a Verificação de Imagem', 
                           'Numpad7 / Numpad8 = Ativa / Desativa o Auto Click', 'Numpad9 = Exibir Estatísticas dessa execução']
        self.toggle_buttons_names = {'Attack': attack_thread, 'Dash': dash_thread, 'Verificação de Imagem': img_search_thread, 'Auto Click': auto_click_thread}
        self.toggle_buttons = {}
         
        # Obtenção dos dados iniciais
        self.folder_path = os.path.join(os.getenv('APPDATA'), 'Giovanni-Pretti', 'RPA_IdleSlayer')
        self.file_path = os.path.join(self.folder_path, 'config.json')
        self.states_bool = self.load_config()  # Recebe as configs do JSON
        self.update_img_search()
        self.states = {}
        for option, state in self.states_bool.items():
            self.states[option] = tk.BooleanVar(value=state)   # Converte bool em tk.BooleanVar para funcionar na interface

        # Configura a interface
        self.setup_ui()

    def setup_ui(self) -> None:
        frame = tk.Frame(self.window, bg='#101010')  # Cria um frame para a label e o button
        frame.pack(anchor='e')

        title_label = tk.Label(
            frame,
            text="Configurações",
            bg='#101010',
            fg='white',
            font=('Arial', 14, 'bold'),
            pady=8)
        title_label.pack(side='left', padx=110)

        button = tk.Button(
            frame,
            text="?",
            bg='#0047AB',
            fg='white',
            font=('Arial', 10, 'bold'),
            width=2,
            activebackground='#666666',
            activeforeground='white',
            command=self.help)
        button.pack(padx=5, pady=5)
        
        # Checkboxes Configurações
        for option, state in self.states.items():  # Itera sobre as opções e para criar os frames, checkboxes e labels dinamicamente
            frame = tk.Frame(self.window, bg='#101010')  # Cria um frame para a label e o checkbox
            frame.pack(anchor='w', padx=40)
            
            checkbox = ttk.Checkbutton(
                frame,
                variable=state,
                onvalue=True,
                offvalue=False,
                style='TCheckbutton',
                command=self.on_checkbox_click)
            checkbox.pack(side='left', anchor='w')

            label = tk.Label(
                frame,
                text=self.label_names[option],
                bg='#101010',
                fg='white')
            label.pack(side='left')

        # Button Atualizar Opções
        self.att_states_button = tk.Button(
            self.window, 
            text='Atualizar Opções',
            bg='#444444',
            fg='white',
            font=('Arial', 10, 'bold'),
            activebackground='#666666',
            activeforeground='white',
            command=self.update_json
        )
        self.att_states_button.pack(pady=10)
        
        separator = ttk.Separator(self.window)
        separator.pack(fill='x', pady=(0, 10))
        
        # Buttons Toggle Threads
        for text in self.toggle_buttons_names.keys():
            frame = tk.Frame(self.window, bg='#101010')  # Cria um frame para a label e o button
            frame.pack(anchor='w', padx=30)
            
            self.toggle_buttons[text] = tk.Button(
                frame,
                text='OFF',
                bg='#C30010',
                fg='white',
                font=('Arial', 10),
                width=6,
                activebackground='#666666',
                activeforeground='white',
                command=lambda text=text: self.on_toggle_button_click(text))  # Passa a função sem executar na criação do botão
            self.toggle_buttons[text].pack(side='left', padx=10)
            
            label = tk.Label(
                frame, 
                text=text, 
                bg='#101010', 
                fg='white',
                font=('Arial', 10))
            label.pack(anchor='w')
        
        self.toggle_buttons['Auto Click'].config(state='disabled')  # Desativa Click no botão do Auto Click para funcionar apenas pelo Keylistener
        
        # Criar o console usando scrolledtext.Text
        self.console = scrolledtext.ScrolledText(
            self.window,
            wrap=tk.WORD,
            state='disabled',
            bg='#171717',
            fg='white',
            width=55,
            font=('Arial', 9))
        self.console.pack(pady=(10, 0), expand=True, fill='both')
        self.console.tag_configure('green', foreground='#00FF00')
        self.console.tag_configure('red', foreground='red')


    def on_checkbox_click(self) -> None:
        '''Remove o foco do checkbox para evitar o contorno de seleção ao clicar'''
        self.att_states_button.focus_set()
        
        
    def on_toggle_button_click(self, button_name: str) -> None:
        '''Alterna o estado do botão e inicia/finaliza a Thread correspondente'''
        btn = self.toggle_buttons[button_name]
        if btn['text'] == 'OFF':
            btn.config(text='ON', bg='#008000')
            self.toggle_buttons_names[button_name].start_thread()
        else:
            btn.config(text='OFF', bg='#C30010')
            self.toggle_buttons_names[button_name].stop_thread()
        
            
    def toggle_threads(self, button_name: str, turn: str, toggle_thread: bool=True) -> None:
        '''Alterna o estado do botão referente ao atalho executado'''
        if toggle_thread:
            if turn == 'ON':
                self.toggle_buttons_names[button_name].start_thread()
            elif turn == 'OFF':
                self.toggle_buttons_names[button_name].stop_thread()
        btn = self.toggle_buttons[button_name]
        if turn == 'ON' and btn['text'] == 'OFF':
            btn.config(text='ON', bg='#008000')
        elif turn == 'OFF' and btn['text'] == 'ON':
            btn.config(text='OFF', bg='#C30010')
       
     
    def help(self) -> None:
        '''Exibe os atalhos das threads no console'''
        self.log_message('================ Atalhos ================', jump_line=True, show_time=False)
        for pos, text in enumerate(self.help_texts):
            if pos == len(self.help_texts) - 1:  # última Iteração
                self.log_message(f'{text}\n', show_time=False)
            else:
                self.log_message(text, show_time=False)
        

    def get_time(self) -> str:
        '''Retorna o horário atual'''
        return datetime.today().strftime('%H:%M:%S - ')


    def log_message(self, message: str, jump_line: bool=False, show_time: bool=True, fg=None) -> None:
        '''Envia no console a mensagem passada como parâmetro'''
        self.console.bind('<Button-1>', lambda e: 'break')  # Impede clique no console
        self.console.configure(state='normal')  # Habilitar edição para inserir texto
        if jump_line:
            last_line_index = self.console.index('end-1c linestart')  # Numero da linha da linha atual do console
            last_line_index = int(last_line_index.replace('.0', '')) - 1  # Tratamento para a última linha. De "x.0" Str para "x-1" Int
            last_line = self.console.get(f'{last_line_index}.0', 'end-1c')  # Retorna o texto da última linha
            if last_line.strip() != '':  # Verifica se a linha não está vazia
                self.console.insert('end', '\n')
        if fg:
            self.console.insert(tk.END, f'{self.get_time() if show_time else ""}{message}\n', fg)  # Envia a mensagem
        else:
            self.console.insert(tk.END, f'{self.get_time() if show_time else ""}{message}\n')  # Envia a mensagem
        self.console.see(tk.END)  # Rolagem para a última linha
        self.console.configure(state='disabled')  # Desabilitar edição novamente


    def create_json(self) -> None:
        '''Cria o arquivo JSON com as configurações padrão'''
        default_config = {'Crystal_Saver': False, 'Saver': False, 'Auto_PerfectChest': False, 'Fast_ChestHunt': False, 
                          'Auto_Minions': False, 'Auto_Rage': False, 'Auto_BonusStage': False, 'Wait_AscendingHeights': False}
        if not os.path.exists(self.folder_path): 
            os.makedirs(self.folder_path)
        with open(self.file_path, 'w') as file:
            json.dump(default_config, file, indent=4)


    def load_config(self) -> dict:
        '''Carrega o arquivo de configuração ou retorna um dicionário padrão, cria o arquivo caso não exista'''
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.create_json()
            return self.load_config()


    def update_json(self) -> None:
        '''Salva as configurações atuais no arquivo JSON, cria o arquivo caso não exista'''
        try:
            with open(self.file_path, 'w') as file:
                for option in self.states.keys():
                    self.states_bool[option] = self.states[option].get()  # Converte tk.BooleanVar em bool para salvar no JSON
                self.update_img_search()
                json.dump(self.states_bool, file, indent=4)
                self.log_message('Variáveis atualizadas.')
        except (FileNotFoundError, json.JSONDecodeError):
            self.create_json()
            self.update_json()


    def update_img_search(self) -> None:
        '''Atualiza os atributos da thread de verificação de imagem'''
        for option, state in self.states_bool.items():
            setattr(img_search_thread, option, state)


    def on_close(self) -> None:
        '''Método chamado ao fechar a janela para encerrar a execução completamente'''
        self.log_message('Encerrando a execução devido ao fechamento da interface...')
        sys.exit()