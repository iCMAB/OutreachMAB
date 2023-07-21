from tkinter import ttk


class Page(ttk.Frame):
    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.controller = controller

    def open(self):
        pass

    def close(self):
        pass
