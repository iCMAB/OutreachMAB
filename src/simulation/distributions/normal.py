import random

from .distribution import Distribution


class NormalDist(Distribution):
    def __init__(self, mean: float, sd: float):
        self.mean = mean
        self.sd = sd

    def sample(self) -> float:
        return random.normalvariate(self.mean, self.sd)
