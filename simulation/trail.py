from mesa import Agent
import numpy as np

class Trail(Agent):
    # this is trail marker

    def __init__(self, pos, model, origin, agent):

        super().__init__(pos, model)
        # print(pos)
        self.x, self.y = pos
        self.origin = origin
        self.agent = agent
