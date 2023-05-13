from random import randint


class TDice(object):
    def __init__(self, default_eyes=1):
        self.eyes = default_eyes

    def __del__(self):
        pass

    def roll(self):
        self.eyes = randint(1, 6)
        return self.eyes
