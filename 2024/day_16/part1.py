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

        if (x, y) == end:
            return cost
        
        if (x, y, direction) in visited:
            continue

        visited.add((x, y, direction))

        forward = Navigate().get_next_position(direction, (x, y))

        if Navigate().is_valid_position(map, forward) and Navigate().get_item_at_position(map, forward) != "#":
            heapq.heappush(queue, (cost + 1, forward[0], forward[1], direction))

        for rotation_cost in [1000, 1000]:

            clockwise_direction = Navigate().get_clockwise_direction(direction)
            heapq.heappush(queue, (cost + rotation_cost, x, y, clockwise_direction))

            counter_clockwise_direction = Navigate().get_counter_clockwise_direction(direction)
            heapq.heappush(queue, (cost + rotation_cost, x, y, counter_clockwise_direction))

    return -1

raw_map = []
map = []

with open('input_data.txt') as f:
    raw_map = f.read().splitlines()

print(get_cheapest_cost(raw_map))





