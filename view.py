import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

from os.path import expanduser
from unitbasisframe import UnitBasisFrame
from unitformulaframe import UnitFormulaFrame
from ticketmassloadframe import TicketMassLoadFrame


class View(tk.Frame):

    # create the constants
    UNIT_BASIS = 'Unit Basis'
    UNIT_FORMULA = 'Unit Formula'
    TICKET_TO_MASS_LOAD = 'Ticket To Mass Load'

    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.controller = None
        self.statusbar_info_label = None
        self.switch_view_combobox = None

        # self.unitBasisFrame = UnitBasisFrame(self)
        # self.unitFormulaFrame = UnitFormulaFrame(self)
        # self.ticketMassLoadFrame = TicketMassLoadFrame(self)

        # self.unitBasisFrame.grid(row=1, column=0, sticky='nsew')
        # self.unitFormulaFrame.grid(row=2, column=0, sticky='nsew')
        # self.ticketMassLoadFrame.grid(row=1, column=1, rowspan=2, sticky='nsew')

        self.create_menubar()
        self.create_toolbar()
        self.create_statusbar()

        self['bg'] = 'red'

        self.grid(row=0, column=0, sticky=tk.NSEW)

    def create_menubar(self):
        """
        Create the menu
        :return:
        """
        # create the menubar
        menubar = tk.Menu(self.master)
        self.master['menu'] = menubar
        # create the file menu
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label='Open', command=self.open_file_command)
        file_menu.add_command(label='Save', command=self.save_file_command)
        file_menu.add_command(label='Save As', command=self.save_as_command)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.exit_command)
        # add the File menu to the menubar
        menubar.add_cascade(label='File', menu=file_menu)

    def create_toolbar(self):
        toolbar = tk.Frame(self, bd=1, relief=tk.RAISED)

        # create the toolbar widgets
        open_button = tk.Button(toolbar, text='Open', command=self.open_file_command)
        save_button = tk.Button(toolbar, text='Save', command=self.save_file_command)
        customers_button = tk.Button(toolbar, text='Customers', command=self.enter_customers)

        # pack the toolbar widgets
        open_button.pack(side=tk.LEFT, padx=2, pady=2)
        save_button.pack(side=tk.LEFT, padx=2, pady=2)
        customers_button.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(fill='x', expand=True)

    def create_statusbar(self):
        statusbar = tk.Frame(self, bd=1, relief=tk.RAISED)

        self.statusbar_info_label = tk.Label(statusbar, bd=1, relief=tk.SUNKEN)
        self.statusbar_info_label['text'] = 'Hello, anyone home'
        self.statusbar_info_label.pack(side=tk.RIGHT, padx=2, pady=2)

        statusbar.pack(fill='x', expand=True)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    @staticmethod
    def get_ticket_file_name():
        filetypes = (
            ('tab separated files', '*.tsv'),
            ('All files', '*.*'),
        )

        home_dir = expanduser('~')

        filepath = fd.askopenfilename(
            title='Open exported ticket',
            initialdir=home_dir,
            filetypes=filetypes,
        )

        return filepath

    def open_file_command(self):
        """
        Open a ticket export used in mass loads
        :return:
        """
        if self.controller is None:
            print('No controller')
            return
        filepath = self.get_ticket_file_name()
        if not filepath:
            return
        self.controller.load_ticket_data(filepath=filepath)
        return filepath

    def save_file_command(self):
        """
        Save the mass load csv file using the name of the TSV file opened
        :return:
        """
        if self.controller is not None:
            print('Save file command')
        else:
            print('No controller')

    def save_as_command(self):
        """
        Save the mass load file under a different name
        :return:
        """
        if self.controller is not None:
            print('Save as file command')
        else:
            print('No controller')

    def enter_customers(self):
        """
        Save the mass load file under a different name
        :return:
        """
        if self.controller is not None:
            print('Enter customer list')
        else:
            print('No controller')

    def exit_command(self):
        """
        Exit the application
        :return:
        """
        print('Exit application')
        self.master.destroy()
