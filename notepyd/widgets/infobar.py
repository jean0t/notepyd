import tkinter as tk

class InfoBar(tk.Frame):
    def __init__(self, parent, app_context):
        super().__init__(parent, height=20, bg='#eeeeee')
        self.app_context = app_context

        self.file_label = tk.Label(self, text="Untitled", anchor='w')
        self.word_count_label = tk.Label(self, text='Words: 0 | Chars: 0', anchor='e')

        self.file_label.pack(side='left', padx=10)
        self.word_count_label.pack(side='right', padx=10)
        
        self.pack(side='bottom', fill='x')

    def update_file_name(self, name):
        self.file_label.config(text=name or 'Untitled')

    def update_stats(self, text):
        chars = len(text)
        words = len(text.split())
        self.word_count_label.config(text=f'Words: {words} | Chars: {chars}')
