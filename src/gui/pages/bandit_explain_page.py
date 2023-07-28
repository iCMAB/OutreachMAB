import tkinter.font as tkFont
import tkinter as tk
import webbrowser

from src.gui.standard_widgets import Page, Header


class BanditExplainPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        header = Header(
            master=self,
            app=self.app,
            title="Bandit Explanation",
            forward_button_args={
                "text": "NEXT",
                "command": lambda: self.app.set_page("settings"),
            }
        )
        header.grid(column=0, row=0, columnspan=5, sticky=tk.NSEW)

        self.columnconfigure((0, 3), weight=1)
        self.rowconfigure(4, weight=1)

        explain_text = tk.Label(self, text=" A Multi-Armed Bandit problem is one in which the problem has given multiple options, all with different\nrewards, where"\
                                 " at any given time, we can only select one option. The goal of the bandit is to leverage a\nmachine learning algorithm, in order"\
                                 " to make the best selection each time the decision needs to be made.\n\nTo learn more about multi-armed bandits, see the supporting presentation.", justify="center")
        explain_text.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        slides_button = tk.Button(self, text="Show Me the Presentation", command=lambda: webbrowser.open_new_tab("https://docs.google.com/presentation/d/1nfdbCnrvaHLtVeKtXrGiCp7zwmGpY7rCum5SNdVkCjk"))
        slides_button.grid(row=2, column=1, columnspan=2, padx=5, pady=10, ipadx=50, ipady=20)

        next_button = tk.Button(self, text="Continue", command=lambda: self.app.set_page("settings"))
        next_button.grid(row=3, column=2, padx=10, pady=10, ipadx=50, ipady=20)

        back_button = tk.Button(self, text="Back to Start", command=lambda: self.app.set_page("start"))
        back_button.grid(row=3, column=1, padx=10, pady=10, ipadx=50, ipady=20)





