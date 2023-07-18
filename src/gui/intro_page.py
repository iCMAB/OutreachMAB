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
                             command=lambda: controller.set_page("simulation"))

        your_settings = ttk.Label(self, text="Your Selected Settings", justify="center")
        your_settings.grid(row=1, column=0, padx=20, pady=10)

        model_label = ttk.Label(self, text="Bandit Model: " + self.controller.simulation.bandit.type, font=tkFont.Font(size=12))
        model_label.grid(row=2, column=0, padx=20, pady=10)

        arms_label = ttk.Label(self, text="Number of Arms: " + str(self.controller.simulation.bandit.n_arms), font=tkFont.Font(size=12))
        arms_label.grid(row=3, column=0, padx=20, pady=10)

        iters_label = ttk.Label(self, text="Number of Frames: " + str(self.controller.simulation.num_frames), font=tkFont.Font(size=12))
        iters_label.grid(row=4, column=0, padx=20, pady=10)
        # putting the button in its place by
        # using grid
        button1.grid(row=5, column=0, padx=20, pady=10, ipadx=50, ipady=20)
