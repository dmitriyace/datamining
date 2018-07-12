from random import randint


class Die():
    """class which represents one die"""

    def __init__(self, num_sides=6):
        """pie has 6 facets (sides) by default"""
        self.num_sides = num_sides

    def roll(self):
        """returns random number from 1 to self.num_sides"""
        return randint(1, self.num_sides)
