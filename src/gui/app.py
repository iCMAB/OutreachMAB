import tkinter as tk
from tkinter import ttk
from typing import Dict, Type

from src.gui.pages.bandit_explain_page import BanditExplainPage
from src.gui.pages.intro_page import IntroPage
from src.gui.pages.results_page import ResultsPage
from src.gui.pages.settings_page import SettingsPage
from src.gui.pages.simulation_page import SimulationPage
from src.gui.pages.start_page import StartPage
from src.simulation.simulator import Simulator


class App(tk.Tk):
    def __init__(self, config_file: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.simulator = Simulator(config_file)

        self.container = ttk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.page_history = []
        self.pages: Dict[str, Type] = {
            "start": StartPage,
            "simulation": SimulationPage,
            "settings": SettingsPage,
            "results": ResultsPage,
            "bandits_explained": BanditExplainPage,
            "intro": IntroPage
        }

        self.title("Restaurant Outreach")
        width = 1200
        height = 800
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=True, height=True)
        self.bind("<Button-1>", self.click_event)

        self.set_page("start")

    def set_page(self, page: str):
        if len(self.page_history) > 0:
            self.page_history[-1].close()
            self.page_history[-1].destroy()

        new_page = self.pages[page](master=self.container, app=self)
        new_page.open()
        new_page.grid(column=0, row=0, sticky=tk.NSEW)
        self.page_history.append(new_page)

    def back_page(self):
        if len(self.page_history) <= 1:
            return

        current = self.page_history.pop(-1)
        previous = self.page_history[-1]
        current.close()
        previous.open()
        previous.tkraise()

    def click_event(self, event):
        x, y = self.winfo_pointerxy()  # get the mouse position on screen
        widget = self.winfo_containing(x, y)  # identify the widget at this location
        widget.focus()  # focus on root
