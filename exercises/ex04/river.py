"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        keep_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                keep_fish.append(fish)
        self.fish = keep_fish

        keep_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                keep_bears.append(bear)
        self.bears = keep_bears

        return None

    def bears_eating(self):
        i = 0
        while i < len(self.bears):
            if len(self.fish) >= 5:
                self.bears[i].hunger_score += 3
                self.remove_fish(3)
                i += 1
        return None

    def check_hunger(self):
        survive = []
        i = 0
        while i < len(self.bears):
            if self.bears[i].hunger_score >= 0:
                survive.append(self.bears[i])
            i += 1
        self.bears = survive
        return None

    def remove_fish(self, amount: int):
        i = 0
        while i < amount:
            self.fish.pop(0)
            i += 1

    def repopulate_fish(self):
        amount_new_fish = (len(self.fish) // 2) * 4
        i = 0
        while i < amount_new_fish:
            self.fish.append(Fish())
            i += 1
        return None

    def repopulate_bears(self):
        amount_new_bears = len(self.bears) // 2
        i = 0
        while i < amount_new_bears:
            self.bears.append(Bear())
            i += 1
        return None

    def view_river(self):
        day_str: int = self.day
        bears_str: int = len(self.bears)
        fish_str: int = len(self.fish)
        print(f"~~~ Day {day_str}: ~~~")
        print(f"Fish population: {fish_str}")
        print(f"Bear population: {bears_str}")
        return

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        return

    def one_river_week(self):
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
