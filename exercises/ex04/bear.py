"""File to define Bear class."""

__author__ = "730656365"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        """initiates bear with 0 age and 0 hunger score"""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """ages bera by 1 and reduces hunger score by 1"""
        self.age += 1
        self.hunger_score += -1
        return None

    def eat(self, num_fish: int):
        """increases hunger score by fish eaten"""
        self.hunger_score += num_fish
        return None
