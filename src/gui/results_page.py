import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

from src.simulation.simulator import Simulator
from .page import Page


# TODO: Fix out pane scaling and default width


class ResultsPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        title = ttk.Label(self, text="Results Page")
        title.pack(side=tk.TOP)

        panes = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        panes.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

        self.l_panel = _LeftPanel(self, self.controller.simulator)
        panes.add(self.l_panel, weight=1)
        self.r_panel = _RightPanel(self, self.controller.simulator)
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

        frames = self.controller.simulator.frames
        self.controller.simulator.generate_frame_graphs(len(frames) - 1)

        self.l_panel.update()
        self.r_panel.update()


class _RightPanel(ttk.LabelFrame):
    def __init__(self, parent, simulator: Simulator):
        super().__init__(parent, text="Reward/Regret Trends")
        self.simulator = simulator

    def update(self):
        output_dir = self.simulator.grapher.output_dir
        for i in range(self.simulator.n_arms):
            img = create_image_label(
                parent=self,
                image_filepath=output_dir / f"{i}_rewards.png",
                text=f"Restaurant #{i}",
                size=(96, 96),
                compound=tk.LEFT
            )
            img.grid(column=0, row=i)


class _LeftPanel(ttk.LabelFrame):
    def __init__(self, parent, simulator: Simulator):
        super().__init__(parent, text="Restaurant Sampling")
        self.simulator = simulator

    def update(self):
        output_dir = self.simulator.grapher.output_dir

        scatter = create_image_label(
            parent=self,
            image_filepath=output_dir / "scatter.png",
            text="placeholder_text_for_reward_regret_chart",
            size=(512, 128),
        )
        scatter.grid(column=0, row=0)

        standard_label = ttk.Label(
            self,
            text=f"""
                    The [MODEL NAME] model selected gained a total of [REWARD]
                    points over [N] iterations, with a total of [REGRET] missed
                    points. As you can see from the totals graphed over time,
                    the reward increases slowly as the Bandits explore, then settles
                    into a linear growth once the optimal arm is found and the
                    bandit starts to exploit it.
                    """
        )
        standard_label.grid(column=0, row=1)

        cumulative = create_image_label(
            parent=self,
            image_filepath=output_dir / "cum_scatter.png",
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
                    which in this case is set to 5, and the average regret should
                    approach 0. You can judge the selected model for yourself by
                    looking at the averages above, and the expected average reward
                    has been added for reference.
                    """
        )
        cumulative_label.grid(column=0, row=3)

def create_image_label(parent, image_filepath, text, size, *args, **kwargs):
    load = Image.open(image_filepath)
    load = load.resize(size)
    render = ImageTk.PhotoImage(load)
    img = ttk.Label(parent, text=text, image=render, *args, **kwargs)
    img.image = render
    return img
