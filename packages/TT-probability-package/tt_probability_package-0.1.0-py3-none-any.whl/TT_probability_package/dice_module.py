import random

class Dice:
    def __init__(self, faces=6, values=[1, 2, 3, 4, 5, 6], fair=True, chances=[1, 1, 1, 1, 1, 1]):
        if len(values) != faces:
            raise ValueError(
                "The number of values must match the number of faces")

        self.faces = faces
        self.values = values
        self.chances = chances

        if sum(chances) == 0:
            raise ValueError("The total chances cannot be zero")

        self.chances_sum = sum(chances)

        if fair:
            self.chances = [1] * faces

    def roll(self):
        """Roll the dice and return the result."""
        result = random.choices(self.values, weights=self.chances)[0]
        return result
