import tkinter as tk
from helpers.controller import Controller
from helpers.model import Model
from helpers.view import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')
        self.geometry('700x700')

        # create a model
        model = Model()

        # create a view and place it on the root window
        view = View(self)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)

        
if __name__ == '__main__':
    app = App()
    app.mainloop()
