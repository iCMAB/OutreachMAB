from .bandit_model import BanditModel
from .contextual import BANDITS as CONTEXTUAL_BANDITS
from .contextual import LinearUCB
from .standard import BANDITS as STANDARD_BANDITS
from .standard import EpsilonGreedyBandit, RandomBandit, TSBandit, UCBBandit

BANDITS = STANDARD_BANDITS | CONTEXTUAL_BANDITS
