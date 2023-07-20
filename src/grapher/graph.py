from pathlib import Path
from tkinter import ttk

from src.simulation.simulator import Simulator
from src.utils import Pathlike


class Graph(ttk.Frame):

    def __init__(self, filepath: Pathlike, simulator: Simulator, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.filepath = Path(filepath)
        self.simulator = simulator
        self.data = None
