from typing import List, Dict, Any


class Frame:
    def __init__(
            self,
            frame_num: int,
            context: Dict[str, Any],
            rewards: List[float],
            choice: int,
    ):
        self.frame_num = frame_num
        self.context = context
        self.rewards = rewards
        self.choice = choice
        self.reward = self.rewards[self.choice]
        self.regret = max(self.rewards) - self.reward
