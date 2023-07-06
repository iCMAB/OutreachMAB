from distributions.distribution import Distribution

class Restaurant:
    def __init__(self, distribution: Distribution):
        self.distribution = distribution
        self.history = []

    def sample(self) -> float:
        sample = self.distribution.sample()
        self.history.append(sample)
        return sample
