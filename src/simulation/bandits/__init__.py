from .bandit_model import BanditModel
from .random import RandomBandit
from .epsilon_greedy import EpsilonGreedyBandit
from .thompson_sampling import TSBandit

BANDITS = {
    "Random": RandomBandit,
    "Epsilon Greedy": EpsilonGreedyBandit,
    "Thompson Sampling": TSBandit
}
