import json
import tkinter as tk
from tkinter import ttk
from typing import Dict, Optional, List, Any

from src.gui.pages import PAGES
from src.gui.standard_widgets import Page
from src.simulation.simulator import Simulator


class App(tk.Tk):
    def __init__(self, config_filepath: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.simulator: Optional[Simulator] = None

        with open(config_filepath, "r") as config_file:
            self.config: Dict[str, Dict] = json.load(config_file)

        self.container = ttk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.page_history = []

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

    def show_page(self, page_name: str, args: List[Any], kwargs: Dict[str, Any]) -> Page:
        page = PAGES[page_name](master=self.container, app=self, *args, **kwargs)
        page.open()
        page.grid(column=0, row=0, sticky=tk.NSEW)
        return page

    def set_page(self, page_name: str, args: List[Any] = None, kwargs: Dict[str, Any] = None):
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}

        if len(self.page_history) > 0:
            self.page_history[-1].close()
            # self.page_history[-1].destroy()

        page = self.show_page(page_name, args, kwargs)
        self.page_history.append(page)

    def back_page(self):
        if len(self.page_history) <= 1:
            return

        current = self.page_history.pop(-1)
        previous = self.page_history[-1]
        current.close()
        current.destroy()
        previous.open()
        previous.grid(column=0, row=0, sticky=tk.NSEW)

    def click_event(self, event):
        x, y = self.winfo_pointerxy()  # get the mouse position on screen
        widget = self.winfo_containing(x, y)  # identify the widget at this location
        widget.focus()  # focus on root

    def create_simulator(
            self,
            num_frames: int,
            bandit: str,
            n_arms: int
    ):
        self.simulator = Simulator(
            config=self.config,
            bandit=bandit,
            n_arms=n_arms,
            num_frames=num_frames,
        )
