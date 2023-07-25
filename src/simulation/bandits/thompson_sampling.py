from .bandit_model import BanditModel
import random
import numpy as np

class TSBandit(BanditModel):
    #Very simple Thompson Sampling, takes Regret as a Bernoulli distribution, there either is or is not regret
    def __init__(self, n_arms: int, epsilon):
        super().__init__(n_arms)
        self.max_rewards = [0] * self.n_arms
        self.regrets = [0] * self.n_arms
        self.type = "Thompson Sampling"
    def select_arm(self) -> int:
        bandit = 0
        beta_max = 0

        for i in range(0, self.n_arms):
            beta_d = random.betavariate(self.max_rewards[i] + 1, self.regrets[i] + 1)
            if beta_d > beta_max:
                beta_max = beta_d
                bandit = i

        return bandit

    def update(self, reward: float, regret: int, choice: int):
        if regret > 0:
            self.regrets[choice] += 1
        else:
            self.max_rewards[choice] += 1