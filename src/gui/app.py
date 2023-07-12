from typing import Dict

import tkinter as tk
from tkinter import ttk

from .start_page import StartPage
from .simulation_page import SimulationPage

class App(tk.Tk):
    rightButton = tk.Button
    currentIter = tk.Label
    leftButton = tk.Button
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames: Dict[str, ttk.Frame] = {
            "start": StartPage(container, self),
            "simulation": SimulationPage(container, self)
        }

        for _, v in self.frames.items():
            v.grid(row=0, column=0, sticky="nsew")

        self.title("Restaurant Outreach")
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        self.set_page("start")

    def set_page(self, page: str):
        frame = self.frames[page]
        frame.tkraise()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
