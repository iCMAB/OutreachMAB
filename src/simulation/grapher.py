import math
import os

import matplotlib.pyplot as plt
import numpy as np

from .simulator import Simulator

MIN, MAX, STEP = 0, 12, 1

# TODO: Only regenerate changed graphs


class Grapher:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_frame_graphs(self, frame_num: int, simulator: Simulator, full_update: bool = True):
        self.generate_reward_histograms(frame_num, simulator, full_update=full_update)

    def generate_reward_histograms(self, frame_num: int, simulator: Simulator, full_update: bool = True):
        if full_update:
            for i in range(simulator.n_arms):
                self.generate_reward_histogram(frame_num, i, simulator)
        else:
            choice = simulator.frames[frame_num].choice
            self.generate_reward_histogram(frame_num, choice, simulator)

            previous_choice = simulator.frames[frame_num - 1].choice
            if frame_num > 0 and choice != previous_choice:
                self.generate_reward_histogram(frame_num, previous_choice, simulator)

    def generate_reward_histogram(self, frame_num: int, arm_index: int, simulator: Simulator):
        frames = simulator.frames[:frame_num + 1]
        rewards = [frame.rewards[arm_index] for frame in frames if arm_index == frame.choice]
        fig, ax = plt.subplots()

        n, bins, patches = plt.hist(rewards, bins=np.arange(MIN, MAX, STEP))

        # Color the selected bar
        if arm_index == frames[-1].choice:
            selected_bin = math.floor((rewards[-1] - MIN) / STEP)
            patches[selected_bin].set_fc("r")

        # Add labels and save to file
        plt.ylabel('Rewards')
        plt.savefig(f"{self.output_dir}/{arm_index}_rewards")
        plt.close(fig)
