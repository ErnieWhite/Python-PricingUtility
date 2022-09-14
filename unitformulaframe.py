import tkinter as tk
from tkinter import ttk


class UnitFormulaFrame(ttk.Labelframe):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self['text'] = 'Find basis value'

        # create the labels
        unit_price_label = tk.Label(self)
        formula_label = tk.Label(self)
        decimals_label = tk.Label(self)
        basis_label = tk.Label(self)

        # create the inputs
        unit_price_entry = tk.Entry(self)
        formula_entry = tk.Entry(self)
        decimals_combobox = ttk.Combobox(self)

        # create copy button
        copy_button = tk.Button(self)

        # create the display
        basis_entry = tk.Entry(self)

        # setup the widgets
        unit_price_label['text'] = 'Unit Price'
        formula_label['text'] = 'Formula'
        decimals_label['text'] = 'Decimals'
        basis_label['text'] = 'Basis Value'
        copy_button['text'] = 'Copy'

        # place the widgets
        unit_price_label.grid(row=0, column=0)
        formula_label.grid(row=1, column=0)
        decimals_label.grid(row=2, column=0)
        basis_label.grid(row=3, column=0)

        unit_price_entry.grid(row=0, column=1, sticky='ew')
        formula_entry.grid(row=1, column=1, sticky='ew')
        decimals_combobox.grid(row=2, column=1, sticky='ew')
        basis_entry.grid(row=3, column=1, sticky='ew')

        copy_button.grid(row=3, column=2, sticky='e')


