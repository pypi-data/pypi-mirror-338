import unittest
from TT_probability_package.dice_module import Dice
from TT_probability_package.coin_module import Coin
from TT_probability_package.analyser_module import Analyser

class TestTracker(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.tracker = Tracker()  # Create a new Tracker instance for each test

    def test_dice_tracking(self):
        """Test that Tracker correctly tracks dice roll results."""
        dice = Dice(faces=6, tracker=self.tracker)  # Tracker is passed to Dice
        for _ in range(10):
            dice.roll()  # Roll the dice 10 times
        
        # Check that 10 results were tracked
        self.assertEqual(len(self.tracker.results), 10)
        
        # Check that all dice rolls are within the valid range of 1 to 6
        self.assertTrue(all(result in range(1, 7) for result in self.tracker.results))

    def test_coin_tracking(self):
        """Test that Tracker correctly tracks coin flip results."""
        coin = Coin(head_p=0.5, tracker=self.tracker)  # Tracker is passed to Coin
        for _ in range(10):
            coin.flip()  # Flip the coin 10 times
        
        # Check that 10 results were tracked
        self.assertEqual(len(self.tracker.results), 10)
        
        # Check that all coin flips are either 'Heads' or 'Tails'
        self.assertTrue(all(result in ['Heads', 'Tails'] for result in self.tracker.results))

    def test_combined_tracking(self):
        """Test that Tracker correctly tracks both dice and coin results."""
        dice = Dice(faces=6, tracker=self.tracker)
        coin = Coin(head_p=0.5, tracker=self.tracker)
        
        # Simulate 5 dice rolls and 5 coin flips
        for _ in range(5):
            dice.roll()
            coin.flip()

        # Check that the total number of results is 10 (5 dice + 5 coin flips)
        self.assertEqual(len(self.tracker.results), 10)
        
        # Check that all results are either dice rolls (1-6) or coin flips ('Heads', 'Tails')
        self.assertTrue(all(result in range(1, 7) or result in ['Heads', 'Tails'] for result in self.tracker.results))

    def test_contains_method(self):
        """Test that Tracker correctly identifies specific sequences in results."""
        dice = Dice(faces=1, tracker=self.tracker, values=[1])
        coin = Coin(head_p=1, tracker=self.tracker)  # Always flips 'Heads'
        
        # Simulate some rolls and flips
        dice.roll()  # Adds a dice roll of 1
        coin.flip()  # Adds a coin flip of 'Heads'
        
        # Test unordered check
        self.assertTrue(self.tracker.contains([1, 'Heads']))  # Should return True
        
        # Test ordered check (assuming flip happens after roll)
        self.assertTrue(self.tracker.contains([1, 'Heads'], ordered=True))

    def test_reset(self):
        """Test that the reset method clears the results."""
        dice = Dice(faces=6, tracker=self.tracker)
        dice.roll()  # Roll the dice once
        
        # Ensure there is one result
        self.assertEqual(len(self.tracker.results), 1)
        
        self.tracker.reset()  # Reset the tracker
        
        # Ensure the results list is empty after reset
        self.assertEqual(len(self.tracker.results), 0)

if __name__ == "__main__":
    unittest.main()