"""simulates river life cycle"""

from exercises.ex04.river import River

__author__: str = "730656365"
my_river: River = River(num_fish=10, num_bears=2)
my_river.view_river()
my_river.one_river_week()
