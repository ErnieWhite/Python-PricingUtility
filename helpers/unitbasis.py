import re
import tkinter as tk
from tkinter import ttk

from functools import partial


class UnitBasis(tk.Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.title('Find Formula from Unit/Basis')

        # create the container
        self.container = tk.Frame(self)

        # create a status bar
        self.statusBar = tk.Frame(self)
        self.errorDisplay = tk.Label(self.statusBar)
        self.errorDisplay.pack(side=tk.LEFT)

        # create our invalid commands
        # self['text'] = 'Find Formulas'
        # create the input widgets
        unit_price_label = tk.Label(self.container, text='Unit Price')
        basis_value_label = tk.Label(self.container, text='Basis Value')
        decimals_places_label = tk.Label(self.container, text='Decimal Places')
        vcmd = (self.register(self.onValidate),
                '%P', '%W')
        ivcmd = (self.register(self.invalid),
                 '%W')
        self.unit_price_entry = tk.Entry(self.container, validate='key', validatecommand=vcmd)
        self.basis_value_entry = tk.Entry(self.container, validate='key', validatecommand=vcmd)
        self.decimals_places_combobox = ttk.Combobox(self.container)

        # create the display widgets
        self.multiplier_display_entry = tk.Entry(self.container)
        self.discount_display_entry = tk.Entry(self.container)
        self.markup_display_entry = tk.Entry(self.container)
        self.gross_display_entry = tk.Entry(self.container)

        # create the copy buttons
        multiplier_copy_button = tk.Button(self.container)
        discount_copy_button = tk.Button(self.container)
        markup_copy_button = tk.Button(self.container)
        gross_copy_button = tk.Button(self.container)

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

        self.container.pack(side=tk.TOP, fill=tk.BOTH)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)

    def destroy(self):
        self.state('withdrawn')
        self.master.unitBasisToggle.switch()

    def onValidate(self, value, widget_name):
        """
        Validate the currency value.  Can have a dollar sigh and commas
        :param value: The value after the edit
        :return: boolean
        """
        print(value)
        pattern = r'(\$?(0?|[1-9][0-9]{0,2})(,\d{3})*(\.\d{1,4})?)$'
        print(f'Fullmatch result {re.fullmatch(pattern, value)}')
        if re.fullmatch(pattern, value) is None:
            print(widget_name)
            return False

        # clear the message
        self.show_message(widget_name)
        return True

    def invalid(self, widget_name):
        """
        Show the error message if the data is not valid

        :param widget_name: used to change the font color of the named widget.  Name are in TK format not Tkinter format
        :return:
        """

        self.show_message(
            widget_name,
            message='Please enter a valid curreny value. Can contain a dollar sign and commas',
            color='red'
        )

    def show_message(self, widget_name, message='', color='black'):
        """
        Show the error message in the status bar
        :param message:
        :param color:
        :return:
        """
        self.errorDisplay['text'] = message
        print(widget_name)
        if widget_name == '.!view.!unitbasis.!entry':
            self.unit_price_entry['foreground'] = color
        elif widget_name == '.!view.!unitformula.!entry':
            self.basis_value_entry['forground'] = color
