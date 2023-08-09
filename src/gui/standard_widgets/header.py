import tkinter as tk
from tkinter import ttk


class Header(tk.LabelFrame):
    def __init__(self, master, app, title: str, forward_button_args: dict):
        super().__init__(master)
        self.configure(background='#D8E2DC')

        back_button = tk.Button(
            self,
            height=2,
            width=8,
            text="BACK",
            bg='#3B8ED0', activebackground='#36719F', fg='#DCE4EE',
            font=tk.font.Font(size=16),
            command=lambda: app.back_page()
        )
        back_button.grid(column=0, row=0, sticky=tk.NW)

        title = ttk.Label(
            self,
            text=title,
            anchor=tk.CENTER,
            background='#D8E2DC',
            font=("Arial", 24, "bold")
        )
        title.grid(column=1, row=0, sticky=tk.NSEW)
        self.columnconfigure(1, weight=1)

        end_button = tk.Button(
            self,
            height=2,
            width=8,
            font=tk.font.Font(size=16),
            bg='#3B8ED0',
            activebackground='#36719F',
            fg='#DCE4EE',
            **forward_button_args,
        )
        end_button.grid(column=1, row=0, sticky=tk.NE)
