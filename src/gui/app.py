import tkinter as tk
from tkinter import ttk
from typing import Dict

from src.gui.pages.intro_page import IntroPage
from src.gui.pages.results_page import ResultsPage
from src.gui.pages.settings_explain_page import SettingsExplainPage
from src.gui.pages.settings_page import SettingsPage
from src.gui.pages.simulation_page import SimulationPage
from src.gui.pages.start_page import StartPage
from src.gui.standard_widgets.page import Page
from src.simulation.simulator import Simulator


class App(tk.Tk):
    def __init__(self, config_file: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.simulator = Simulator(config_file)

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.current_page: Page | None = None
        self.pages: Dict[str, Page] = {
            "start": StartPage(master=container, app=self),
            "simulation": SimulationPage(master=container, app=self),
            "settings": SettingsPage(master=container, app=self),
            "results": ResultsPage(master=container, app=self),
            "settings_explained": SettingsExplainPage(master=container, app=self),
            "intro": IntroPage(master=container, app=self)
        }

        for _, v in self.pages.items():
            v.grid(row=0, column=0, sticky="nsew")

        self.title("Restaurant Outreach")
        width = 1200
        height = 800
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=True, height=True)

        self.set_page("start")

    def set_page(self, page: str):
        if self.current_page is not None:
            self.current_page.close()

        new_page = self.pages[page]
        new_page.open()
        new_page.tkraise()
        self.current_page = new_page
