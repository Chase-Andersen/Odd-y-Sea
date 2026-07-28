import random


class FateDie:
    def __init__(self):
        self.last_roll = None

    def roll(self):
        self.last_roll = random.randint(1, 6)
        return self.last_roll