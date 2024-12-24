import sys
import heapq
sys.path.append("..")
from Libraries.navigate import Navigate

def get_cheapest_cost(map: list):

    start = Navigate().get_position_of_item(map, "S")
    end = Navigate().get_position_of_item(map, "E")

    queue = [(0, start[0], start[1], Navigate().right)] #cost, x, y, direction
    visited = set()

    while queue:
        cost, x, y, direction = heapq.heappop(queue)

        visited.add((x, y, direction))

        if (x, y) == end:
            return cost

        forward = (cost + 1, Navigate().get_next_position(direction, (x, y)), direction)
        clockwise = (cost + 1000, (x, y), Navigate().get_clockwise_direction(direction))
        counter_clockwise = (cost + 1000, (x, y), Navigate().get_counter_clockwise_direction(direction))

        for next_cost, next_position, next_direction in [forward, clockwise, counter_clockwise]:

            if Navigate().get_item_at_position(map, next_position) == "#": continue

            if (next_position[0], next_position[1], next_direction) in visited: continue

            heapq.heappush(queue, (next_cost, next_position[0], next_position[1], next_direction))

    return -1

raw_map = []
map = []

with open('input_data.txt') as f:
    raw_map = f.read().splitlines()

print(get_cheapest_cost(raw_map))





