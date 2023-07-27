import tkinter.font as tkFont
from tkinter import ttk

from src.gui.standard_widgets.page import Page


class SettingsExplainPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        explain_text = ttk.Label(self,
                                 text="In the context of the activity, these settings mean the following:\n\nBandit Model: This is the type of algorithm the bandit" \
                                      " will be using when selecting\nan option for each frame.\n\nNumber of Arms: This controls the number of possible restaurants the bandit\ncan" \
                                      " choose from in each frame.\n\nNumber of Iterations: This is the total number of frames that will be included\nin the simulation.\n\n" \
                                      "WARNING: With a low number of iterations the bandit may not have enough time to\nexplore and may not end up having a high rate of success.",
                                 justify="left", font=tkFont.Font(size=12))

        # grid
        explain_text.grid(row=0, column=0, padx=20, pady=(50, 10))

        button1 = ttk.Button(self, text="Back", command=lambda: self.app.set_page("settings"))
        button1.grid(row=1, column=0, padx=10, pady=10, ipadx=50, ipady=20)