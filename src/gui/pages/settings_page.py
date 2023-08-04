import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

from src.gui.standard_widgets import Page, Header, BoundedEntry
from src.simulation.bandits import STANDARD_BANDITS, CONTEXTUAL_BANDITS


class SettingsPage(Page):
    def __init__(self, contextual: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        header = Header(
            master=self,
            app=self.app,
            title="Settings",
            forward_button_args={
                "text": "NEXT",
                "command": lambda: self.app.set_page("intro")
            }
        )
        header.grid(column=0, columnspan=7, row=0, sticky=tk.NSEW)

        # noinspection PyTypeChecker
        self.columnconfigure((1, 2, 3, 4, 5), weight=2)
        self.columnconfigure(6, weight=1)
        # noinspection PyTypeChecker
        self.rowconfigure((1, 2, 3, 4, 5), weight=1)

        #bandit model label and current selection
        model_label = ttk.Label(
            self,
            text='Bandit Model',
            font=tkFont.Font(size=18),
            background='#b0ada9',
            borderwidth=40,
            relief="solid"
        )
        model_label.grid(row=1, column=1, padx=(10,0), pady=(10, 5), sticky="nsew", columnspan=2)

        self.selected_bandit = tk.StringVar()

        model_selection = ttk.Label(
            self,
            textvariable=self.selected_bandit,
            font=tkFont.Font(size=18),
            background='#b0ada9',
            borderwidth=40,
            justify="left",
            relief="solid"
        )
        model_selection.grid(row=1, column=3, pady=(10,5), columnspan=3, sticky="nsew")

        #the actual menu for bandit selection
        bandit_menu_button = tk.Menubutton(self, background='#b0ada9', borderwidth=1, relief="solid", text="V")
        bandit_menu = tk.Menu(bandit_menu_button, tearoff=False)
        bandit_menu_button.configure(menu=bandit_menu)

        # Dynamically load bandit options
        if not contextual:
            bandits = STANDARD_BANDITS
        else:
            bandits = CONTEXTUAL_BANDITS
        for name in bandits.keys():
            bandit_menu.add_radiobutton(label=name, variable=self.selected_bandit, value=name)
        self.selected_bandit.set(list(bandits.keys())[0])

        bandit_menu_button.grid(row=1, column=6, padx=(0, 10), pady=(10, 5), sticky="nsew")

        bandit_menu_desc = tk.Label(self, text="Bandit Model: This is the type of algorithm the bandit" \
                                               " will be using when selecting\nan option for each frame.",
                                    justify="left", font=tkFont.Font(size=12))

        bandit_menu_desc.grid(row=2, column=1, columnspan=6, padx=10, pady=(0, 10), sticky="nsew")


        #number of arms label and entry box
        arms_label = ttk.Label(self, text="Number of Arms", font=tkFont.Font(size=18), background='#b0ada9',
                                borderwidth=20, relief="solid")
        arms_label.grid(row=3, column=1, padx=(10, 0), pady=(10, 5), columnspan=4, sticky="nsew")

        self.num_arms_var = tk.StringVar(value="5")
        self.num_arms_entry = BoundedEntry(
            master=self,
            minimum=1,
            maximum=5,
            default=5,
            var=self.num_arms_var,
            exportselection=False,
            background='#b0ada9',
            justify='center',
            font=tkFont.Font(size=18))
        self.num_arms_entry.grid(row=3, column=4, padx=(0, 10), pady=(10, 5), sticky="nsew", columnspan=3)

        num_arms_desc = tk.Label(self,
                                 text="Number of Arms: This controls the number of possible restaurants the bandit can\n" \
                                      "choose from in each frame.", justify="left", font=tkFont.Font(size=12))

        num_arms_desc.grid(row=4, column=1, columnspan=6, padx=10, pady=(0, 10), sticky="nsew")

        #number of iterations label and entry box
        iterations_label = ttk.Label(self, text="Number of Iterations", font=tkFont.Font(size=18), background='#b0ada9',
                               borderwidth=20, relief="solid")
        iterations_label.grid(row=5, column=1, padx=(10, 0), pady=(10,5), columnspan=4, sticky="nsew")

        self.num_frames_var = tk.StringVar(value="100")
        self.num_frames_entry = BoundedEntry(
            master=self,
            minimum=1,
            maximum=1024,
            default=100,
            var=self.num_frames_var,
            exportselection=False,
            background='#b0ada9',
            justify='center',
            font=tkFont.Font(size=18)
        )
        self.num_frames_entry.grid(row=5, column=4, padx=(0, 10), pady=(10, 5), sticky="nsew", columnspan=3)

        num_iter_desc = tk.Label(self,
                                 text="Number of Iterations: This is the total number of frames that will be included\nin the simulation.\n\n" \
                                      "WARNING: With a low number of iterations the bandit may not have enough time to\nexplore and may not end up having a high rate of success.",
                                 justify="left", font=tkFont.Font(size=12))

        num_iter_desc.grid(row=6, column=1, columnspan=6, padx=10, pady=(0, 10), sticky="nsew")

        button1 = ttk.Button(self, text="Start", command=lambda: self.app.set_page("intro"))
        button1.grid(row=7, column=1, padx=10, pady=10, ipadx=50, ipady=20)

    def close(self):
        num_arms = int(self.num_arms_var.get())
        self.app.create_simulator(
            num_frames=int(self.num_frames_var.get()),
            bandit=self.selected_bandit.get(),
            n_arms=num_arms
        )
