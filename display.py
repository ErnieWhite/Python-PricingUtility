import tkinter as tk
from tkinter import ttk


class Display(tk.Entry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self['state'] = tk.DISABLED
