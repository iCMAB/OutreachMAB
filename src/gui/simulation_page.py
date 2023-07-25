import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

import numpy as np

from .page import Page, Updatable, create_image_label


class SimulationPage(Updatable, Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frame_num_var = tk.IntVar()

        self.columnconfigure(0, weight=1)

        header = _Header(master=self, page=self)
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

        # self.formats = {
        #     "restaurant": "Selected: Restaurant {}",
        #     "reward": "Reward: {:4f}",
        #     "regret": "Regret: {:4f}",
        # }
        #
        # # Variables for labels
        # self.restaurant_string = tk.StringVar()
        # self.reward_string = tk.StringVar()
        # self.regret_string = tk.StringVar()
        #
        # label_style = ttk.Style().configure(
        #     "TLabel",
        #     font=("Times", 23),
        #     foreground="#333333",
        #     justify="left"
        # )
        #
        # selection_label = ttk.Label(self, textvariable=self.restaurant_string)
        # selection_label.place(x=60, y=90, width=300, height=40)
        #
        # reward_label = ttk.Label(self, textvariable=self.reward_string)
        # reward_label.place(x=60, y=150, width=300, height=40)
        #
        # regret_label = ttk.Label(self, textvariable=self.regret_string)
        # regret_label.place(x=60, y=210, width=300, height=40)
        #
        # next_button = ttk.Button(
        #     self,
        #     style="Nav.TButton",
        #     text="RESULTS",
        #     command=lambda: self.controller.set_page("results")
        # )
        # next_button.place(x=0, y=0, width=300, height=60)

    def open(self):
        self.app.simulator.run_simulation()
        self.update()

        # frame_num = self.iter.get()
        # frame = self.controller.simulator.frames[frame_num]
        #
        # self.iter.set(frame_num)
        # self.restaurant_string.set(self.formats["restaurant"].format(frame.choice))
        # self.reward_string.set(self.formats["reward"].format(frame.reward))
        # self.regret_string.set(self.formats["regret"].format(frame.regret))
        #
        # output_dir = self.controller.simulator.generate_frame_graphs(frame_num)
        # for i, graph in enumerate(os.listdir(output_dir)):
        #     load = Image.open(f"{output_dir}/{graph}")
        #     load = load.resize((64, 64))
        #     render = ImageTk.PhotoImage(load)
        #     img = ttk.Label(self, image=render)
        #     img.image = render
        #     img.place(x=600 - render.width(), y=i * render.height())

    def update(self):
        self.app.simulator.generate_frame_graphs(frame_num=self.frame_num_var.get())
        super().update()


class _Header(ttk.LabelFrame):
    def __init__(self, master, page: Page):
        super().__init__(master, text="TEST")
        self.page = page

        back_button = tk.Button(
            self,
            height=2,
            width=5,
            text="BACK",
            command=lambda: self.page.app.set_page("start"),
        )
        back_button.grid(column=0, row=0, sticky=tk.NW)

        title = ttk.Label(self, text="Results Page", justify=tk.CENTER)
        title.grid(column=1, row=0, sticky=tk.NSEW)
        self.columnconfigure(1, weight=1)

        end_button = tk.Button(
            self,
            height=2,
            width=5,
            text="END",
            command=lambda: self.page.app.set_page("results"),
        )
        end_button.grid(column=1, row=0, sticky=tk.NE)


class _LeftPanel(Updatable, ttk.LabelFrame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master, text="Restaurant Sampling")
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var


class _RightPanel(Updatable, ttk.PanedWindow):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master, orient=tk.VERTICAL)
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var

        header = _RightHeader(master=self, page=self.page, frame_num_var=self.frame_num_var)
        self.add(header)
        self.subwidgets.append(header)

        sample_grid = _SampleGrid(master=self, page=self.page, frame_num_var=self.frame_num_var)
        self.add(sample_grid, weight=1)
        self.subwidgets.append(sample_grid)


class _RightHeader(ttk.LabelFrame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master, text="TEST")
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var

        self.frame_num_string = tk.StringVar(value=str(self.frame_num_var.get()))

        left_button = tk.Button(
            self,
            text="PREV",
            height=2,
            width=5,
            command=self.decrement_frame_num,
        )
        left_button.grid(column=0, row=0)

        current_iter = ttk.Label(
            self,
            font=tkfont.Font(family='Times', size=32),
            foreground="#333333",
            justify="center",
            textvariable=self.frame_num_string,
        )
        current_iter.grid(column=1, row=0)

        right_button = tk.Button(
            self,
            height=2,
            width=5,
            text="NEXT",
            command=self.increment_frame_num,
        )
        right_button.grid(column=2, row=0)

    def update(self) -> None:
        self.frame_num_string.set(str(self.frame_num_var.get()))

    def increment_frame_num(self):
        self.frame_num_var.set(min(self.frame_num_var.get() + 1, self.simulator.num_frames - 1))
        self.page.update()

    def decrement_frame_num(self):
        self.frame_num_var.set(max(0, self.frame_num_var.get() - 1))
        self.page.update()


class _SampleGrid(ttk.Frame):
    def __init__(self, master, page: Page, frame_num_var: tk.IntVar):
        super().__init__(master)
        self.page = page
        self.simulator = page.app.simulator
        self.frame_num_var = frame_num_var

    def update(self):
        output_dir = self.simulator.grapher.output_dir
        for i in range(self.simulator.n_arms):
            restaurant_frame = ttk.LabelFrame(master=self, text=f"Restaurant #{i}")
            restaurant_frame.grid(column=0, row=i)

            img = create_image_label(
                master=restaurant_frame,
                image_filepath=output_dir / f"{i}_rewards.png",
                text=f"Restaurant #{i} graph placeholder",
                size=(96, 96),
            )
            img.grid(column=0, row=0, rowspan=3)

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
