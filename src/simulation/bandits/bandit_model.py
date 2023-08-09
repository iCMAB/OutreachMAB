from abc import ABC, abstractmethod
from typing import List

class BanditModel(ABC):
    def __init__(self, type: str, n_arms: int):
        self.n_arms = n_arms
        self.type = type

    @abstractmethod
    def select_arm(self, context: List[float]) -> int:
        pass

    @abstractmethod
    def update(self, reward: float, regret: int, choice: int):
        pass
