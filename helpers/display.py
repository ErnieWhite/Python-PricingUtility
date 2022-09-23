import tkinter as tk


class Display(tk.Entry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self['state'] = tk.DISABLED
