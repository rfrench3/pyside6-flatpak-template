"""Run this script to update the template to fit your application."""

from pathlib import Path
print("NOTICE: Once you accept changes (after all questions are answered), you will not be able to run this script again!")

name = input("Provide the name of your application (example: Pyside6 Flatpak Template): ")
id = input("Provide the application identifier (example: io.github.rfrench3.pyside6-flatpak-template): ")
command = input("Provide the command that will open the application (example: pyside6apptemplate)")

current_folder = Path(__file__).resolve().parent
yml = current_folder / "io.github.rfrench3.pyside6-flatpak-template.yml"
xml = current_folder / "io.github.rfrench3.pyside6-flatpak-template.metainfo.xml"
png = current_folder / "io.github.rfrench3.pyside6-flatpak-template.png"
svg = current_folder / "io.github.rfrench3.pyside6-flatpak-template.svg"
desktop = current_folder / "io.github.rfrench3.pyside6-flatpak-template.desktop"
readme = current_folder / "README.md"

if input("Accept changes? (y/N) ").lower() != 'y':
    print("Operation cancelled.")
    exit()

# attempt to automatically parse for github. If this fails, some more information will need to be manually input.
parse_github: bool = "io.github" in id
if parse_github:
    split = id.split('.')
    if len(split) == 4:
        username = split[2]
        repo = split[3]
    else:
        parse_github = False


yml.rename(f"{id}.yml")
xml.rename(f"{id}.metainfo.xml")
png.rename(f"{id}.png")
svg.rename(f"{id}.svg")
desktop.rename(f"{id}.desktop")

with open(yml, "r") as file:
    lines = file.readlines()

for line in lines:
    line.replace("pyside6apptemplate", command)
    line.replace("io.github.rfrench3.pyside6-flatpak-template", id)
    if "url: https://github.com/" in line:
        line = line.split("url: ")[0] + f"url: https://github.com/{username}/{repo}.git"

with open(yml, "w") as file:
    file.writelines(lines)


print("Success! Now you must update the README.md and ensure you are using the latest PySide6 and KDE runtimes (check the yml and requirements.in/txt).")
