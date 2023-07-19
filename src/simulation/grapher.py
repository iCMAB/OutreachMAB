import math
import os

import matplotlib.pyplot as plt
import numpy as np

from .simulator import Simulator


# TODO: Only regenerate changed graphs


class Grapher:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_frame_graphs(self, frame_num: int, simulator: Simulator):
        self.generate_reward_histograms(frame_num, simulator)

    def generate_reward_histograms(self, frame_num: int, simulator: Simulator, full_update: bool = True):
        MIN, MAX, STEP = 0, 10, 1

        frames = simulator.frames[:frame_num + 1]
        updates = range(simulator.n_arms) if full_update else frames[-1].choice
        for i in updates:
            # Generate Basic histogram
            rewards = [frame.rewards[i] for frame in frames if i == frame.choice]
            fig, ax = plt.subplots()
            n, bins, patches = plt.hist(rewards, bins=np.arange(MIN, MAX, STEP))

            # Color the selected bar
            if i == frames[-1].choice:
                selected_bin = math.floor((rewards[-1] - MIN) / STEP)
                patches[selected_bin].set_fc("r")

            # Add labels and save to file
            plt.ylabel('Rewards')
            plt.savefig(f"{self.output_dir}/{i}_rewards")
            plt.close(fig)
