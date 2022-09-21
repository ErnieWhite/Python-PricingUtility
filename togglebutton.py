# This class is based on https://www.geeksforgeeks.org/on-off-toggle-button-switch-in-tkinter/
import tkinter as tk


class ToggleButton(tk.Button):
    def __init__(self, master, **kwargs):

        if 'imageOn' in kwargs:
            self.imageOn = kwargs['imageOn']
            kwargs.pop('imageOn')
        else:
            self.imageOn = None
        if 'imageOff' in kwargs:
            self.imageOff = kwargs['imageOff']
            kwargs.pop('imageOff')
        else:
            self.imageOff = None

        self.is_on = False
        if 'switch' in kwargs:
            if kwargs['switch'] == 'on':
                self.is_on = True
            elif kwargs['switch'] == 'off':
                self.is_on = False
            else:
                raise ValueError('Expected: "on" or "off" got: ' + kwargs['switch'])
            kwargs.pop('switch')

        super().__init__(master, **kwargs)

        if self.is_on:
            self.config(image=self.imageOn)
        else:
            self.config(image=self.imageOff)

    # Define our switch function
    def switch(self):
        # Determine is on or off
        if self.is_on:
            self.config(image=self.imageOff)
            self.is_on = False
        else:
            self.config(image=self.imageOn)
            self.is_on = True
