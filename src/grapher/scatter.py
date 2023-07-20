import matplotlib.pyplot as plt

from .graph import Graph


class Scatter(Graph):
    def __init__(self, cumulative: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cumulative = cumulative

    def generate(self, frame_num: int):
        frames = self.simulator.frames[:frame_num + 1]
        rewards = [f.reward for f in frames]
        regrets = [f.regret for f in frames]

        if self.cumulative:
            rewards = [sum(rewards[:i]) for i in range(len(frames))]
            regrets = [sum(regrets[:i]) for i in range(len(frames))]

        fig, ax = plt.subplots()
        ax.plot(rewards)
        ax.plot(regrets)

        plt.savefig(self.filepath)
        plt.close(fig)
