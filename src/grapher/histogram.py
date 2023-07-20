import math

import matplotlib.pyplot as plt
import numpy as np

from .graph import Graph

MIN, MAX, STEP = 0, 12, 1


class Histogram(Graph):
    def __init__(self, arm_index: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arm_index = arm_index
        self.cached = None

    def generate(self, frame_num):
        frames = self.simulator.frames[:frame_num + 1]
        rewards = [frame.rewards[self.arm_index] for frame in frames if self.arm_index == frame.choice]

        if rewards == self.cached:
            return
        else:
            self.cached = rewards

        fig, ax = plt.subplots()
        n, bins, patches = plt.hist(rewards, bins=np.arange(MIN, MAX, STEP))

        # Color the selected bar
        if self.arm_index == frames[frame_num].choice:
            selected_bin = math.floor((rewards[-1] - MIN) / STEP)
            patches[selected_bin].set_fc("r")

        # Add labels and save to file
        plt.ylabel('Rewards')
        plt.savefig(self.filepath)
        plt.close(fig)
