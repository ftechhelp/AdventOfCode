import sys
import heapq
sys.path.append("..")
from Libraries.navigate import Navigate

def get_cheapest_cost(map: list):

    start = Navigate().get_position_of_item(map, "S")
    end = Navigate().get_position_of_item(map, "E")

    queue = [(0, start[0], start[1], Navigate().right, [(start[0], start[1])])] #cost, x, y, direction, path
    best_tile_cost = {}
    lowest_cost = float("inf")
    best_path_tiles = set()

    while queue:

        print(f"Queue size: {len(queue)}")

        cost, x, y, direction, path = heapq.heappop(queue)

        if cost > lowest_cost:
            continue

        if (x, y, direction) not in best_tile_cost:
            best_tile_cost[(x, y, direction)] = cost
        elif cost > best_tile_cost[(x, y, direction)]:
            continue

        if (x, y) == end:
            if cost < lowest_cost:
                lowest_cost = cost
                best_path_tiles = set(path)
                continue
            elif cost == lowest_cost:
                best_path_tiles.update(path)
                continue

        forward = (cost + 1, Navigate().get_next_position(direction, (x, y)), direction)
        clockwise = (cost + 1000, (x, y), Navigate().get_clockwise_direction(direction))
        counter_clockwise = (cost + 1000, (x, y), Navigate().get_counter_clockwise_direction(direction))

        for next_cost, next_position, next_direction in [forward, clockwise, counter_clockwise]:

            if Navigate().get_item_at_position(map, next_position) == "#": continue

            heapq.heappush(queue, (next_cost, next_position[0], next_position[1], next_direction, path + [(next_position[0], next_position[1])]))

    return len(best_path_tiles)

raw_map = []
map = []

with open('input_data.txt') as f:
    raw_map = f.read().splitlines()

print(get_cheapest_cost(raw_map))





