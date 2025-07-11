"""This file contains functions that make it simpler to load elements, including .ui widgets from Qt Designer."""


from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader



# This will only load the app icon from the theme, which happens automatically when installed as a flatpak
app_icon = QIcon.fromTheme("io.github.rfrench3.pyside6apptemplate")


def load_widget(ui_file: str, window_title:str='Scopebuddy GUI', icon:QIcon=app_icon):
    """Load a widget from a UI file and return it.
    Handles widgets as windows and widgets loaded into windows."""
    loader = QUiLoader()
    ui = QFile(ui_file)
    ui.open(QFile.OpenModeFlag.ReadOnly)
    widget = loader.load(ui)
    ui.close()
    if widget.isWindow():
        # set window attributes
        widget.setWindowTitle(window_title)
        widget.setWindowIcon(icon) #type:ignore
    return widget

def load_message_box(parent_window,title:str,  text:str,  icon:QMessageBox.Icon=QMessageBox.Icon.Information,  standard_buttons:QMessageBox.StandardButton=QMessageBox.StandardButton.Ok) -> QMessageBox.StandardButton:
    """Loads a QMessageBox, returns the result of exec()."""
    msg = QMessageBox(parent_window)
    msg.setIcon(icon)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setStandardButtons(standard_buttons)
    return msg.exec() #type:ignore