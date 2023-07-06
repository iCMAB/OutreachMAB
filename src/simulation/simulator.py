import json
from typing import List

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
    def __init__(self, config_filepath):
        with open(config_filepath, "r") as config_file:
            config = json.load(config_file)
        self.config = config

        self.num_frames = config["simulation"]["frames"]
        self.frame_num = 0
        self.frames = []

        self.restaurants = []
        for config in config["restaurants"]:
            distribution = DISTRIBUTIONS[config["distribution"]](**config["parameters"])
            self.restaurants.append(Restaurant(distribution=distribution))

        self.bandit: BanditModel = BANDITS[config["bandit"]["model"]](n_arms = len(self.restaurants), **config["bandit"]["parameters"])

    def run_simulation(self):
        self.log_start()
        for i in range(self.num_frames):
            self.frame_num = i
            frame = self.run_frame()
            self.frames.append(frame)
            self.log_frame(frame)

    def run_frame(self) -> Frame:
        frame = Frame(
            frame_num=self.frame_num,
            rewards=[r.sample() for r in self.restaurants],
            choice=self.bandit.select_arm()
        )
        self.bandit.get_reward(frame.reward)
        return frame


    def log_start(self):
        print("Starting Simulation")
        print("")
        print(f"Number of frames: {self.num_frames}")
        print(f"Bandit model: {self.config['bandit']['model']}")
        print(f"Number of arms: {len(self.restaurants)}")

    def log_frame(self, frame: Frame):
        print("\n")
        print(f"Frame No. {frame.frame_num}")
        print(f"")