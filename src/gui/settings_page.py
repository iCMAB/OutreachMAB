import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class SettingsPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Settings", justify="center", font=tkFont.Font(size=18))

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=3, padx=10, pady=50)

        button1 = ttk.Button(self, text="Start",
                             command=lambda: controller.set_page("simulation"))
        button1.grid(row=4, column=1, padx=10, pady=10, ipadx=50, ipady=20)
