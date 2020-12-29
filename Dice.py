import random

"""A simple Dice class. Allows us to create any number of dice
with any number of sides, and roll them."""

class Dice:

    def __init__(self, numDice, numSides):
        self.numDice = numDice
        self.numSides = numSides

    def roll(self):
        roll = 0
        for i in range(self.numDice):
            roll += random.randint(1, self.numSides)

        return roll

