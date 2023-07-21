import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

from src.simulation.bandits import BANDITS
from .page import Page

class SettingsPage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.grid_columnconfigure((1, 2, 3, 4, 5), weight=2)
        self.grid_columnconfigure(6, weight=1)
        self.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)

        # label of frame Layout 2
        label = tk.Label(self, text="Settings", font=tkFont.Font(size=18))

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=3, padx=10, pady=50)

        self.selected_bandit = tk.StringVar()
        self.selected_bandit.set("Random")

        #bandit model label and current selection
        model_label = ttk.Label(self, text='Bandit Model', font=tkFont.Font(size=18), background='#b0ada9', borderwidth=40, relief="solid")
        model_label.grid(row=1, column=1, padx=(10,0), pady=10, sticky="nsew", columnspan=2)

        model_selection = ttk.Label(self, textvariable=self.selected_bandit, font=tkFont.Font(size=18), background='#b0ada9', borderwidth=40, justify="left", relief="solid")
        model_selection.grid(row=1, column=3, pady=10, columnspan=3, sticky="nsew")

        #the actual menu for bandit selection
        bandit_menu_button = tk.Menubutton(self, background='#b0ada9', borderwidth=1, relief="solid", text="V")
        bandit_menu = tk.Menu(bandit_menu_button, tearoff=False)
        bandit_menu_button.configure(menu=bandit_menu)

        #ALL BANDIT OPTIONS GO HERE
        bandit_menu.add_radiobutton(label="Random", variable=self.selected_bandit, value="Random")
        bandit_menu.add_radiobutton(label="Epsilon Greedy", variable=self.selected_bandit, value="Epsilon Greedy")
        bandit_menu.add_radiobutton(label="Thompson Sampling", variable=self.selected_bandit, value="Thompson Sampling")
        #END BANDIT OPTIONS

        bandit_menu_button.grid(row=1, column=6, padx=(0, 10), pady=10, sticky="nsew")


        #number of arms label and entry box
        arms_label = ttk.Label(self, text="Number of Arms", font=tkFont.Font(size=18), background='#b0ada9',
                                borderwidth=20, relief="solid")
        arms_label.grid(row=2, column=1, padx=(10, 0), pady=10, columnspan=4, sticky="nsew")

        self.num_of_arms = tk.IntVar(value=5)
        self.arms_number = tk.Entry(self, exportselection=0, textvariable=self.num_of_arms, background='#b0ada9', justify='center', font=tkFont.Font(size=18))
        self.arms_number.grid(row=2, column=4, padx=(0, 10), pady=10, sticky="nsew", columnspan=3)

        #number of iterations label and entry box
        iterations_label = ttk.Label(self, text="Number of Iterations", font=tkFont.Font(size=18), background='#b0ada9',
                               borderwidth=20, relief="solid")
        iterations_label.grid(row=3, column=1, padx=(10, 0), pady=10, columnspan=4, sticky="nsew")

        self.num_of_iters = tk.IntVar(value=100)

        self.iter_number = tk.Entry(self, exportselection=0, textvariable=self.num_of_iters, background='#b0ada9', justify='center', font=tkFont.Font(size=18))
        self.iter_number.grid(row=3, column=4, padx=(0, 10), pady=10, sticky="nsew", columnspan=3)

        def start():

            self.controller.simulation.num_frames = int(self.iter_number.get())
            self.controller.simulation.bandit: BanditModel = BANDITS[self.selected_bandit.get()] \
                (n_arms=int(self.arms_number.get()), **self.controller.simulation.config["bandit"]["parameters"])
            self.controller.simulation.n_arms = self.arms_number.get()

            self.parent.children['!intropage'].update()
            self.controller.set_page("intro")


        button1 = ttk.Button(self, text="Start", command=start)
        button1.grid(row=5, column=1, padx=10, pady=10, ipadx=50, ipady=20)

        button2 = ttk.Button(self, text="What do these mean?", command=lambda: controller.set_page("settings_explained"))
        button2.grid(row=4, column=1, padx=10, pady=10, ipadx=50, ipady=20)

