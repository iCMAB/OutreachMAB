from .bandit_model import BanditModel
import random

class LinearTSBandit(BanditModel):
    def __init__(self, n_arms: int):
        super().__init__(n_arms)