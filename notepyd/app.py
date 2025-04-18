import tkinter as tk

from widgets.editor import Editor
from widgets.navbar import Navbar
from widgets.infobar import InfoBar
from config import START_GEOMETRY

from pathlib import Path

class Notepyd(tk.Tk):
    """
    creates the gui program
    """
    def __init__(self):
        super().__init__()
        self.title('Notepyd')
        self.geometry(START_GEOMETRY)
        self.current_file = None

        self.navbar = Navbar(self, self)
        self.editor = Editor(self, self)
        self.infobar = InfoBar(self, self)

        self.bind_all('<Control-s>', self._save_file)
        self.bind_all('<Control-o>', self._open_file)
        self.bind_all('<Control-z>', self._undo)
        self.bind_all('<Control-y>', self._redo)

    def set_current_file(self, path):
        self.infobar.update_file_name(path.split("/")[-1])
        self.current_file = path

    def _save_file(self, event=None):
        self.navbar.save_file()

    def _open_file(self, event=None):
        self.navbar.open_file()

    def _undo(self, event=None):
        try:
            self.editor.text.edit_undo()
        except tk.TclError:
            pass

    def _redo(self, event=None):
        try:
            self.editor.text.edit_redo()
        except tk.TclError:
            pass

