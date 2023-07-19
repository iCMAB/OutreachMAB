from .bandit_model import BanditModel
from .random import RandomBandit
from .epsilon_greedy import EpsilonGreedyBandit

BANDITS = {
    "Random": RandomBandit,
    "Epsilon Greedy": EpsilonGreedyBandit,
    "Linear TS": LinearTSBandit
}
