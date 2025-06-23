#!/usr/bin/env python3

import sys
sys.path.insert(0, "/app/share/pyside6apptemplate") # flatpak path
import os

#PySide6, Qt Designer UI files
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


ui_main = "./src/mainwindow.ui"
path_svg = "./io.github.rfrench3.pyside6-flatpak-template.svg"
path_png = "./io.github.rfrench3.pyside6-flatpak-template.png"

def in_flatpak() -> bool:
    # Checks if the app is running inside a Flatpak sandbox
    return os.path.exists("/.flatpak-info")

def icon_path(path_svg,path_png) -> str:
    # tries to load the svg icon, app falls back to png if it fails
    icon = QIcon(path_svg)
    if icon.isNull():
        path_icon = path_png
    else:
        path_icon = path_svg
    return path_icon

# bundle of ui-launching code
def launch_window(ui_path:str,window_title:str="WindowTitle"):
    # new_window = launch_window(pathToUI,title)
    loader = QUiLoader()
    ui = QFile(ui_path)
    ui.open(QFile.ReadOnly)
    variable_name = loader.load(ui)
    ui.close()

    #set window attributes
    variable_name.setWindowTitle(window_title)
    variable_name.setWindowIcon(QIcon(icon_path(path_svg,path_png)))
    return variable_name

class MainWindowLogic():
    def __init__(self, window): 
        self.window = window

        # connect ui elements to code
        self.button = self.window.findChild(QPushButton,"pushButton")

        # Connect actions to slots or functions
        self.button.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        print("button clicked!")



# Logic that loads the main window
app = QApplication([])

window_main = launch_window(ui_main,"Basic Window")
logic = MainWindowLogic(window_main)

window_main.show()
app.exec()