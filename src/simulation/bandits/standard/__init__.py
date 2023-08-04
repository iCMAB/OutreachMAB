from .epsilon_greedy import EpsilonGreedyBandit
from .random import RandomBandit
from .thompson_sampling import TSBandit
from .ucb import UCBBandit

BANDITS = {
    "Random": RandomBandit,
    "Epsilon Greedy": EpsilonGreedyBandit,
    "Thompson Sampling": TSBandit,
    "Upper Confidence Bound": UCBBandit
}
