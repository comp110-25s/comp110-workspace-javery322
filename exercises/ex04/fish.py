"""File to define Fish class."""

__author__: str = "730656365"


class Fish:
    age: int

    def __init__(self):
        """initiates fish with age of zero"""
        self.age: int = 0
        return None

    def one_day(self):
        """ages fish by one day"""
        self.age += 1
        return None
