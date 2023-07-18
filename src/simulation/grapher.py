import os
from typing import List

import matplotlib.pyplot as plt

from .frame import Frame


class Grapher:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def plots_from_frames(self, n_arms: int, frames: List[Frame]):
        restaurant_rewards = []
        for i in range(n_arms):
            restaurant_rewards.append([frame.rewards[i] for frame in frames])
        self.generate_reward_histograms(restaurant_rewards)

    def generate_reward_histograms(self, restaurant_rewards: List[List[float]]):
        for i, rewards in enumerate(restaurant_rewards):
            fig, ax = plt.subplots()
            plt.hist(rewards)
            plt.ylabel('Rewards')
            plt.savefig(f"{self.output_dir}/{i}_rewards")
            plt.close(fig)
