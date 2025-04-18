import tkinter as tk
from tkinter import filedialog, messagebox

class Navbar(tk.Menu):
    """
    Responsible to create the navbar for the notepyd
    """

    def __init__(self, parent, app_context):
        super().__init__(parent)
        self.app = app_context

        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Save As', command=self.save_as_file)
        self.add_cascade(label='File', menu=file_menu)

        about_menu = tk.Menu(self, tearoff=0)
        about_menu.add_command(label='About', command=self.show_about)
        self.add_cascade(label='About', menu=about_menu)

        parent.config(menu=self)

    def open_file(self):
        path = filedialog.askopenfilename()
        if path:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.app.editor.set_text(content)
                self.app.set_current_file(path)

    def save_file(self):
        if self.app.current_file:
            with open(self.app.current_file, 'w', encoding='utf-8') as file:
                file.write(self.app.editor.get_text())

        else:
            self.save_as_file()

    def save_as_file(self):
        path = filedialog.asksaveasfilename(defaultextension='.txt')
        if path:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(self.app.editor.get_text())
            self.app.set_current_file(path)

    def show_about(self):
        messagebox.showinfo('About', 'Notepyd is a text editor in gui, made with tkinter.\nCreator: jean0t (github.com/jean0t)')
