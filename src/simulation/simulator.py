import json
from typing import List, Dict
from collections.abc import Mapping, MutableMapping

from .distributions import DISTRIBUTIONS
from .bandits import BANDITS, BanditModel
from .restaurant import Restaurant


class Frame:
    def __init__(
            self,
            frame_num: int,
            rewards: List[float],
            choice: int,
    ):
        self.frame_num = frame_num
        self.rewards = rewards
        self.choice = choice
        self.reward = self.rewards[self.choice]
        self.regret = max(self.rewards) - self.reward


class Simulator:
    def __init__(self, config_filepath: str, overrides: Dict[str, Dict] = None):
        with open(config_filepath, "r") as config_file:
            config: Dict[str, Dict] = json.load(config_file)
        self.config = recursive_update(config, overrides or {})

        self.num_frames = config["simulation"]["frames"]
        self.frame_num = 0
        self.frames = {}

        self.restaurants = []
        for r_config in config["restaurants"]:
            self.restaurants.append(Restaurant(
                distribution=DISTRIBUTIONS[r_config["distribution"]](**r_config["parameters"])
            ))

        self.bandit: BanditModel = BANDITS[config["bandit"]["model"]] \
            (n_arms=len(self.restaurants), **config["bandit"]["parameters"])

    def run_simulation(self):
        self.log_start()
        for i in range(self.num_frames):
            self.run_frame(i)

    def run_frame(self, index: int) -> Frame:
        self.frame_num = index

        frame = Frame(
            frame_num=index,
            rewards=[r.sample() for r in self.restaurants],
            choice=self.bandit.select_arm()
        )
        self.bandit.update(frame.reward, frame.choice)

        self.frames[index] = frame
        self.log_frame(frame)

        return frame

    def log_start(self):
        print("Starting Simulation")
        print("")
        print(f"Number of frames: {self.num_frames}")
        print(f"Bandit model: {self.bandit.type}")
        print(f"Number of arms: {self.bandit.n_arms}")

    def log_frame(self, frame: Frame):
        print("\n")
        print(f"Frame No. {frame.frame_num}")
        print(f"Restaurant Selected: {frame.choice}")
        print(f"Reward: {frame.reward}")
        print(f"Regret: {frame.regret}")

def recursive_update(d: MutableMapping, u: Mapping) -> MutableMapping:
    """
    Recursively updates dict1 with values from dict2. If a conflicting value is a Mapping, recursively updates the value
    rather than replace it. Does not add entries, only updates them.

    :param d: The original Mapping to update
    :param u: The Mapping to update value from
    :return: A reference to the d Mapping
    """
    for k, v in u.items():
        if isinstance(v, Mapping):
            d[k] = recursive_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d
