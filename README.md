# pyside6-flatpak-template
This is a base template for a flatpak app using PySide6, complete with additional helpful information.

### Information
- CRITICAL: 
    - This repository does not follow standard python packaging conventions. It is strictly set up for creating a flatpak application, and adapting it for other packaging formats may prove difficult.
    - There are three places you must update when a new version of PySide6 releases: the .yml file, the github workflows, and requirements.in (then regenerate requirements.txt)

- There are multiple ways you can use PySide6 to create an app. This repository utilizes Qt Designer to create .ui files because I believe it is the easiest way to use Qt, but adapting it to QML and other formats should not be difficult.
- At the time of writing, KDE does not have up-to-date bindings for Python, and attempting to use the Kwidgets present in Qt Designer will not work.
- Github workers are set up for this repository to automate certain things, such as adding the packaged flatpak to tagged releases on Github.

### Running the Application
To run the application, the simplest method is to use `uv` to manage a python virtual environment.
```bash 
# setup
uv venv

# create and install an updated requirements.txt
uv pip compile requirements.in
uv pip install -r requirements.txt

# run application
uv run python src/main.py
```


### yml File
- The yml file is a blueprint for building the app. It can source files from git directly, but for building locally and with the automated github workflow it should stay as-is.
- While the tag is able to be set to a branch (such as main), for security and stability reasons it should in all cases be set to a tagged release outside of testing your latest changes.

### Building the App
Install flatpak builder from Flathub, and in the directory with the yml file, run the following commands:

```bash
# INSTALL THE APP DIRECTLY
flatpak-builder --install --user app io.github.rfrench3.pyside6-flatpak-template.yml

flatpak run io.github.rfrench3.pyside6-flatpak-template
```

```bash
# CREATE A PACKAGE (without using the Github actions)
flatpak-builder --force-clean --repo=repo builddir io.github.rfrench3.pyside6-flatpak-template.yml

flatpak build-bundle repo pyside6-flatpak-template.flatpak io.github.rfrench3.pyside6-flatpak-template
```

# Licensing
Information for the licensing of apps that use Qt is located here: https://www.qt.io/qt-licensing
