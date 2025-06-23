#!/usr/bin/env python3

import sys
sys.path.insert(0, "/app/share/pyside6apptemplate") # flatpak path
import os

#PySide6, Qt Designer UI files
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile



def in_flatpak() -> bool:
    # Checks if the app is running inside a Flatpak sandbox
    return os.environ.get("FLATPAK_SANDBOX_DIR") is not None

def app_icon(path_svg,path_png):
    # tries to load the svg icon, app falls back to png if it fails
    icon = QIcon(path_svg)
    if icon.isNull():
        return QIcon(path_png)
    else:
        return icon
        
# bundle of ui-launching code
def launch_window(ui_path:str,window_title:str="WindowTitle"):
    # new_window = launch_window(pathToUI,title)
    loader = QUiLoader()
    ui = QFile(ui_path)
    ui.open(QFile.OpenModeFlag.ReadOnly)
    variable_name = loader.load(ui)
    ui.close()

    #set window attributes
    variable_name.setWindowTitle(window_title)
    variable_name.setWindowIcon(icon)
    return variable_name




ui_main = "./src/mainwindow.ui"
path_svg = "./io.github.rfrench3.pyside6-flatpak-template.svg"
path_png = "./io.github.rfrench3.pyside6-flatpak-template.png"

# logic for the main window

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
#icon = app_icon(path_svg,path_png)
icon = QIcon.fromTheme("io.github.rfrench3.pyside6-flatpak-template")

window_main = launch_window(ui_main,"Basic Window")
logic = MainWindowLogic(window_main)

window_main.show()
app.exec()