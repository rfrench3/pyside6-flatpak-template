#!/usr/bin/env python3

import sys
sys.path.insert(0, "/app/share/pyside6apptemplate") # flatpak path
import os

#PySide6, Qt Designer UI files
from PySide6.QtWidgets import QApplication, QPushButton #Import widgets here as needed
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile



def in_flatpak() -> bool:
    """Return True if running inside a Flatpak sandbox."""
    return os.environ.get("FLATPAK_SANDBOX_DIR") is not None
        
def launch_window(ui_file:str,window_title:str="WindowTitle"):
    """Launch a new window of the given ui element, optionally set the window title."""
    loader = QUiLoader()
    ui = QFile(ui_file)
    ui.open(QFile.OpenModeFlag.ReadOnly)
    variable_name = loader.load(ui)
    ui.close()

    #set window attributes
    variable_name.setWindowTitle(window_title)
    variable_name.setWindowIcon(icon)
    return variable_name


uipath = "app/share/pyside6apptemplate/" if in_flatpak() else "./src/"

ui_main = uipath + "mainwindow.ui"


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
icon = QIcon.fromTheme("io.github.rfrench3.pyside6-flatpak-template") # this will only load when the app has been installed as a flatpak.

window_main = launch_window(ui_main,"Basic Window")
logic = MainWindowLogic(window_main)

window_main.show()
app.exec()