import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

import numpy as np

from src.gui.standard_widgets import Page, Updatable, Header, ImageLabel

DARK_BUTTON_BG = "#ff8080"
LIGHT_BUTTON_BG = "#f0f0f0"


class SimulationPage(Updatable, Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frame_num_var = tk.IntVar()

        self.columnconfigure(0, weight=1)

        header = Header(
            master=self,
            app=self.app,
            title="Simulation Page",
            forward_button_args={
                "text": "END",
                "command": lambda: self.app.set_page("results"),
            }
        )
        header.grid(column=0, row=0, sticky=tk.NSEW)
        self.rowconfigure(0, weight=0, minsize=32)

        panes = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        panes.grid(column=0, row=1, sticky=tk.NSEW)
        self.rowconfigure(1, weight=1)

        l_panel = _LeftPanel(master=self, page=self, frame_num_var=self.frame_num_var)
        panes.add(l_panel, weight=1)
        self.subwidgets.append(l_panel)

        r_panel = _RightPanel(master=self, page=self, frame_num_var=self.frame_num_var)
        panes.add(r_panel, weight=1)
        self.subwidgets.append(r_panel)

    def open(self):
        self.app.simulator.run_simulation()
        self.update()

    def update(self):
        self.app.simulator.generate_frame_graphs(frame_num=self.frame_num_var.get())
        super().update()


class _LeftPanel(Updatable, ttk.Frame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master)
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var

        self.columnconfigure(0, weight=1)

        header = _LeftHeader(master=self, page=self.page, frame_num_var=self.frame_num_var)
        header.grid(column=0, row=0, sticky=tk.NSEW)
        self.subwidgets.append(header)
        self.rowconfigure(index=0, weight=0, minsize=32)

        frame_info = _FrameInfo(master=self, page=self.page, frame_num_var=self.frame_num_var)
        frame_info.grid(column=0, row=1, sticky=tk.NSEW)
        self.subwidgets.append(frame_info)
        self.rowconfigure(index=1, weight=0, minsize=128)

        charts = _Charts(master=self, page=self.page, frame_num_var=self.frame_num_var)
        charts.grid(column=0, row=2, sticky=tk.NSEW)
        self.subwidgets.append(charts)
        self.rowconfigure(index=2, weight=1)


class _LeftHeader(ttk.LabelFrame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master, text="TEST")
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var

        self.frame_entry = tk.StringVar(value=str(self.frame_num_var.get()))

        self.left_button = tk.Button(
            self,
            text="PREV",
            height=2,
            width=5,
            command=self.decrement_frame_num,
        )
        self.left_button.grid(column=0, row=0)

        self.right_button = tk.Button(
            self,
            height=2,
            width=5,
            text="NEXT",
            command=self.increment_frame_num,
        )
        self.right_button.grid(column=1, row=0)

        current_iter = ttk.Entry(
            self,
            font=tkfont.Font(family='Times', size=16),
            foreground="#333333",
            justify="center",
            textvariable=self.frame_entry,
        )
        current_iter.grid(column=2, row=0)
        current_iter.bind(sequence="<Key-Return>", func=self.entry_submit)

        right_button = tk.Button(
            self,
            height=2,
            width=5,
            text="JUMP",
            command=self.entry_submit,
        )
        right_button.grid(column=4, row=0)

    def update(self) -> None:
        frame_num = self.frame_num_var.get()
        self.frame_entry.set(str(frame_num))

        self.right_button.config(bg=LIGHT_BUTTON_BG)
        self.left_button.config(bg=LIGHT_BUTTON_BG)

        if frame_num >= self.simulator.num_frames - 1:
            self.right_button.config(bg=DARK_BUTTON_BG)
        elif frame_num <= 0:
            self.left_button.config(bg=DARK_BUTTON_BG)

    def entry_submit(self, *args):
        try:
            new_frame_num = int(self.frame_entry.get())
            new_frame_num = max(0, new_frame_num)
            new_frame_num = min(new_frame_num, self.simulator.num_frames - 1)
            self.frame_num_var.set(new_frame_num)
        except ValueError:
            self.frame_entry.set(str(self.frame_num_var.get()))
        self.page.update()


    def increment_frame_num(self):
        self.frame_num_var.set(min(self.frame_num_var.get() + 1, self.simulator.num_frames - 1))
        if self.frame_num_var.get() >= self.simulator.num_frames - 1:
            self.right_button.config(bg=DARK_BUTTON_BG)
        self.left_button.config(bg=LIGHT_BUTTON_BG)
        self.page.update()

    def decrement_frame_num(self):
        self.frame_num_var.set(max(0, self.frame_num_var.get() - 1))
        if self.frame_num_var.get() <= 0:
            self.left_button.config(bg=DARK_BUTTON_BG)
        self.right_button.config(bg=LIGHT_BUTTON_BG)
        self.page.update()


class _FrameInfo(Updatable, ttk.LabelFrame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master, text="Frame Information")
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var

    def update(self):
        super().update()

        frame = self.simulator.frames[self.frame_num_var.get()]

        choice_label = ttk.Label(master=self, text=f"Restaurant Choice: {frame.choice}")
        choice_label.grid(column=0, row=0)

        reward_label = ttk.Label(master=self, text=f"Reward: {frame.reward:0.2f}")
        reward_label.grid(column=0, row=1)

        regret_label = ttk.Label(master=self, text=f"Regret: {frame.regret:0.2f}")
        regret_label.grid(column=0, row=2)


class _Charts(Updatable, ttk.LabelFrame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master, text="Reward/Regret Charts")
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var

    def update(self):
        output_dir = self.simulator.grapher.output_dir

        avg_scatter = ImageLabel(
            master=self,
            image_filepath=output_dir / "avg_scatter.png",
            text="placeholder_text_for_reward_regret_chart",
            size=(512, 128),
        )
        avg_scatter.grid(column=0, row=0)

        standard_label = ttk.Label(
            self,
            text="Average reward and regret"
        )
        standard_label.grid(column=0, row=1)

        cumulative = ImageLabel(
            master=self,
            image_filepath=output_dir / "cum_scatter.png",
            text="placeholder_text_for_cumulative_chart",
            size=(512, 128),
        )
        cumulative.grid(column=0, row=2)

        cumulative_label = ttk.Label(
            self,
            text="Cumulative reward and regret"
        )
        cumulative_label.grid(column=0, row=3)


class _RightPanel(ttk.Frame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master)
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var

    def update(self):
        output_dir = self.simulator.grapher.output_dir
        for i in range(int(self.simulator.n_arms)):
            restaurant_frame = ttk.LabelFrame(master=self, text=f"Restaurant #{i}")
            restaurant_frame.grid(column=0, row=i, sticky=tk.NSEW)
            self.columnconfigure(index=0, weight=1)

            image_label = ImageLabel(
                master=restaurant_frame,
                image_filepath=output_dir / f"{i}_rewards.png",
                text=f"Restaurant #{i} graph placeholder",
                size=(96, 96),
            )
            image_label.grid(column=0, row=0, rowspan=3)

            frames = self.simulator.frames[:self.frame_num_var.get() + 1]
            rewards = [frame.rewards[i] for frame in frames if i == frame.choice]

            samples_label = ttk.Label(restaurant_frame, text=f"Number of Samples: {len(rewards)}")
            samples_label.grid(column=1, row=0)

            avg_reward = f"{np.average(rewards):0.2f}" if len(rewards) > 0 else "N/A"
            avg_label = ttk.Label(restaurant_frame, text=f"Average Reward: {avg_reward}")
            avg_label.grid(column=1, row=1)

            std_dev = f"{np.std(rewards):0.2f}" if len(rewards) > 0 else "N/A"
            sd_label = ttk.Label(restaurant_frame, text=f"Standard Deviation: {std_dev}")
            sd_label.grid(column=1, row=2)
