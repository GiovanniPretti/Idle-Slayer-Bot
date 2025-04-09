import os
import sys


def resource_path(relative_path: str) -> str:
    '''Retorna o caminho absoluto para os recursos, funcionando tanto no .exe quanto no compilador'''
    if getattr(sys, 'frozen', False):  # No .exe
        base_path = sys._MEIPASS  # Caminho temporário do PyInstaller
    else:  # No compilador
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Pasta raiz do projeto

    full_path = os.path.join(base_path, relative_path)
    return full_path