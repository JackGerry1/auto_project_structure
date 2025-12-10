import tkinter as tk
from model.model import Model
from view.view import View
from controller.controller import Controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Auto Project Structure Generator')

        model = Model()
        view = View(self)
        controller = Controller(model, view)

        view.set_controller(controller)
        view.grid(row=0, column=0, padx=10, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
