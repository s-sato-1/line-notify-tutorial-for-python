@echo off

pyinstaller main.py --onefile --clean

xcopy settings.ini dist /Y
