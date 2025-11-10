#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only

"""
PySide6 Flatpak Template

Created in 2025 by rfrench3 (TealMango) - https://github.com/rfrench3

Licensed under the GNU GPLv3 only. See LICENSE file in the project root for full license information.
"""

"""
This template provides a basic example of a main window, a significantly more advanced example, 
useful functions for loading widgets, and has many comments to help people trying to learn how 
to make Flatpaks and/or use PySide6.

type:ignore is used because self.window.findChild() is able to either output None or the class of the widget. 
It should never output None unless something has gone horribly wrong, so the possibility of None is often ignored.
"""

import sys

# locating other application files
sys.path.insert(0, "/app/share/pyside6apptemplate")  # flatpak path
from program_file_locator import DATA_DIR
from widget_manager import app_icon, load_widget, load_message_box

# PySide6, Qt Designer UI files
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QTabWidget,
    QToolButton,
    QScrollArea,
    QWidget,
)  # Import widgets here as needed

# Not all elements that you may use are in PySide6.QtWidgets
from PySide6.QtGui import QAction

# Edit the .ui file using Qt Designer, pathlib.Path is used here
ui_main = DATA_DIR / "main_window.ui"
ui_advanced = DATA_DIR / "advanced_main_window.ui"
ui_dynamic = DATA_DIR / "dynamic.ui"


# logic for the basic main window
class MainWindow:
    def __init__(self, ui_file):
        self.window = load_widget(
            ui_file,
            "Application Main Window",
            app_icon,  # defaults to app_icon if not specified, this only needs to be set for custom icons
        )  # it is only set here for example, there is no difference if it is excluded

        # Initialize UI Elements
        self.load_message_box: QPushButton = self.window.findChild(
            QPushButton, "load_message_box"
        )  # type:ignore
        self.load_advanced_window: QPushButton = self.window.findChild(
            QPushButton, "load_advanced_window"
        )  # type:ignore

        # Connect actions to slots or functions
        self.load_message_box.clicked.connect(self.button_clicked)
        self.load_advanced_window.clicked.connect(self.launch_advanced_ui)

        self.window.show()  # must be at the end of the __init__

    def button_clicked(self):
        """Loads a QMessageBox."""
        load_message_box(self.window, "message box title!", "message box text!")

    def launch_advanced_ui(self):
        """Launches the more advanced example of a main window as a separate window."""
        self.advanced_window = AdvancedMainWindow(ui_advanced)


# Logic for the advanced main window (same as the regular main window, but with a lot of additional widgets)
class AdvancedMainWindow:
    def __init__(self, ui_file):
        self.window = load_widget(ui_file, "Advanced Main Window")

        # Initialize UI elements
        self.top_tab: QTabWidget = self.window.findChild(
            QTabWidget, "tabWidget_top"
        )  # type:ignore
        self.nested_tab: QTabWidget = self.window.findChild(
            QTabWidget, "tabWidget_nested"
        )  # type:ignore
        self.set_tabs_to_initial: QPushButton = self.window.findChild(
            QPushButton, "set_tabs_to_initial"
        )  # type:ignore
        self.set_to_2nd_tab: QPushButton = self.window.findChild(
            QPushButton, "set_to_2nd_tab"
        )  # type:ignore
        self.load_dynamically: QToolButton = self.window.findChild(
            QToolButton, "load_dynamically"
        )  # type:ignore
        self.scroll_area: QScrollArea = self.window.findChild(
            QScrollArea, "scrollArea"
        )  # type:ignore
        self.container: QWidget = self.window.findChild(
            QWidget, "container"
        )  # type:ignore

        self.dynamic_list: list = []

        # Define logic for UI elements
        self.set_tabs_to_initial.clicked.connect(self.reset_tabs)
        self.set_to_2nd_tab.clicked.connect(self.top_tab_to_tab_2)
        self.load_dynamically.clicked.connect(self.load_new_thing)

        self.window.show()  # must be at the end of the __init__

    def reset_tabs(self):
        """Set both tabs to index 0."""
        self.top_tab.setCurrentIndex(0)
        self.nested_tab.setCurrentIndex(0)

    def top_tab_to_tab_2(self):
        """Set top_tab to index 1."""
        self.top_tab.setCurrentIndex(1)

    def load_new_thing(self):
        """Loads the dynamic.ui instances into the QScrollArea."""

        dynamic_widget = DynamicWidget(ui_dynamic)

        # load it into a list so each instance retains its own functionality
        self.dynamic_list.append(dynamic_widget)

        # Add the new widget to the existing container layout
        # (which is positioned as wanted inside of the QScrollArea)
        layout = self.container.layout()
        layout.addWidget(dynamic_widget.window)  # type:ignore


# class for the dynamically loaded widgets in the advanced window
class DynamicWidget:
    def __init__(self, ui_file) -> None:
        self.window = load_widget(ui_file)
        self.delete_button: QPushButton = self.window.findChild(
            QPushButton, "delete_widget"
        )  # type:ignore
        self.delete_button.clicked.connect(self.delete_self)

    def delete_self(self):
        self.window.close()


# Logic that loads the application
app = QApplication([])
logic_main_window = MainWindow(ui_main)
app.exec()  # event loop
