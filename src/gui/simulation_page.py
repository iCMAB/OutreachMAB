import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from typing import Optional

from .page import Page

class SimulationPage(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.formats = {
            "restaurant": "Selected: Restaurant {}",
            "reward": "Reward: {:4f}",
            "regret": "Regret: {:4f}",
        }

        # Variables for labels
        self.iter = tk.IntVar()
        self.restaurant_string = tk.StringVar()
        self.reward_string = tk.StringVar()
        self.regret_string = tk.StringVar()

        nav_button_style = ttk.Style().configure(
            "Nav.TButton",
            background="#f0f0f0",
            font=('Times', 30),
            foreground="#000000",
            justify="center",
        )

        right_button = ttk.Button(
            self,
            style="Nav.TButton",
            text=">",
            command=self.increaseCommand
        )
        right_button.place(x=390, y=370, width=140, height=80)

        left_button = ttk.Button(
            self,
            style="Nav.TButton",
            text="<",
            command=self.decreaseCommand
        )
        left_button.place(x=60, y=370, width=140, height=80)

        current_iter = ttk.Label(
            self,
            font=tkfont.Font(family='Times', size=50),
            foreground="#333333",
            justify="center",
            textvariable=self.iter,
        )
        current_iter.place(x=230, y=370, width=131, height=65)

        label_style = ttk.Style().configure(
            "TLabel",
            font=("Times", 23),
            foreground="#333333",
            justify="left"
        )

        selection_label = ttk.Label(self, textvariable=self.restaurant_string)
        selection_label.place(x=60, y=90, width=300, height=40)

        reward_label = ttk.Label(self, textvariable=self.reward_string)
        reward_label.place(x=60, y=150, width=300, height=40)

        regret_label = ttk.Label(self, textvariable=self.regret_string)
        regret_label.place(x=60, y=210, width=300, height=40)

    def open(self):
        self.controller.simulation.run_simulation()
        self.update_labels(frame_num=0)

    def increaseCommand(self):
        frame_num = self.iter.get() + 1

        self.update_labels(frame_num)

    def decreaseCommand(self):
        frame_num = max(0, self.iter.get() - 1)

        self.update_labels(frame_num)

    def update_labels(self, frame_num: Optional[int] = None):
        if frame_num is None:
            frame_num = self.iter.get()
        else:
            self.iter.set(frame_num)

        frame = self.controller.simulation.frames[frame_num]

        self.iter.set(frame_num)
        self.restaurant_string.set(self.formats["restaurant"].format(frame.choice))
        self.reward_string.set(self.formats["reward"].format(frame.reward))
        self.regret_string.set(self.formats["regret"].format(frame.regret))
