import sys
import heapq
sys.path.append("..")
from Libraries.navigate import Navigate

def get_cheapest_cost(map: list):

    start = Navigate().get_position_of_item(map, "S")
    end = Navigate().get_position_of_item(map, "E")

    queue = [(0, start[0], start[1], Navigate().right, [])] #cost, x, y, direction, tiles
    best_cost = float('inf')
    best_tiles = set()
    visited = {}

    while queue:
        cost, x, y, direction, tiles = heapq.heappop(queue)

        tile_position_direction = (x, y, direction)

        if tile_position_direction in visited and visited[tile_position_direction] < cost:
            continue

        visited[tile_position_direction] = cost

        #print(f"Queue Length: {len(queue)}")

        if cost > best_cost:
            continue

        tiles.append((x, y))

        if (x, y) == end:
            print(f"Found End")
            if cost < best_cost:
                best_cost = cost
                best_tiles = set(tiles)
                print(f"New Best Cost: {best_cost}")
            elif cost == best_cost:
                best_tiles.update(tiles)
                print(f"Same Cost, New Best Tile: {best_tiles}")
            continue


        forward = Navigate().get_next_position(direction, (x, y))

        if Navigate().is_valid_position(map, forward) and Navigate().get_item_at_position(map, forward) != "#":
            heapq.heappush(queue, (cost + 1, forward[0], forward[1], direction, tiles.copy()))

        for rotation_cost in [1000, 1000]:

            clockwise_direction = Navigate().get_clockwise_direction(direction)
            heapq.heappush(queue, (cost + rotation_cost, x, y, clockwise_direction, tiles.copy()))

            counter_clockwise_direction = Navigate().get_counter_clockwise_direction(direction)
            heapq.heappush(queue, (cost + rotation_cost, x, y, counter_clockwise_direction, tiles.copy()))

    return len(best_tiles)

raw_map = []
map = []

with open('input_data.txt') as f:
    raw_map = f.read().splitlines()

print(get_cheapest_cost(raw_map))





