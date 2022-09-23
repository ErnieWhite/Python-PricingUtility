import tkinter as tk
from tkinter import ttk

from helpers.display import Display


class MassLoad(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # self['text'] = 'Ticket Mass Load'

        main_frame = tk.Frame(self)

        header_frame = tk.Frame(main_frame)
        detail_frame = tk.Frame(main_frame)

        # create the vars
        self._file_name_var = tk.StringVar()
        self._order_number_var = tk.StringVar()
        self._ship_date_var = tk.StringVar()
        self._customer_name_var = tk.StringVar()

        # ticket header widgets
        file_name_label = ttk.Label(header_frame, text='File Name')
        self.file_name_display = Display(header_frame, textvariable=self._file_name_var, state=tk.DISABLED)

        order_number_label = ttk.Label(header_frame, text='Order Number')
        self.order_number_display = Display(header_frame, textvariable=self._order_number_var)

        ship_date_label = ttk.Label(header_frame, text='Ship Date')
        self.ship_date_display = Display(header_frame, textvariable=self._ship_date_var)

        customer_name_label = ttk.Label(header_frame, text='Customer Name')
        self._customer_name_display = Display(header_frame, textvariable=self._customer_name_var)

        # place the header widgets
        file_name_label.grid(row=0, column=0)
        self.file_name_display.grid(row=0, column=1, sticky='ew')

        order_number_label.grid(row=1, column=0)
        self.order_number_display.grid(row=1, column=1)

        ship_date_label.grid(row=2, column=0)
        self.ship_date_display.grid(row=2, column=1)

        customer_name_label.grid(row=4, column=0)
        self._customer_name_display.grid(row=4, column=1)

        header_frame.grid(row=0, column=0, sticky=tk.NSEW)
        detail_frame.grid(row=1, column=0, sticky=tk.NSEW)
        main_frame.grid(row=0, column=0, sticky=tk.NSEW)

    @property
    def file_name(self):
        return self._file_name_var.get()

    @file_name.setter
    def file_name(self, text):
        self._file_name_var.set(text)

    @property
    def order_number(self):
        return self._order_number_var.get()

    @order_number.setter
    def order_number(self, text):
        self._order_number_var.set(text)

    @property
    def ship_date(self):
        return self._ship_date_var.get()

    @ship_date.setter
    def ship_date(self, text):
        self._ship_date_var.set(text)

    @property
    def customer_name(self):
        return self._customer_name_var.get()

    @customer_name.setter
    def customer_name(self, text):
        self._customer_name_var.set(text)
