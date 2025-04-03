import unittest
from TT_probability_package.coin_module import Coin

class TestCoin(unittest.TestCase):
    
    def test_coin_flip(self):
        """Test that a coin flip result is either 'Heads' or 'Tails'."""
        coin = Coin()
        result = coin.flip()
        self.assertIn(result, ["H", "T"])

    def test_biased_coin(self):
        """Test that a biased coin flip gives a high probability of heads when head_p = 0.9."""
        biased_coin = Coin(head_p=0.9)
        flips = [biased_coin.flip() for _ in range(1000)]
        head_count = sum(1 for flip in flips if flip == "H")
        self.assertGreater(head_count / 1000, 0.85)  # Expect more than 85% heads
    
    def test_unbiased_coin(self):
        """Test that an unbiased coin flip gives approximately 50% heads."""
        unbiased_coin = Coin(head_p=0.5)
        flips = [unbiased_coin.flip() for _ in range(1000)]
        head_count = sum(1 for flip in flips if flip == "H")
        self.assertLess(abs(head_count / 1000 - 0.5), 0.05)  # Expect ~50% heads within a tolerance of 5%

    def test_edge_case_head_p_zero(self):
        """Test the edge case where head_p = 0, expecting all 'Tails'."""
        biased_coin = Coin(head_p=0.0)
        flips = [biased_coin.flip() for _ in range(1000)]
        tail_count = sum(1 for flip in flips if flip == "T")
        self.assertGreater(tail_count / 1000, 0.95)  # Expect more than 95% tails

    def test_edge_case_head_p_one(self):
        """Test the edge case where head_p = 1, expecting all 'Heads'."""
        biased_coin = Coin(head_p=1.0)
        flips = [biased_coin.flip() for _ in range(1000)]
        head_count = sum(1 for flip in flips if flip == "H")
        self.assertGreater(head_count / 1000, 0.95)  # Expect more than 95% heads

if __name__ == "__main__":
    unittest.main()