from tkinter import ttk


class Page(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent

    def open(self):
        pass

    def close(self):
        pass
