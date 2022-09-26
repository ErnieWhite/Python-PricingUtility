import tkinter as tk
from tkinter import ttk


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
        self.createInputWidgets()

        # create the copy buttons
        multiplierCopyButton = tk.Button(self.container)
        discountCopyButton = tk.Button(self.container)
        markupCopyButton = tk.Button(self.container)
        grossCopyButton = tk.Button(self.container)

        # set up the widgets
        decimalValues = ('Auto', '0', '1', '2', '3', '4', '5', '6',)
        self.decimalsPlacesCombobox['values'] = decimalValues
        self.decimalsPlacesCombobox['state'] = 'readonly'
        self.multiplierDisplayEntry['state'] = 'readonly'
        self.markupDisplayEntry['state'] = 'readonly'
        self.discountDisplayEntry['state'] = 'readonly'
        self.grossDisplayEntry['state'] = 'readonly'
        multiplierCopyButton['text'] = 'Copy'
        discountCopyButton['text'] = 'Copy'
        markupCopyButton['text'] = 'Copy'
        grossCopyButton['text'] = 'Copy'

        # place the widgets
        tk.Label(self.container, text='Unit Price').grid(row=0, column=0)
        tk.Label(self.container, text='Basis Value').grid(row=1, column=0)
        tk.Label(self.container, text='Decimal Places').grid(row=2, column=0)
        self.unitPriceEntry.grid(row=0, column=1, sticky='ew')
        self.multiplierDisplayEntry.grid(row=0, column=2, sticky='ew')
        self.multiplierCopyButton.grid(row=0, column=3)

        self.basisValueLabel.grid(row=1, column=0)
        self.basisValueEntry.grid(row=1, column=1, sticky='ew')
        self.discountDisplayEntry.grid(row=1, column=2, sticky='ew')
        discountCopyButton.grid(row=1, column=3)

        self.decimalsPlacesLabel.grid(row=2, column=0)
        self.decimalsPlacesCombobox.grid(row=2, column=1, sticky='ew')
        self.markupDisplayEntry.grid(row=2, column=2, sticky='ew')
        markupCopyButton.grid(row=2, column=3)

        self.grossDisplayEntry.grid(row=3, column=2, sticky='ew')
        grossCopyButton.grid(row=3, column=3)

        self.container.pack(side=tk.TOP, fill=tk.BOTH)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)

    def createInputWidgets(self):

        vcmd = (self.register(self.onValidate),
                '%P', '%W')
        ivcmd = (self.register(self.invalid),
                 '%W')
        self.unitPriceEntry = tk.Entry(self.container, validate='key', validatecommand=vcmd, invalidcommand=ivcmd)
        self.basisValueEntry = tk.Entry(self.container, validate='key', validatecommand=vcmd, invalidcommand=ivcmd)
        self.decimalsPlacesCombobox = ttk.Combobox(self.container)

        # create the display widgets
        self.multiplierDisplayEntry = tk.Entry(self.container)
        self.discountDisplayEntry = tk.Entry(self.container)
        self.markupDisplayEntry = tk.Entry(self.container)
        self.grossDisplayEntry = tk.Entry(self.container)


    def destroy(self):
        self.state('withdrawn')
        # TODO: fix this
        self.master.unitBasisToggle.switch()

    def onValidate(self, value, widgetName):
        """
        Validate the currency value.  Can have a dollar sigh and commas
        :param value: The value after the edit
        :param widgetName: The name of the widget that is being validated.
                            This is the TK name i.e. .!view.!unitbasis.!entry
        :return: boolean
        """
        if self.is_float_or_empty(value):
            self.show_message(widgetName)
            return True
        else:
            return False

        # print(value)
        # pattern = r'(\$?(0?|[1-9][0-9]{0,2})(,\d{3})*(\.\d{1,4})?)$'
        # print(f'Fullmatch result {re.fullmatch(pattern, value)}')
        # if re.fullmatch(pattern, value) is None:
        #     print(widgetName)
        #     return False
        #
        # # clear the message
        # self.show_message(widgetName)
        # return True

    def invalid(self, widgetName):
        """
        Show the error message if the data is not valid

        :param widgetName: used to change the font color of the named widget.  Name are in TK format not Tkinter format
        :return:
        """

        self.show_message(
            widgetName,
            message='Please enter a valid currency value. Can contain a dollar sign and commas',
            color='red'
        )

    def show_message(self, widgetName, message='', color='black'):
        """
        Show the error message in the status bar
        :param message:
        :param color:
        :return:
        """
        self.errorDisplay['text'] = message
        print(widgetName)
        if widgetName == '.!view.!unitbasis.!entry':
            self.unitPriceEntry['foreground'] = color
        elif widgetName == '.!view.!unitformula.!entry':
            self.basisValueEntry['forground'] = color

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def is_float_or_empty(self, value):
        return self.is_float(value) or value == ''
    
    def find_multiplier(formula: str) -> float:
        """converts a string formula to a float multiplier

        a return value of -1 indicates error
        """
        try:
            print(formula)
            if formula[0] in '+-':
                return 1 + float(formula) / 100
            if formula[0].upper() == 'd':
                return 1 / float(formula[1:])
            if formula.upper().startswith('gp'):
                return 1 / (1 - float(formula[2:]) / 100)
            if formula[0].upper() in '*x':
                return float(formula[1:])
        except ZeroDivisionError:
            return -1

    def validate_formula(self, value: str) -> bool:
        """returns a boolean indicating if value is in one of the forms case insensitive

        [g]

        [''|none]

        [*||x||d|-|+]{0..9}[.]{0..9}

        gp[-|+]{0..9}[.]{0..9}

        """
        leaders = ['*', 'x', '-', '+', 'd', 'g', 'gp']
        value = value.upper()
        if value in leaders:
            return True
        leaders.remove('g')
        for leader in leaders:
            if value.startswith(leader) and (self.is_float(value[len(leader):]) or value[len(leader):] == '.'):
                return True
        if value == '':
            return True
        return False

    def valid_formula(self, value: str) -> bool:
        """returns a boolean indicating if value is in one of the forms case insensitive

        [g]

        [''|none]

        [*||x||d|-|+]{0..9}[.]{0..9}

        gp[-|+]{0..9}[.]{0..9}

        """
        leaders = ['*', 'x', '-', '+', 'd', 'gp']
        value = value.upper()
        for leader in leaders:
            if value.startswith(leader) and self.is_float(value[len(leader):]):
                return True
        return False

   




