import os
from pathlib import Path

from src.simulation.simulator import Simulator
from .histogram import Histogram


class Grapher:
    def __init__(self, simulator: Simulator, output_dir):
        self.output_dir = Path(output_dir)
        os.makedirs(output_dir, exist_ok=True)

        self.simulator = simulator
        self.reward_histograms = []
        for i in range(self.simulator.n_arms):
            hist = Histogram(arm_index=i, simulator=simulator, filepath=self.output_dir / f"{i}_rewards.png")
            self.reward_histograms.append(hist)

    def generate_frame_graphs(self, frame_num: int):
        for hist in self.reward_histograms:
            hist.generate(frame_num=frame_num)
