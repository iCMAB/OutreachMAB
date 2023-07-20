import os
from pathlib import Path

from src.simulation.simulator import Simulator
from .histogram import Histogram
from .scatter import Scatter


class Grapher:
    def __init__(self, simulator: Simulator, output_dir):
        self.output_dir = Path(output_dir)
        os.makedirs(output_dir, exist_ok=True)

        self.simulator = simulator
        self.graphs = []

        self.reward_histograms = []
        for i in range(self.simulator.n_arms):
            hist = Histogram(arm_index=i, simulator=simulator, filepath=self.output_dir / f"{i}_rewards.png")
            self.reward_histograms.append(hist)
            self.graphs.append(hist)

        self.scatter = Scatter(simulator=simulator, filepath=self.output_dir / "scatter.png", cumulative=False)
        self.graphs.append(self.scatter)

        self.cum_scatter = Scatter(simulator=simulator, filepath=self.output_dir / "cum_scatter.png", cumulative=True)
        self.graphs.append(self.cum_scatter)

    def generate_frame_graphs(self, frame_num: int):
        for graph in self.graphs:
            graph.generate(frame_num=frame_num)
