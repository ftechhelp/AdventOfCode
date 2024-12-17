import sys
from collections import deque
sys.path.append("..")
from Libraries.navigate import Navigate

class Reindeer:

    def __init__(self, map: list):

        self.map = map
        self.position = Navigate().get_position_of_item(map, "S")
        self.direction_facing = Navigate().right

    def turn_90_degrees(self):
        direction_index = (Navigate().directions.index(self.direction_facing) + 1) % 4
        self.direction_facing = Navigate().directions[direction_index]

    def move(self, position: tuple):
        Navigate().swap_positions(self.map, self.position, position)
        self.position = position

class ReindeerMazeMap:

    def __init__(self, map: list):

        self.reindeer = Reindeer(map)
        self.end_tile = Navigate().get_position_of_item(map, "E")
        self.lowest_score = 0

    def get_lowest_score(self):

        visited = set()
        start_position = self.reindeer.position
        self.lowest_score = self.walk()
    
    def walk(self) -> int:
        pass


raw_map = []
map = []

with open('example.txt') as f:
    raw_map = f.read().splitlines()

for row in raw_map:
    map.append(list(row))

Navigate().print_map(map)

