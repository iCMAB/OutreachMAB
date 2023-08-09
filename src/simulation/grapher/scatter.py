from enum import Enum

import matplotlib.pyplot as plt

from .graph import Graph


class ScatterType(Enum):
    STANDARD = 0
    CUMULATIVE = 1
    AVERAGE = 2

class Scatter(Graph):
    def __init__(self, plot_type: ScatterType, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = plot_type

    def generate(self, frames, frame_num):
        super().generate(frames, frame_num)

        frames = frames[:frame_num + 1]
        rewards = [f.reward for f in frames]
        regrets = [f.regret for f in frames]

        if self.type == ScatterType.CUMULATIVE:
            rewards = [sum(rewards[:i]) for i in range(len(frames))]
            regrets = [sum(regrets[:i]) for i in range(len(frames))]
        elif self.type == ScatterType.AVERAGE:
            rewards = [sum(rewards[:i]) / (i + 1) for i in range(len(frames))]
            regrets = [sum(regrets[:i]) / (i + 1) for i in range(len(frames))]

        ratio = .3
        plt.rcParams['figure.figsize'] = (8, 8 * ratio)
        fig, ax = plt.subplots()
        ax.plot(rewards)
        ax.plot(regrets)

        x_left, x_right = ax.get_xlim()
        y_low, y_high = ax.get_ylim()
        ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)

        plt.tight_layout()
        plt.savefig(self.filepath)
        plt.close(fig)
