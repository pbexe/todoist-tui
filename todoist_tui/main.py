from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import *
from picotui.defs import *
import os
from todoist.api import TodoistAPI

def choose_project():
    with Context():
        rows, columns = os.popen('stty size', 'r').read().split()
        Screen.attr_color(C_WHITE, C_RED)
        Screen.cls()
        Screen.attr_reset()
        d = Dialog(0, 0, int(columns), int(rows))
        d.add(1, 1, "Project:")
        choice = WListBox(16, int(rows) - 5, ["choice%d" % i for i in range(100)])
        d.add(1, 3, choice)
        b = WButton(8, "Choose")
        d.add(1, int(rows) - 2, b)
        b.finish_dialog = ACTION_OK
        res = d.loop()
    return choice.get()

def loading_project():
    with Context():
        rows, columns = os.popen('stty size', 'r').read().split()
        Screen.attr_color(C_WHITE, C_RED)
        Screen.cls()
        Screen.attr_reset()
        d = Dialog(0, 0, int(columns), int(rows))
        d.add(1, 1, "Loading Project")
        choice = WListBox(16, int(rows) - 5, ["choice%d" % i for i in range(100)])
        d.add(1, 3, choice)
        b = WButton(8, "Choose")
        d.add(1, int(rows) - 2, b)
        b.finish_dialog = ACTION_OK
        res = d.loop()

if __name__ == "__main__":
choose_project()
choose_project()
    
