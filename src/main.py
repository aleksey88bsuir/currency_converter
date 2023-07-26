import subprocess
import os
import sys


# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def run_gui_application():
    try:
        subprocess.run(['python', 'ui/GUI_copy.py'])
    except FileNotFoundError:
        print('Error: GUI.py file not found')


run_gui_application()
