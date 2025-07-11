"""This file is dedicated to locating program files and making them available to main.py.
sys.path.insert(0, "/app/share/pyside6apptemplate") in main.py handles detection of other python files
such as this one, so only the location of non-python files need to be determined here."""

import os

#UPPERCASE_WITH_UNDERSCORES is the naming convention for a constant in Python.
# The yml file is configured to place this in the same location as other application files
DATA_DIR = os.path.dirname(os.path.abspath(__file__)) 

