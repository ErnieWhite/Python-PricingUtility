import tkinter as tk
from tkinter import ttk


class UnitBasisFrame(ttk.Labelframe):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self['text'] = 'Find Formulas'

        # create the input widgets
        unit_price_label = tk.Label(self, text='Unit Price')
        basis_value_label = tk.Label(self, text='Basis Value')
        decimals_places_label = tk.Label(self, text='Decimal Places')
        self.unit_price_entry = tk.Entry(self)
        self.basis_value_entry = tk.Entry(self)
        self.decimals_places_combobox = ttk.Combobox(self)

        # create the display widgets
        self.multiplier_display_entry = tk.Entry(self)
        self.discount_display_entry = tk.Entry(self)
        self.markup_display_entry = tk.Entry(self)
        self.gross_display_entry = tk.Entry(self)

        # create the copy buttons
        multiplier_copy_button = tk.Button(self)
        discount_copy_button = tk.Button(self)
        markup_copy_button = tk.Button(self)
        gross_copy_button = tk.Button(self)

        # setup the widgets
        decimal_values = ('Auto', '0', '1', '2', '3', '4', '5', '6')
        self.decimals_places_combobox['values'] = decimal_values
        self.decimals_places_combobox['state'] = 'readonly'
        self.multiplier_display_entry['state'] = 'readonly'
        self.markup_display_entry['state'] = 'readonly'
        self.discount_display_entry['state'] = 'readonly'
        self.gross_display_entry['state'] = 'readonly'
        multiplier_copy_button['text'] = 'Copy'
        discount_copy_button['text'] = 'Copy'
        markup_copy_button['text'] = 'Copy'
        gross_copy_button['text'] = 'Copy'

        # place the widgets
        unit_price_label.grid(row=0, column=0)
        self.unit_price_entry.grid(row=0, column=1, sticky='ew')
        self.multiplier_display_entry.grid(row=0, column=2, sticky='ew')
        multiplier_copy_button.grid(row=0, column=3)

        basis_value_label.grid(row=1, column=0)
        self.basis_value_entry.grid(row=1, column=1, sticky='ew')
        self.discount_display_entry.grid(row=1, column=2, sticky='ew')
        discount_copy_button.grid(row=1, column=3)

        decimals_places_label.grid(row=2, column=0)
        self.decimals_places_combobox.grid(row=2, column=1, sticky='ew')
        self.markup_display_entry.grid(row=2, column=2, sticky='ew')
        markup_copy_button.grid(row=2, column=3)

        self.gross_display_entry.grid(row=3, column=2, sticky='ew')
        gross_copy_button.grid(row=3, column=3)
