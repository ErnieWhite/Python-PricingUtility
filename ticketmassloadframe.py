from tkinter import ttk


class TicketMassLoadFrame(ttk.Labelframe):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self['text'] = 'Ticket Mass Load'

        self.tempLabel = ttk.Label(self, text='Ticket Mass Load Frame')
        self.tempLabel.grid(row=1, column=1)
