import tkinter as tk
from tkinter import ttk

from .page import Page


class ResultsPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        panes = ttk.PanedWindow(self, orient="horizontal")
        panes.pack(fill=tk.BOTH, expand=True)

        left_panel = ttk.LabelFrame(panes)
        panes.add(left_panel)
        right_panel = ttk.LabelFrame(panes)
        panes.add(right_panel)

        test_label_style = ttk.Style().configure(
            "Label.Test.TLabel",
            background="#f0f0f0",
            font=('Times', 32),
            foreground="#000000",
            justify="center",
        )

        left_label = ttk.Label(left_panel, text="LEFT", style="Label.Test.TLabel")
        left_label.grid(column=0, row=0, sticky="nsew")

        right_label = ttk.Label(right_panel, text="RIGHT", style="Label.Test.TLabel")
        right_label.grid(column=0, row=0, sticky="nsew")

    def open(self):
        pass


class RestaurantResult(ttk.LabelFrame):
    def __init__(self, arm_index: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arm_index = arm_index
