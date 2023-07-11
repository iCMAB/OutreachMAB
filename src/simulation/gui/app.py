from typing import Optional

import tkinter as tk
import tkinter.font as tkFont
from src.simulation.simulator import Simulator

class App:
    rightButton = tk.Button
    currentIter = tk.Label
    leftButton = tk.Button
    def __init__(self, root):
        self.simulation = Simulator("../../config.json")
        self.simulation.run_simulation()

        root.title("Restaurant Outreach")
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

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
        self.update_labels(frame_num=0)

        right_button = tk.Button(root)
        right_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=30)
        right_button["font"] = ft
        right_button["fg"] = "#000000"
        right_button["justify"] = "center"
        right_button["text"] = ">"
        right_button.place(x=390, y=370, width=140, height=80)
        right_button["command"] = self.increaseCommand

        current_iter = tk.Label(root, textvariable=self.iter)
        ft = tkFont.Font(family='Times', size=50)
        current_iter["font"] = ft
        current_iter["fg"] = "#333333"
        current_iter["justify"] = "center"
        current_iter.place(x=230, y=370, width=131, height=65)

        left_button=tk.Button(root)
        left_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=30)
        left_button["font"] = ft
        left_button["fg"] = "#000000"
        left_button["justify"] = "center"
        left_button["text"] = "<"
        left_button.place(x=60, y=370, width=140, height=80)
        left_button["command"] = self.decreaseCommand

        selection_label = tk.Label(root, textvariable=self.restaurant_string)
        ft = tkFont.Font(family='Times', size=23)
        selection_label["font"] = ft
        selection_label["fg"] = "#333333"
        selection_label["justify"] = "left"
        selection_label.place(x=60, y=90, width=300, height=40)

        reward_label = tk.Label(root, textvariable=self.reward_string)
        ft = tkFont.Font(family='Times', size=23)
        reward_label["font"] = ft
        reward_label["fg"] = "#333333"
        reward_label["justify"] = "left"
        reward_label.place(x=60, y=150, width=300, height=40)

        regret_label = tk.Label(root, textvariable=self.regret_string)
        ft = tkFont.Font(family='Times', size=23)
        regret_label["font"] = ft
        regret_label["fg"] = "#333333"
        regret_label["justify"] = "left"
        regret_label.place(x=60, y=210, width=300, height=40)

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

        frame = self.simulation.frames[frame_num]

        self.iter.set(frame_num)
        self.restaurant_string.set(self.formats["restaurant"].format(frame.choice))
        self.reward_string.set(self.formats["reward"].format(frame.reward))
        self.regret_string.set(self.formats["regret"].format(frame.regret))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
