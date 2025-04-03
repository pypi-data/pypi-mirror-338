import random

class Coin:
    def __init__(self, head_p=0.5):
        self.head_p = head_p

    def flip(self):
        """Flip the coin and return 'Heads' or 'Tails'."""
        result = 'H' if random.random() <= self.head_p else 'T'

        return result
