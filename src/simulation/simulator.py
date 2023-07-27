import json
from collections.abc import Mapping, MutableMapping
from typing import Dict, List

from .bandits import BANDITS, BanditModel
from .distributions import DISTRIBUTIONS
from .frame import Frame
from .grapher.grapher import Grapher
from .restaurant import Restaurant


class Simulator:
    def __init__(self, config_filepath: str, overrides: Dict[str, Dict] = None):
        with open(config_filepath, "r") as config_file:
            config: Dict[str, Dict] = json.load(config_file)
        self.config = recursive_update(config, overrides or {})

        self.n_arms: int = config["simulation"]["n_arms"]
        self.num_frames: int = config["simulation"]["frames"]
        self.frame_num: int = 0
        self.frames: List[Frame] = []
        self.grapher = Grapher(n_arms=self.n_arms, output_dir=config["graphing"]["output_dir"])

        self.restaurants: List[Restaurant] = []
        for r_config in config["restaurants"][:self.n_arms]:
            self.restaurants.append(Restaurant(
                distribution=DISTRIBUTIONS[r_config["distribution"]](**r_config["parameters"])
            ))

        self.bandit: BanditModel = BANDITS[config["bandit"]["model"]] \
            (n_arms=self.n_arms, **config["bandit"]["parameters"])

    def run_simulation(self):
        self.log_start()
        for i in range(self.num_frames):
            self.frame_num = i
            self.run_frame()

    def run_frame(self) -> Frame:
        frame = Frame(
            frame_num=self.frame_num,
            rewards=[r.sample() for r in self.restaurants],
            choice=self.bandit.select_arm()
        )
        self.bandit.update(frame.reward, frame.regret, frame.choice)

        self.frames.append(frame)
        self.log_frame(frame)

        return frame

    def generate_frame_graphs(self, frame_num: int):
        self.grapher.generate_frame_graphs(frames=self.frames[:frame_num + 1], frame_num=frame_num)
        return self.grapher.output_dir

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

    def get_rewards(self, arm_index: int) -> List[float]:
        return [frame.rewards[arm_index] for frame in self.frames if arm_index == frame.choice]

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
