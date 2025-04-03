from .coin_module import Coin
from .dice_module import Dice
from .card_deck_module import CardDeck

from setuptools import setup

setup(
    name="your_library",
    version="0.1.0",
    packages=["your_library"],
    install_requires=[
        "matplotlib",
        "numpy",
    ],
)

print("Thank you for installing TT's Probability Library")