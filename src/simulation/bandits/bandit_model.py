from abc import ABC, abstractmethod


class BanditModel(ABC):
    def __init__(self, n_arms):
        self.n_arms = n_arms

    @abstractmethod
    def select_arm(self) -> int:
        pass

    @abstractmethod
    def get_reward(self, reward: float):
        pass
