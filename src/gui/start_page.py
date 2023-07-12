import tkinter as tk
from tkinter import ttk

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Start Page")

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Start",
                             command=lambda: controller.set_page("simulation"))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Options")

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


        button3 = ttk.Button(self, text="Quit", command=lambda: controller.destroy())
        button3.grid(row=3, column=1, padx=10, pady=10)
