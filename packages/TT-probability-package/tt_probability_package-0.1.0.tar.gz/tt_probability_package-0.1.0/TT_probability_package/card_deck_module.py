import random

class CardDeck:
    def __init__(self, suits=None, ranks=None, custom_deck=None):
        if suits is None:
            suits = ['H', 'D', 'C', 'S']
        if ranks is None:
            ranks = ['2', '3', '4', '5', '6', '7',
                     '8', '9', '10', 'J', 'Q', 'K', 'A']

        self.suits = suits
        self.ranks = ranks

        if custom_deck:
            # Save the original custom deck for later reset
            self.original_custom_deck = custom_deck
            self.cards = custom_deck[:]
        else:
            self.cards = [rank + suit for suit in suits for rank in ranks]

        self.size = len(self.cards)
        self.shuffle()

    def set_custom_deck(self, custom_deck):
        """Set a custom deck using a list of strings in the format 'RankSuit'."""
        self.original_custom_deck = custom_deck  # Save the original custom deck
        self.cards = custom_deck[:]
        self.size = len(self.cards)
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw(self, n=1):
        """Draw n cards from the deck."""
        if n > self.size:
            n = self.size

        drawn_cards = [self.cards.pop() for _ in range(n)]
        self.size -= n 
        
        return drawn_cards

    def reset_deck(self):
        """Reset the deck to its custom state and shuffle."""
        if hasattr(self, 'original_custom_deck') and self.original_custom_deck:
            # Reset to the original custom deck state
            self.cards = self.original_custom_deck[:]
        else:
            # If no custom deck, reset to the standard 52-card deck
            self.cards = [rank + suit for suit in self.suits for rank in self.ranks]

        self.size = len(self.cards)  # Reset deck size
        self.shuffle()