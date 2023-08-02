import random

from .bandit_model import BanditModel


class RandomBandit(BanditModel):

    def __init__(self, n_arms: int, epsilon):
        super().__init__(n_arms)
        self.type = "Random"

    def select_arm(self, context) -> int:
        return random.randrange(0, self.n_arms)

    def update(self, reward: float, regret: int, choice: int):
        pass
