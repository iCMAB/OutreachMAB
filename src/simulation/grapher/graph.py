from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from src.simulation.frame import Frame
from src.utils import Pathlike


class Graph(ABC):
    def __init__(self, filepath: Pathlike, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.filepath = Path(filepath)
        self.cache = None

    @abstractmethod
    def generate(self, frames: List[Frame], frame_num: int):
        ...

    def cache_check(self, frames: List[Frame], frame_num: int) -> bool:
        if (frames, frame_num) == self.cache:
            return True
        else:
            self.cache = (frames, frame_num)
            return False
