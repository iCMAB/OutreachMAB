import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

import customtkinter as ctk

from src.gui.standard_widgets import Page, Header


class IntroPage(Page):
    def __init__(self, contextual: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.contextual = contextual

        self.grid_columnconfigure(0, weight=1)

        header = Header(
            master=self,
            app=self.app,
            title="Simulation Introduction",
            forward_button_args={
                "text": "START",
                "command": lambda: self.app.set_page("simulation", kwargs={"contextual": self.contextual})
            }
        )
        header.grid(column=0, row=0, sticky=tk.NSEW)

        # label of frame Layout 2
        intro_text = ttk.Label(
            master=self,
            text="""
            In this activity you will be going through a simulation of a multi-armed bandit
            making restaurant recommendations. The multi-armed bandit in this stage will
            not be utilizing context. It will be attempting to find the restaurant that provides
            the best reward the most often. 
            You will be going through the simulation with the bandit and see the decision it
            makes each step of the way. There are supporting graphs to display the data
            that the bandit has collected so far.
            """,

            font=tkFont.Font(size=14), justify='center', background='#D8E2DC'
        )

        # grid
        intro_text.grid(row=1, column=0, columnspan=4, padx=20, pady=(20, 10))

        your_settings = ttk.Label(self, text="Your Selected Settings", justify="center", font=tkFont.Font(size=18), background='#D8E2DC')
        your_settings.grid(row=2, column=0, columnspan=4, padx=20, pady=10)

        iters_label = ttk.Label(self, text="Number of Frames: " + str(self.app.simulator.num_frames),
                                font=tkFont.Font(size=14), justify="center", background='#D8E2DC')
        iters_label.grid(row=3, column=0, columnspan=4, padx=20, pady=10)

        model_label = ttk.Label(self, text="Bandit Model: " + self.app.simulator.bandit.type,
                                font=tkFont.Font(size=14), justify="center", background='#D8E2DC')
        model_label.grid(row=4, column=0, columnspan=4, padx=20, pady=10)

        arms_label = ttk.Label(self, text="Number of Arms: " + str(self.app.simulator.bandit.n_arms),
                               font=tkFont.Font(size=14), justify="center", background='#D8E2DC')
        arms_label.grid(row=5, column=0, columnspan=4, padx=20, pady=10)

        continue_button = ctk.CTkButton(self, text="START",
                                        command=lambda: self.app.set_page("simulation",
                                                                          kwargs={"contextual": self.contextual}),
                                        font=ctk.CTkFont(size=24))
        continue_button.grid(row=6, column=0, columnspan=4, padx=20, pady=10, ipadx=50, ipady=20)

    def open(self):
        self.app.simulator.run_simulation()
