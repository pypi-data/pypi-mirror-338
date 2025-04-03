import unittest
from TT_probability_package.dice_module import Dice

class TestDice(unittest.TestCase):

    def test_default_dice_roll(self):
        # Create a standard 6-faced dice
        dice = Dice(faces=6, values=[1, 2, 3, 4, 5, 6], fair=True)
        
        # Roll the dice multiple times to ensure the result is within the set range
        for _ in range(1000):
            result = dice.roll()
            self.assertIn(result, range(1, 7), f"Result {result} not in expected range 1-6")

    def test_unfair_dice_roll(self):
        # Create a biased dice where face 6 has higher chances
        dice = Dice(faces=6, values=[1, 2, 3, 4, 5, 6], fair=False, chances=[1, 1, 1, 1, 1, 5])
        
        # Roll the dice multiple times to ensure that face 6 is rolled more often
        rolls = [dice.roll() for _ in range(1000)]
        count_six = rolls.count(6)
        
        # Since the chance for 6 is 5 times higher, the percentage should be around 50%
        self.assertGreater(count_six / 1000, 0.45, "Face 6 should appear more than 45% of the time")
        self.assertLess(count_six / 1000, 0.55, "Face 6 should appear less than 55% of the time")

if __name__ == "__main__":
    unittest.main()