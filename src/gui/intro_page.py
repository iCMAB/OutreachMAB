import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

from .page import Page

class IntroPage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.grid_columnconfigure(0, weight=1)

        # label of frame Layout 2
        intro_text = ttk.Label(self, text="In this activity you will be going through a simulation of a multi-armed bandit\nmaking restaurant recommendations. "\
                          "The multi-armed bandit in this stage will\nnot be utilizing context. It will be attempting to find the restaurant that provides\nthe best "\
                          "reward the most often. \n\nYou will be going through the simulation with the bandit and see the decision it\nmakes each step of the way. "\
                          "There are supporting graphs to display the data\nthat the bandit has collected so far.", justify="left", font=tkFont.Font(size=12))

        # grid
        intro_text.grid(row=0, column=0, padx=20, pady=(50,10))

        button1 = ttk.Button(self, text="Continue",
                             command=lambda: self.controller.set_page("simulation"))

        your_settings = ttk.Label(self, text="Your Selected Settings", justify="center")
        your_settings.grid(row=1, column=0, padx=20, pady=10)

        self.model_label = ttk.Label(self, text="Bandit Model: " + self.controller.simulator.bandit.type, font=tkFont.Font(size=12))
        self.model_label.grid(row=3, column=0, padx=20, pady=10)

        self.arms_label = ttk.Label(self, text="Number of Arms: " + str(self.controller.simulator.bandit.n_arms), font=tkFont.Font(size=12))
        self.arms_label.grid(row=4, column=0, padx=20, pady=10)

        self.iters_label = ttk.Label(self, text="Number of Frames: " + str(self.controller.simulator.num_frames), font=tkFont.Font(size=12))
        self.iters_label.grid(row=2, column=0, padx=20, pady=10)
        # putting the button in its place by
        # using grid
        button1.grid(row=5, column=0, padx=20, pady=10, ipadx=50, ipady=20)

    def open(self):
        self.model_label.config(text="Bandit Model: " + self.controller.simulator.bandit.type)
        self.arms_label.config(text="Number of Arms: " + str(self.controller.simulator.bandit.n_arms))
        self.iters_label.config(text="Number of Frames: " + str(self.controller.simulator.num_frames))


