import random

from .bandit_model import BanditModel


class RandomBandit(BanditModel):
    def select_arm(self) -> int:
        return random.randrange(0, self.n_arms)

    def get_reward(self, reward: float):
        pass
