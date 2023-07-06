

class Restaurant:
    def __init__(self, distribution):
        self.distribution = distribution
        self.history = []

    def sample(self) -> float:
        sample = self.distribution.sample()
        self.history.append(sample)
        return sample
