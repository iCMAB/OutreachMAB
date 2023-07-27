import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

from src.gui.standard_widgets.page import Page
from src.simulation.bandits import BANDITS, BanditModel


class SettingsPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # noinspection PyTypeChecker
        self.columnconfigure((1, 2, 3, 4, 5), weight=2)
        self.columnconfigure(6, weight=1)
        # noinspection PyTypeChecker
        self.rowconfigure((1, 2, 3, 4, 5), weight=1)

        self.selected_bandit = tk.StringVar()
        self.selected_bandit.set("Random")

        #bandit model label and current selection
        model_label = ttk.Label(self, text='Bandit Model', font=tkFont.Font(size=18), background='#b0ada9', borderwidth=40, relief="solid")
        model_label.grid(row=1, column=1, padx=(10,0), pady=(10, 5), sticky="nsew", columnspan=2)

        model_selection = ttk.Label(self, textvariable=self.selected_bandit, font=tkFont.Font(size=18), background='#b0ada9', borderwidth=40, justify="left", relief="solid")
        model_selection.grid(row=1, column=3, pady=(10,5), columnspan=3, sticky="nsew")

        #the actual menu for bandit selection
        bandit_menu_button = tk.Menubutton(self, background='#b0ada9', borderwidth=1, relief="solid", text="V")
        bandit_menu = tk.Menu(bandit_menu_button, tearoff=False)
        bandit_menu_button.configure(menu=bandit_menu)

        #ALL BANDIT OPTIONS GO HERE
        bandit_menu.add_radiobutton(label="Random", variable=self.selected_bandit, value="Random")
        bandit_menu.add_radiobutton(label="Epsilon Greedy", variable=self.selected_bandit, value="Epsilon Greedy")
        bandit_menu.add_radiobutton(label="Thompson Sampling", variable=self.selected_bandit, value="Thompson Sampling")
        #END BANDIT OPTIONS

        bandit_menu_button.grid(row=1, column=6, padx=(0, 10), pady=(10, 5), sticky="nsew")

        bandit_menu_desc = tk.Label(self, text="Bandit Model: This is the type of algorithm the bandit" \
                                               " will be using when selecting\nan option for each frame.",
                                    justify="left", font=tkFont.Font(size=12))

        bandit_menu_desc.grid(row=2, column=1, columnspan=6, padx=10, pady=(0, 10), sticky="nsew")


        #number of arms label and entry box
        arms_label = ttk.Label(self, text="Number of Arms", font=tkFont.Font(size=18), background='#b0ada9',
                                borderwidth=20, relief="solid")
        arms_label.grid(row=3, column=1, padx=(10, 0), pady=(10, 5), columnspan=4, sticky="nsew")

        self.num_of_arms = tk.IntVar(value=5)
        self.arms_number = tk.Entry(self, exportselection=False, textvariable=self.num_of_arms, background='#b0ada9',
                                    justify='center', font=tkFont.Font(size=18))
        self.arms_number.grid(row=3, column=4, padx=(0, 10), pady=(10, 5), sticky="nsew", columnspan=3)

        num_arms_desc = tk.Label(self,
                                 text="Number of Arms: This controls the number of possible restaurants the bandit can\n" \
                                      "choose from in each frame.", justify="left", font=tkFont.Font(size=12))

        num_arms_desc.grid(row=4, column=1, columnspan=6, padx=10, pady=(0, 10), sticky="nsew")

        #number of iterations label and entry box
        iterations_label = ttk.Label(self, text="Number of Iterations", font=tkFont.Font(size=18), background='#b0ada9',
                               borderwidth=20, relief="solid")
        iterations_label.grid(row=5, column=1, padx=(10, 0), pady=(10,5), columnspan=4, sticky="nsew")

        self.num_of_iters = tk.IntVar(value=100)

        self.iter_number = tk.Entry(self, exportselection=False, textvariable=self.num_of_iters, background='#b0ada9',
                                    justify='center', font=tkFont.Font(size=18))
        self.iter_number.grid(row=5, column=4, padx=(0, 10), pady=(10, 5), sticky="nsew", columnspan=3)

        num_iter_desc = tk.Label(self,
                                 text="Number of Iterations: This is the total number of frames that will be included\nin the simulation.\n\n" \
                                      "WARNING: With a low number of iterations the bandit may not have enough time to\nexplore and may not end up having a high rate of success.",
                                 justify="left", font=tkFont.Font(size=12))

        num_iter_desc.grid(row=6, column=1, columnspan=6, padx=10, pady=(0, 10), sticky="nsew")

        def start():
            self.app.simulator.num_frames = int(self.iter_number.get())
            # noinspection PyTypeHints
            self.app.simulator.bandit: BanditModel = BANDITS[self.selected_bandit.get()] \
                (n_arms=int(self.arms_number.get()), **self.app.simulator.config["bandit"]["parameters"])
            self.app.simulator.n_arms = self.arms_number.get()

            self.app.set_page("intro")

        button1 = ttk.Button(self, text="Start", command=start)
        button1.grid(row=7, column=1, padx=10, pady=10, ipadx=50, ipady=20)
