from .bandit_model import BanditModel

class UCBBandit(BanditModel):
    def __init__(self, n_arms: int, epsilon):
        super().__init__(n_arms)
        self.type = "Upper Confidence Bound"