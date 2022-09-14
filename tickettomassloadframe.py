from tkinter import ttk


class TicketToMassLoadFrame(ttk.Labelframe):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self['text'] = 'Ticket To Mass Load'

        self.tempLabel = ttk.Label(self, text='Ticket To Mass Load Frame')
        self.tempLabel.grid(row=1, column=1)
