import textwrap
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

import numpy as np

from src.gui.standard_widgets import Page, Subwidget, Header, ImageLabel, BoundedEntry, ToolTip


class SimulationPage(Subwidget, Page):
    def __init__(self, contextual: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.contextual = contextual

        self.frame_num_var = tk.IntVar()
        self.configure(background='#D8E2DC')

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
        ttk.Style().configure('panes', background='#D8E2DC')
        panes.grid(column=0, row=1, sticky=tk.NSEW)
        self.rowconfigure(1, weight=1)

        l_panel = _LeftPanel(master=self, page=self, frame_num_var=self.frame_num_var, contextual=self.contextual)
        panes.add(l_panel, weight=1)
        self.subwidgets.append(l_panel)

        r_panel = _RightPanel(master=self, page=self, frame_num_var=self.frame_num_var)
        panes.add(r_panel, weight=1)
        self.subwidgets.append(r_panel)

    def open(self):
        self.update()

    def update(self):
        self.app.simulator.generate_frame_graphs(frame_num=self.frame_num_var.get())
        super().update()


class _LeftPanel(Subwidget, tk.Frame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar, contextual: bool):
        super().__init__(master)
        self.contextual = contextual
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var

        self.columnconfigure(0, weight=1)

        header = _LeftHeader(master=self, page=self.page, frame_num_var=self.frame_num_var)
        header.grid(column=0, row=0, sticky=tk.NSEW)
        self.subwidgets.append(header)
        self.rowconfigure(index=0, weight=0, minsize=32)

        frame_info = _FrameInfo(master=self, page=self.page, frame_num_var=self.frame_num_var,
                                contextual=self.contextual)
        frame_info.grid(column=0, row=1, sticky=tk.NSEW)
        self.subwidgets.append(frame_info)
        self.rowconfigure(index=1, weight=0, minsize=128)

        charts = _Charts(master=self, page=self.page, frame_num_var=self.frame_num_var)
        charts.grid(column=0, row=2, sticky=tk.NSEW)
        self.subwidgets.append(charts)
        self.rowconfigure(index=2, weight=1)


class _LeftHeader(Subwidget, tk.LabelFrame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master, text="Frame Controls")
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var
        self.configure(background='#D8E2DC')

        self.left_button = tk.Button(
            self,
            text="PREV",
            height=2,
            width=5,
            command=self.decrement_frame_num,
            font=tkfont.Font(size=14),
            bg='#3B8ED0', activebackground='#36719F', fg='#DCE4EE'
        )
        self.left_button.grid(column=0, row=0)
        ToolTip(widget=self.left_button, text="Rewinds simulation by one frame")

        self.right_button = tk.Button(
            self,
            height=2,
            width=5,
            text="NEXT",
            command=self.increment_frame_num,
            font=tkfont.Font(size=14),
            bg='#3B8ED0', activebackground='#36719F', fg='#DCE4EE'
        )
        self.right_button.grid(column=1, row=0)
        ToolTip(widget=self.right_button, text="Advances simulation by one frame")

        self.frame_entry = tk.StringVar(value=str(self.frame_num_var.get()))
        current_iter = BoundedEntry(
            master=self,
            minimum=1,
            maximum=self.simulator.num_frames,
            default=1,
            var=self.frame_entry,
            func=self.entry_submit,
            font=tkfont.Font(family='Times', size=16),
            foreground="#333333",
            justify="center",
        )
        current_iter.grid(column=2, row=0)
        ToolTip(widget=current_iter, text="Manually input a frame index, input is automatically bounded")

        jump_button = tk.Button(
            self,
            height=2,
            width=5,
            text="JUMP",
            command=self.entry_submit,
            font=tkfont.Font(size=14),
            bg='#3B8ED0', activebackground='#36719F', fg='#DCE4EE'
        )
        jump_button.grid(column=4, row=0)
        ToolTip(
            widget=jump_button,
            text="Submit frame entry, clicking outside of text box or hitting <Enter> also submits entry"
        )

        self.cur_frame_label = tk.Label(
            self,
            text=f"{self.frame_num_var.get() + 1}/{self.simulator.num_frames}",
            background='#D8E2DC',
            foreground='#525B76',
            font=tkfont.Font(size=18))
        self.cur_frame_label.grid(column=5, row=0)

    def update(self) -> None:
        frame_num = self.frame_num_var.get()
        self.frame_entry.set(str(frame_num + 1))

        self.cur_frame_label.config(text=f"{frame_num + 1}/{self.simulator.num_frames}")

        self.left_button.config(state=tk.NORMAL)
        self.right_button.config(state=tk.NORMAL)

        if frame_num >= self.simulator.num_frames - 1:
            self.right_button.config(state=tk.DISABLED)
        elif frame_num <= 0:
            self.left_button.config(state=tk.DISABLED)

    def entry_submit(self, frame_num: int):
        self.frame_num_var.set(frame_num - 1)
        self.page.update()


    def increment_frame_num(self):
        self.frame_num_var.set(min(self.frame_num_var.get() + 1, self.simulator.num_frames - 1))
        self.page.update()

    def decrement_frame_num(self):
        self.frame_num_var.set(max(0, self.frame_num_var.get() - 1))
        self.page.update()


class _FrameInfo(Subwidget, tk.LabelFrame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar, contextual: bool):
        super().__init__(master, text="Frame Information")
        self.contextual = contextual
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var
        self.configure(background='#D8E2DC')

    def update(self):
        super().update()

        frame = self.simulator.frames[self.frame_num_var.get()]

        label_offset = 0
        if self.contextual:
            context_header = ttk.Label(master=self, text=f"Context:", justify=tk.LEFT, background='#D8E2DC',
                                     font=tkfont.Font(size=14))
            context_header.grid(column=0, row=0, sticky=tk.NSEW)

            loc_label = ttk.Label(
                master=self,
                text=f"    Location: ({frame.context['location'][0]:0.2f}, {frame.context['location'][1]:0.2f})",
                justify=tk.LEFT,
                background='#D8E2DC',
                font=tkfont.Font(size=14)
            )
            loc_label.grid(column=0, row=1, sticky=tk.NSEW)
            ToolTip(
                widget=loc_label,
                text=textwrap.dedent("""
                The location of the user during this frame, arbitrary units from 0 - 10.
                Penalty exponentially decays as distance from restaurant increases
                """).strip()
            )

            time_label = ttk.Label(master=self, text=f"    Time: {frame.context['time']: 0.2f}", justify=tk.LEFT,
                                     background='#D8E2DC', font=tkfont.Font(size=14))
            time_label.grid(column=0, row=2, sticky=tk.NSEW)
            ToolTip(
                widget=time_label,
                text=textwrap.dedent("""
                The current time of the user during this frame, measured in hours since midnight (0 - 24).
                Penalty exponentially decays as distance from restaurant's peak increases
                """).strip()
            )

            label_offset = 3

        optimal_label = ttk.Label(master=self, text=f"Optimal Choice: {frame.rewards.index(max(frame.rewards))}",
                                  justify=tk.LEFT, background='#D8E2DC', font=tkfont.Font(size=14))
        optimal_label.grid(column=0, row=label_offset, sticky=tk.NSEW)
        ToolTip(widget=optimal_label, text="The optimal restaurant choice for this frame")

        choice_label = ttk.Label(master=self, text=f"Restaurant Choice: {frame.choice}", justify=tk.LEFT,
                                 background='#D8E2DC', font=tkfont.Font(size=14))
        choice_label.grid(column=0, row=label_offset + 1, sticky=tk.NSEW)
        ToolTip(widget=choice_label, text="The restaurant selected for this frame")

        reward_label = ttk.Label(master=self, text=f"    Reward: {frame.reward:0.2f}", justify=tk.LEFT,
                                 background='#D8E2DC', font=tkfont.Font(size=14))
        reward_label.grid(column=0, row=label_offset + 2, sticky=tk.NSEW)
        ToolTip(widget=reward_label, text="The reward returned from the chosen restaurant")

        optimal_reward_label = ttk.Label(master=self, text=f"    Optimal: {max(frame.rewards):0.2f}",
                                         justify=tk.LEFT, background='#D8E2DC', font=tkfont.Font(size=14))
        optimal_reward_label.grid(column=0, row=label_offset + 3, sticky=tk.NSEW)
        ToolTip(widget=optimal_reward_label, text="The maximum possible reward from all restaurants this frame")

        regret_label = ttk.Label(master=self, text=f"    Regret: {frame.regret:0.2f}", justify=tk.LEFT,
                                 background='#D8E2DC', font=tkfont.Font(size=14))
        regret_label.grid(column=0, row=label_offset + 4, sticky=tk.NSEW)
        ToolTip(widget=regret_label, text="The difference between the maximum possible reward and the reward observed")


class _Charts(Subwidget, tk.LabelFrame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master, text="Reward/Regret Charts")
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var
        self.configure(background='#D8E2DC')

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


class _RightPanel(Subwidget, tk.Frame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master)
        self.configure(background = '#D8E2DC')
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var
        self.configure(background='#D8E2DC')

    def update(self):
        output_dir = self.simulator.grapher.output_dir
        for i in range(int(self.simulator.n_arms)):
            restaurant_frame = tk.LabelFrame(master=self, text=f"Restaurant #{i}", background = '#D8E2DC')
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

            samples_label = tk.Label(restaurant_frame, text=f"Number of Samples: {len(rewards)}", background = '#D8E2DC')
            samples_label.grid(column=1, row=0)

            avg_reward = f"{np.average(rewards):0.2f}" if len(rewards) > 0 else "N/A"
            avg_label = tk.Label(restaurant_frame, text=f"Average Reward: {avg_reward}", background = '#D8E2DC')
            avg_label.grid(column=1, row=1)

            std_dev = f"{np.std(rewards):0.2f}" if len(rewards) > 0 else "N/A"
            sd_label = tk.Label(restaurant_frame, text=f"Standard Deviation: {std_dev}", background = '#D8E2DC')
            sd_label.grid(column=1, row=2)
