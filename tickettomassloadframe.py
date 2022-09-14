from tkinter import ttk


class TicketToMassLoadFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tempLabel = ttk.Label(self, text='Ticket To Mass Load Frame')
        self.tempLabel.grid(row=1, column=1)
