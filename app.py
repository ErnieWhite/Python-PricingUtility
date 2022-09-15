import tkinter as tk
from controller import Controller
from model import Model
from view import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')
        self['bg'] = 'pink'
        self.geometry('700x700')

        # create a model
        model = Model()

        # create a view and place it on the root window
        view = View(self)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)
