from .bandit_model import BanditModel
import random
import math
import numpy as np
class UCBBandit(BanditModel):
    def __init__(self, n_arms: int, epsilon: float = 1):
        super().__init__(n_arms)
        self.type = "Upper Confidence Bound"
        self.exploration = epsilon #not actually considered epsilon, but epsilon is keyword that BanditModel takes
        self.sums = [0] * n_arms
        self.iter = 0
        self.count = [0] * n_arms
        self.log_hist = []

    def select_arm(self) -> int:
        UCB_Values = [0] * self.n_arms

        for i in range(0, self.n_arms):
            if self.count[i] > 0:
                ln_iter = math.log(self.iter)
                self.log_hist.append(ln_iter)

                #Calculate UCB
                avg = self.sums[i]/self.count[i]
                ucb_value = avg + self.exploration*(ln_iter/self.count[i])
                UCB_Values[i] = ucb_value

            elif (self.count[i] == 0):
                UCB_Values[i] = 5000000000 #so large it will always be selected

        bandit = np.argmax(UCB_Values)
        return bandit

    def update(self, reward: float, regret: int, choice: int):
        self.iter += 1
        self.count[choice] += 1
        self.sums[choice] += reward