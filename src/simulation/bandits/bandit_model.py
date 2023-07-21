from abc import ABC, abstractmethod


class BanditModel(ABC):
    def __init__(self, n_arms: int):
        self.n_arms = n_arms

    @abstractmethod
    def select_arm(self) -> int:
        pass

    @abstractmethod
    def update(self, reward: float, regret: int, choice: int):
        pass
