@echo off
echo Gerando executavel com PyInstaller...

if exist venv call venv\Scripts\activate.bat

REM Deleta os diretorios "dist" e "build" e o arquivo .spec
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist main.spec del /q main.spec

REM Gera o executavel
pyinstaller --onefile --windowed --icon=img/icon.ico --add-data "img;img" main.py

echo.
echo Executavel gerado na pasta "dist" pronto para uso.
pause
