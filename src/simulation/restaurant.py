import math
from typing import Dict, Any, Tuple, Optional

from .distributions.distribution import Distribution


class Restaurant:
    def __init__(
            self,
            distribution: Distribution,
            location: Tuple[float, float],
            peak_time: float,
            context: Optional[Dict[str, float]] = None,
    ):
        self.distribution = distribution
        self.context = context
        self.location = location
        self.peak_time = peak_time

        self.history = []

    def sample(self) -> float:
        sample = self.distribution.sample()
        self.history.append(sample)
        return sample

    def sample_with_context(self, context: Dict[str, Any] = None) -> float:
        sample = self.sample()

        if self.context is None:
            return sample

        x_delta = context["location"][0] - self.location[0]
        y_delta = context["location"][1] - self.location[1]
        distance = math.pow(math.pow(x_delta, 2) + math.pow(y_delta, 2), .5)

        distance_decay_ratio = self.context["distance_decay_ratio"]
        distance_penalty_ratio = self.context["distance_penalty_ratio"]
        distance_penalty = sample * exponential_decay_penalty(distance * distance_decay_ratio)
        corrected_distance_penalty = distance_penalty * distance_penalty_ratio

        # penalty = (1 - e ^ -distance * decay_factor) * penalty_factor
        # reward = reward - penalty

        time_delta = abs(context["time"] - self.peak_time)
        time_decay_ratio = self.context["time_decay_ratio"]
        time_penalty_ratio = self.context["time_penalty_ratio"]
        time_penalty = sample * exponential_decay_penalty(time_delta * time_decay_ratio)
        corrected_time_penalty = time_penalty * time_penalty_ratio

        penalties = corrected_distance_penalty + corrected_time_penalty
        return sample - penalties


def exponential_decay_penalty(decay_factor: float):
    return 1 - math.pow(math.e, -decay_factor)
