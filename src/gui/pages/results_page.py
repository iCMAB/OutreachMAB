import tkinter as tk
from tkinter import ttk

import customtkinter as ctk
import numpy as np

from src.gui.standard_widgets import Page, ImageLabel, Header
from src.simulation.simulator import Simulator


class ResultsPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(background='#D8E2DC')
        self.columnconfigure(0, weight=1)

        header = Header(
            master=self,
            app=self.app,
            title="Simulation Results",
            forward_button_args={
                "text": "RESTART",
                "command": lambda: self.app.set_page("start"),
            }
        )
        header.grid(column=0, row=0, sticky=tk.NSEW)
        self.rowconfigure(0, weight=0, minsize=32)

        panes = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        panes.grid(column=0, row=1, sticky=tk.NSEW)
        self.rowconfigure(1, weight=1)

        self.l_panel = _LeftPanel(self, self.app.simulator)
        panes.add(self.l_panel, weight=1)
        self.r_panel = _RightPanel(self, self.app.simulator)
        panes.add(self.r_panel, weight=1)

    def open(self):
        self.update()

    def update(self, full_update: bool = True):
        default = ttk.Style().configure(
            "TLabel",
            font=("Times", 12),
            foreground="#333333",
            justify="left"
        )

        frames = self.app.simulator.frames
        self.app.simulator.generate_frame_graphs(len(frames) - 1)

        self.l_panel.update()
        self.r_panel.update()


class _RightPanel(tk.LabelFrame):
    def __init__(self, parent, simulator: Simulator):
        super().__init__(parent, text="Reward/Regret Trends")
        self.parent = parent
        self.simulator = simulator
        self.configure(background='#D8E2DC')

    def update(self):
        output_dir = self.simulator.grapher.output_dir
        for i in range(int(self.simulator.n_arms)):
            restaurant_frame = tk.LabelFrame(master=self, text=f"Restaurant #{i}", background='#D8E2DC')
            restaurant_frame.grid(column=0, row=i)

            image_label = ImageLabel(
                master=restaurant_frame,
                image_filepath=output_dir / f"{i}_rewards.png",
                text=f"Restaurant #{i} graph placeholder",
                size=(144, 96),
            )
            image_label.grid(column=0, row=0, rowspan=3)

            rewards = self.simulator.get_rewards(arm_index=i)
            samples_label = ttk.Label(restaurant_frame, text=f"Number of Samples: {len(rewards)}", background='#D8E2DC')
            samples_label.grid(column=1, row=0)
            avg_reward = np.average(rewards)
            avg_label = ttk.Label(restaurant_frame, text=f"Average Reward: {avg_reward:0.2f}", background='#D8E2DC')
            avg_label.grid(column=1, row=1)
            std_dev = np.std(rewards)
            sd_label = ttk.Label(restaurant_frame, text=f"Standard Deviation: {std_dev:0.2f}", background='#D8E2DC')
            sd_label.grid(column=1, row=2)

        quit_button = ctk.CTkButton(self, text="Quit", command=lambda: self.parent.app.destroy(), font=ctk.CTkFont(size=24))
        quit_button.grid(row=self.simulator.n_arms, column=0, padx=10, pady=10, ipadx=50, ipady=20)


class _LeftPanel(tk.LabelFrame):
    def __init__(self, parent, simulator: Simulator):
        super().__init__(parent, text="Restaurant Sampling")
        self.simulator = simulator
        self.configure(background='#D8E2DC')

    def update(self):
        output_dir = self.simulator.grapher.output_dir

        avg_scatter = ImageLabel(
            master=self,
            image_filepath=output_dir / "cum_scatter.png",
            text="placeholder_text_for_reward_regret_chart",
            size=(512, 128),
        )
        avg_scatter.grid(column=0, row=0)

        total_reward = sum(frame.reward for frame in self.simulator.frames)
        total_regret = sum(frame.regret for frame in self.simulator.frames)
        standard_label = ttk.Label(
            self,
            text=f"""
            The {self.simulator.bandit.type} model selected gained a total of {total_reward:0.1f}
            points over {self.simulator.num_frames} iterations, with a total of {total_regret:0.1f} missed
            points. As you can see from the totals graphed over time,
            the reward increases slowly as the Bandits explore, then settles
            into a linear growth once the optimal arm is found and the
            bandit starts to exploit it.
            """,
            background = '#D8E2DC'
        )
        standard_label.grid(column=0, row=1)

        cumulative = ImageLabel(
            master=self,
            image_filepath=output_dir / "avg_scatter.png",
            text="placeholder_text_for_cumulative_chart",
            size=(512, 128),
        )
        cumulative.grid(column=0, row=2)

        cumulative_label = ttk.Label(
            self,
            text=f"""
            One of the methods used to judge the efficacy of Bandit models
            is the trend of the average reward and regret over the course
            of a simulation. A strong bandit model should have an average
            reward that approaches the average return of the optimal arm,
            which in this case is set to {self.simulator.n_arms}, and the average regret should
            approach 0. You can judge the selected model for yourself by
            looking at the averages above, and the expected average reward
            has been added for reference.
            """,
            background = '#D8E2DC'
        )
        cumulative_label.grid(column=0, row=3)
