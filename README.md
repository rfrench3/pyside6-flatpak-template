# pyside6-flatpak-template
This is a base template for a flatpak app using PySide6, complete with additional helpful information.

### Explanation
- There are multiple ways you can use PySide6 to create an app. This repository assumes you will use Qt Designer to create .ui files because I believe it is the easiest method.
- At the time of writing, KDE does not have up-to-date bindings for Python, and attempting to use the Kwidgets in Qt Designer will not work.


### yml File
- The yml file is a blueprint for building the app. It can source files from a local directory, but has been set up here to look for a GitHub repository.
- While the tag is able to be set to a branch (such as main), for security and stability reasons it should in all cases be set to a tagged release outside of testing your latest changes.

### Building the App
Install flatpak builder from Flathub, and in the directory with the yml file, run the following commands:

`flatpak-builder --force-clean --repo=repo builddir io.github.rfrench3.pyside6-flatpak-template.yml`

`flatpak build-bundle repo pyside6-flatpak-template.flatpak io.github.rfrench3.pyside6-flatpak-template`

### Important Notes
The versions of many things in this repository may be out of date! Make sure to check the following and ensure they are up to date:
- /requirements.in
- /requirements.txt (generated from requirements.in)
- /io.github.rfrench3.pyside6-flatpak-template.yml (lines 3 and 6)

Licensing: https://www.qt.io/qt-licensing
