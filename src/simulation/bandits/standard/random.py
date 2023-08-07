import random

from src.simulation.bandits.bandit_model import BanditModel


class RandomBandit(BanditModel):

    def __init__(self, n_arms: int):
        super().__init__(type="Random", n_arms=n_arms)

    def select_arm(self, context) -> int:
        return random.randrange(0, self.n_arms)

    def update(self, reward: float, regret: int, choice: int):
        pass
