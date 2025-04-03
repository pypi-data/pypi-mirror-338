import random

class Dice:
    def __init__(self, n_faces=6, face_values=None, fair=True, relative_weights=None):
        """
        Initialize the Dice object.

        :param n_faces: Number of faces on the die.
        :param face_values: List of face values. If None, generates [1, 2, ..., n_faces].
        :param fair: If True, assigns equal probability to each face.
        :param relative_weights: List of weights for each face (used if fair=False).
        """
        self.n_faces = n_faces
        self.face_values = face_values if face_values is not None else list(range(1, n_faces + 1))

        if len(self.face_values) != n_faces:
            raise ValueError("The number of values must match the number of faces")

        self.relative_weights = relative_weights if relative_weights else [1] * n_faces

        if sum(self.relative_weights) == 0:
            raise ValueError("The total chances cannot be zero")

        self.chances = [1] * n_faces if fair else self.relative_weights

    def roll(self):
        """Roll the dice and return the result."""
        return random.choices(self.face_values, weights=self.chances)[0]

