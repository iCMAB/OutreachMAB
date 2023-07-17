import random

from .bandit_model import BanditModel


class EpsilonGreedyBandit(BanditModel):
    def __init__(self, n_arms: int, epsilon: float = .1):
        super().__init__(n_arms)
        self.epsilon = epsilon
        self.counts = [n_arms]
        self.values = [n_arms]
        self.cumulative = [n_arms]
        self.max = 0
        self.max_choice = 0

        for i in range(self.n_arms - 1):
            self.counts.append(0)
            self.values.append(0)
            self.cumulative.append(0)

    def select_arm(self) -> int:
        if random.random() < self.epsilon:
            choice = random.randint(0, self.n_arms - 1)
        else:
            choice = self.max_choice
        self.counts[choice] += 1
        return choice

    def update(self, reward: float, choice: int):
        self.cumulative[choice] += reward
        avg = self.cumulative[choice]/self.counts[choice]
        self.values[choice] = avg
        if avg > self.max:
            self.max = avg
            self.max_choice = choice
