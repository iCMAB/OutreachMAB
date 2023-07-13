import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

from .page import Page

class SettingsPage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.grid_columnconfigure((1,2,3,4,5), weight=1)

        # label of frame Layout 2
        label = ttk.Label(self, text="Settings", font=tkFont.Font(size=18))

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=2, padx=10, pady=50)

        self.selected_bandit = tk.StringVar()
        self.selected_bandit.set("Random")

        #bandit model label and current selection
        model_label = ttk.Label(self, text='Bandit Model', font=tkFont.Font(size=18), background='#b0ada9', borderwidth=40, relief="solid")
        model_label.grid(row=1, column=1, padx=(10,0), pady=10, columnspan=2, sticky="ew")

        model_selection = ttk.Label(self, textvariable=self.selected_bandit, font=tkFont.Font(size=18), background='#b0ada9', borderwidth=40, justify="left", relief="solid")
        model_selection.grid(row=1, column=3, pady=10, columnspan=2, sticky="ew")

        #bandit dropdown menu
        options = [
            "Random",
            "Linear UCB"
        ]

        bandit_dropdown = ttk.OptionMenu(self, self.selected_bandit, *options)
        bandit_dropdown.grid(row=1, column=5, pady=10, sticky="nsew")

        #number of arms label and entry box
        arms_label = ttk.Label(self, text="Number of Arms", font=tkFont.Font(size=18), background='#b0ada9',
                                borderwidth=20, relief="solid")
        arms_label.grid(row=2, column=1, padx=(10, 0), pady=10, columnspan=4, sticky="ew")

        self.num_of_arms = tk.IntVar(value=5)
        arms_number = ttk.Entry(self, exportselection=0, textvariable=self.num_of_arms, background='#b0ada9', justify='center', font=tkFont.Font(size=18))
        arms_number.grid(row=2, column=4, pady=10, sticky="nsew")

        #number of iterations label and entry box
        iterations_label = ttk.Label(self, text="Number of Iterations", font=tkFont.Font(size=18), background='#b0ada9',
                               borderwidth=20, relief="solid")
        iterations_label.grid(row=3, column=1, padx=(10, 0), pady=10, columnspan=4, sticky="ew")

        button1 = ttk.Button(self, text="Start",
                             command=lambda: controller.set_page("simulation"))
        button1.grid(row=4, column=1, padx=10, pady=10, ipadx=50, ipady=20)

        self.num_of_iters = tk.IntVar(value=100)
        iter_number = ttk.Entry(self, exportselection=0, textvariable=self.num_of_iters, background='#b0ada9', justify='center', font=tkFont.Font(size=18))
        iter_number.grid(row=3, column=4, pady=10, sticky="nsew")
