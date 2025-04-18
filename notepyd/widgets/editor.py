import tkinter as tk

class Editor(tk.Frame):
    """
    Responsible to create the area to edit texts
    """

    def __init__(self, parent, app_context, **kwargs):
        super().__init__(parent)
        self.app_context = app_context

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side='right', fill='y')

        self.text = tk.Text(self, wrap='word', undo=True, autoseparators=True, maxundo=-1, yscrollcommand=self.scrollbar.set, **kwargs)
        self.text.pack(expand=True, fill='both')

        self.scrollbar.config(command=self.text.yview)

        self.pack(expand=True, fill='both')

        self.text.bind('<<Modified>>', self._on_change)

    def _on_change(self, event):
        if self.text.edit_modified():
            content = self.get_text()
            self.app_context.infobar.update_stats(content)
            self.text.edit_modified(False)
            self.text.edit_separator()

    def get_text(self):
        return self.text.get('1.0', tk.END)

    def focus(self):
        self.text.focus_set()

    def set_text(self, content):
        self.text.delete('1.0', tk.END)
        self.text.insert('1.0', content)
        self.text.edit_separator()
