from typing import List


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
