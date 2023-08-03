import tkinter as tk
from tkinter import ttk


class Page(tk.Frame):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background='#D8E2DC')
        self.app = app

    def open(self):
        pass

    def close(self):
        pass
