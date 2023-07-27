from tkinter import ttk


class Page(ttk.Frame):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app

    def open(self):
        pass

    def close(self):
        pass
