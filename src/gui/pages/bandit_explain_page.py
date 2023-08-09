import tkinter as tk
import webbrowser

import customtkinter as ctk
from src.gui.standard_widgets import Page, Header


class BanditExplainPage(Page):
    def __init__(self, contextual: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        header = Header(
            master=self,
            app=self.app,
            title="Bandit Explanation",
            forward_button_args={
                "text": "NEXT",
                "command": lambda: self.app.set_page("settings", kwargs={"contextual": contextual}),
            }
        )
        header.grid(column=0, row=0, columnspan=5, sticky=tk.NSEW)

        self.columnconfigure((0, 3), weight=1)
        self.rowconfigure(4, weight=1)

        if not contextual:
            bandit_explanation = """
            A Multi-Armed Bandit problem is one in which the problem has given multiple options, all with different
            rewards, where at any given time, we can only select one option. The goal of the bandit is to leverage a
            machine learning algorithm, in order to make the best selection each time the decision needs to be made.
            
            To learn more about multi-armed bandits, see the supporting presentation.
            """
        else:
            bandit_explanation = """
            A Contextual Multi-Armed Bandit (often shortened to Contextual Bandits) is an extension of the
            Multi-Armed Bandit problem where the Bandit Algorithms have contextual information that may affect
            the expected reward for each option. For example, a standard MAB that recommends content on a website
            treats every visitor identically, but a Contextual Bandit gets additional information about the
            visitor's preferences and can tailor the recommendation to the specific visitor.
            
            To learn more about contextual bandits, see the supporting presentation.
            """
        explain_text = tk.Label(self, text=bandit_explanation, justify="center", bg='#D8E2DC', font=tk.font.Font(size=14))
        explain_text.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        slides_button = ctk.CTkButton(
            self,
            text="Show Me the Presentation",
            command=lambda: webbrowser.open_new_tab("https://docs.google.com/presentation/d/1nfdbCnrvaHLtVeKtXrGiCp7zwmGpY7rCum5SNdVkCjk"),
            font=ctk.CTkFont(size=24)
        )
        slides_button.grid(row=2, column=1, columnspan=2, padx=5, pady=10, ipadx=50, ipady=20)

        next_button = ctk.CTkButton(
            self,
            text="Next: Settings",
            command=lambda: self.app.set_page("settings", kwargs={"contextual": contextual}),
            font=ctk.CTkFont(size=24)
        )
        next_button.grid(row=3, column=2, padx=10, pady=10, ipadx=50, ipady=20)

        back_button = ctk.CTkButton(self, text="Back to Start", command=lambda: self.app.set_page("start"), font=ctk.CTkFont(size=24))
        back_button.grid(row=3, column=1, padx=10, pady=10, ipadx=50, ipady=20)





