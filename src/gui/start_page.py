import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

from .page import Page

class StartPage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # label of frame Layout 2
        label = ttk.Label(self, text="Multi-Armed Bandit\nRestaurant Selector", justify="center", font=tkFont.Font(size=36))

        # putting the grid in its place by using
        self.grid_columnconfigure((0, 2), weight=1)
        # grid
        label.grid(row=0, column=1, padx=10, pady=50)


        button1 = ttk.Button(self, text="Start",
                             command=lambda: controller.set_page("simulation"))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10, ipadx=50, ipady=20)


        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Settings", command=lambda: controller.set_page("settings"))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10, ipadx=50, ipady=20)



        button3 = ttk.Button(self, text="Quit", command=lambda: controller.destroy())
        button3.grid(row=3, column=1, padx=10, pady=10, ipadx=50, ipady=20)



