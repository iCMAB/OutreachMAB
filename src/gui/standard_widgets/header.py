import tkinter as tk
from tkinter import ttk


class Header(ttk.LabelFrame):
    def __init__(self, master, app, title: str, forward_button_args: dict):
        super().__init__(master)

        back_button = tk.Button(
            self,
            height=2,
            width=5,
            text="BACK",
            command=lambda: app.back_page()
        )
        back_button.grid(column=0, row=0, sticky=tk.NW)

        title = ttk.Label(self, text=title, justify=tk.CENTER)
        title.grid(column=1, row=0, sticky=tk.NSEW)
        self.columnconfigure(1, weight=1)

        end_button = tk.Button(
            self,
            height=2,
            width=5,
            **forward_button_args,
        )
        end_button.grid(column=1, row=0, sticky=tk.NE)
