import os
from pathlib import Path
from typing import List

from .histogram import Histogram
from .scatter import Scatter, ScatterType
from ..frame import Frame


class Grapher:
    def __init__(self, n_arms, output_dir):
        self.output_dir = Path(output_dir)
        for file in os.listdir(output_dir):
            os.remove(f"{output_dir}/{file}")
        os.makedirs(output_dir, exist_ok=True)

        self.graphs = []

        for i in range(n_arms):
            hist = Histogram(filepath=self.output_dir / f"{i}_rewards.png", arm_index=i)
            self.graphs.append(hist)

        scatter = Scatter(filepath=self.output_dir / "avg_scatter.png", plot_type=ScatterType.AVERAGE)
        self.graphs.append(scatter)

        cum_scatter = Scatter(filepath=self.output_dir / "cum_scatter.png", plot_type=ScatterType.CUMULATIVE)
        self.graphs.append(cum_scatter)

    def generate_frame_graphs(self, frames: List[Frame], frame_num: int):
        for graph in self.graphs:
            graph.generate(frames=frames, frame_num=frame_num)
