from typing import Dict

import tkinter as tk
from tkinter import ttk

from .page import Page
from .start_page import StartPage
from .simulation_page import SimulationPage
from .settings_page import SettingsPage
from src.simulation.simulator import Simulator


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.simulation = Simulator("../config.json")

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.current_page: Page = None
        self.pages: Dict[str, Page] = {
            "start": StartPage(container, self),
            "simulation": SimulationPage(container, self),
            "settings": SettingsPage(container, self)
        }

        for _, v in self.pages.items():
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
        if self.current_page is not None:
            self.current_page.close()
        new_page = self.pages[page]
        new_page.open()
        self.current_page = new_page
        new_page.tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
