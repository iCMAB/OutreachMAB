import math
import os

import matplotlib.pyplot as plt
import numpy as np

from .graph import Graph

MIN, MAX, STEP = 0, 12, 1


class Histogram(Graph):
    def __init__(self, arm_index: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arm_index = arm_index
        self.chosen = False

    def cache_check(self, frames, frame_num):
        # If exact same setup as last time, cached is true
        if super().cache_check(frames, frame_num):
            return True

        # If the graph hasn't generated yet, cached is false
        if not os.path.isfile(self.filepath):
            return False

        # If this arm is chosen, cached is false
        if self.arm_index == frames[frame_num].choice:
            self.chosen = True
            return False

        # If this arm was chosen last selection, cached is false
        if self.chosen:
            self.chosen = False
            return False

        # If no reason to redraw, assume its fine
        return True

    def generate(self, frames, frame_num):
        # Return immediately if cache_check returns true
        if self.cache_check(frames, frame_num):
            return

        # Add one to include the frame num, slice stops before index otherwise
        frames = frames[:frame_num + 1]

        # Bin frame rewards by restaurant
        rewards = [frame.rewards[self.arm_index] for frame in frames if self.arm_index == frame.choice]

        fig, ax = plt.subplots()
        n, bins, patches = plt.hist(rewards, bins=np.arange(MIN, MAX, STEP))

        # Color the selected bar
        if self.arm_index == frames[frame_num].choice:
            selected_bin = math.floor((rewards[-1] - MIN) / STEP)
            patches[selected_bin].set_fc("r")
            self.chosen = True
        else:
            self.chosen = False

        # Add labels and save to file
        plt.ylabel('Rewards')
        plt.savefig(self.filepath)
        plt.close(fig)
