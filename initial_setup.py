#!/usr/bin/env python3
"""Run this script to update the template to fit your application."""

from pathlib import Path
print("NOTICE: Once you accept changes (after all questions are answered), you will not be able to run this script again!\n")

app_name = input("Provide the name of your application (example: Pyside6 Flatpak Template): ")
app_id = input("Provide the application identifier (example: io.github.rfrench3.pyside6-flatpak-template): ")
app_command = input("Provide the command that will open the application (example: pyside6apptemplate): ")

current_folder = Path(__file__).resolve().parent
yml = current_folder / "io.github.rfrench3.pyside6-flatpak-template.yml"
xml = current_folder / "io.github.rfrench3.pyside6-flatpak-template.metainfo.xml"
png = current_folder / "io.github.rfrench3.pyside6-flatpak-template.png"
svg = current_folder / "io.github.rfrench3.pyside6-flatpak-template.svg"
desktop = current_folder / "io.github.rfrench3.pyside6-flatpak-template.desktop"
mainpy = current_folder / "src" / "main.py"
widgetspy = current_folder / "src" / "widget_manager.py"
readme = current_folder / "README.md"

if input("Accept changes? (y/N) ").lower() != 'y':
    print("Operation cancelled.")
    exit()

# attempt to automatically parse for github. If this fails, some more information will need to be manually input.
parse_github: bool = "io.github" in app_id
if parse_github:
    split = app_id.split('.')
    if len(split) == 4:
        username = split[2]
        repo = split[3]
    else:
        parse_github = False

png.rename(f"{app_id}.png")
svg.rename(f"{app_id}.svg")

yml = yml.rename(f"{app_id}.yml")
xml = xml.rename(f"{app_id}.metainfo.xml")
desktop = desktop.rename(f"{app_id}.desktop")

### YML FILE ###
def edit_yml():
    with open(yml, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if "io.github.rfrench3.pyside6-flatpak-template" in line:
            lines[i] = lines[i].replace("io.github.rfrench3.pyside6-flatpak-template", app_id)
        if "pyside6apptemplate" in line:
            lines[i] = lines[i].replace("pyside6apptemplate", app_command)
        if ("https://github.com/rfrench3/pyside6-flatpak-template.git" in line) and parse_github:
            lines[i] = lines[i].replace("https://github.com/rfrench3/pyside6-flatpak-template.git", f"https://github.com/{username}/{repo}.git")

    with open(yml, "w") as file:
        file.writelines(lines)
edit_yml()

### XML FILE ###
def edit_xml():
    with open(xml, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if "PySide6 Flatpak Template" in line:
            lines[i] = lines[i].replace("PySide6 Flatpak Template", app_name)
        elif "io.github.rfrench3.pyside6-flatpak-template" in line:
            lines[i] = lines[i].replace("io.github.rfrench3.pyside6-flatpak-template", app_id)
        elif ("https://github.com/rfrench3/pyside6-flatpak-template" in line) and parse_github:
            lines[i] = lines[i].replace("https://github.com/rfrench3/pyside6-flatpak-template", f"https://github.com/{username}/{repo}")
        elif ("https://raw.githubusercontent.com/rfrench3/pyside6-flatpak-template" in line) and parse_github:
            lines[i] = lines[i].replace("https://raw.githubusercontent.com/rfrench3/pyside6-flatpak-template", f"https://raw.githubusercontent.com/{username}/{repo}")

    with open(xml, "w") as file:
        file.writelines(lines)
edit_xml()

### main.py ###
def edit_mainpy():
    with open(mainpy, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if '''sys.path.insert(0, "/app/share/pyside6apptemplate")''' in line:
            lines[i] = lines[i].replace("pyside6apptemplate", app_command)

    with open(mainpy, "w") as file:
        file.writelines(lines)
edit_mainpy()

### widget_manager.py ###
def edit_widgetspy():
    with open(widgetspy, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if '''app_icon = QIcon.fromTheme("io.github.rfrench3.pyside6apptemplate")''' in line:
            lines[i] = lines[i].replace("pyside6apptemplate", app_command)

    with open(widgetspy, "w") as file:
        file.writelines(lines)
edit_widgetspy()

### desktop file ###
def edit_desktop():
    with open(desktop, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("Name="):
            lines[i] = f"Name={app_name}\n"
        if line.startswith("Exec="):
            lines[i] = f"Exec={app_command}\n"
        if line.startswith("Icon="):
            lines[i] = f"Icon={app_id}\n"

    with open(desktop, "w") as file:
        file.writelines(lines)
edit_desktop()

### readme file ###
def edit_readme():
    with open(readme, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if "io.github.rfrench3.pyside6-flatpak-template" in line:
            lines[i] = lines[i].replace("io.github.rfrench3.pyside6-flatpak-template", app_id)

    with open(readme, "w") as file:
        file.writelines(lines)
edit_readme()



print("Success! Now you must:\n" \
"- update the README.md\n" \
"- ensure you are using the latest PySide6 and KDE runtimes (check the yml and requirements.in/txt).\n" \
f"- finish updating the information in the {app_id}.metainfo.xml file\n" \
"- create your new application!")
