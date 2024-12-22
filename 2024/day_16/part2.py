import sys
import heapq
sys.path.append("..")
from Libraries.navigate import Navigate

def get_cheapest_cost(map: list):

    start = Navigate().get_position_of_item(map, "S")
    end = Navigate().get_position_of_item(map, "E")

    queue = [(0, start[0], start[1], Navigate().right, [(start[0], start[1])])] #cost, x, y, direction, path
    visited = {} # (x, y, direction): cost
    min_cost = float('inf')
    shortest_paths = []

    while queue:
        cost, x, y, direction, path = heapq.heappop(queue)

        print(f"Queue length: {len(queue)}")

        if cost > min_cost:
            continue

        if (x, y) == end:
            if cost < min_cost:
                min_cost = cost
                shortest_paths = [path]
            elif cost == min_cost:
                shortest_paths.append(path)
            continue
        
        state = (x, y, direction)
        if state in visited and visited[state] < cost:
            continue

        visited[state] = cost

        forward = Navigate().get_next_position(direction, (x, y))

        if Navigate().is_valid_position(map, forward) and Navigate().get_item_at_position(map, forward) != "#":
            new_path = path + [forward]
            heapq.heappush(queue, (cost + 1, forward[0], forward[1], direction, new_path))

        for rotation_cost in [1000, 1000]:
            clockwise_direction = Navigate().get_clockwise_direction(direction)
            heapq.heappush(queue, (cost + rotation_cost, x, y, clockwise_direction, path[:]))

            counter_clockwise_direction = Navigate().get_counter_clockwise_direction(direction)
            heapq.heappush(queue, (cost + rotation_cost, x, y, counter_clockwise_direction, path[:]))

    if not shortest_paths:
        return -1

    unique_tiles = set()
    for path in shortest_paths:
        unique_tiles.update(path)

    return len(unique_tiles)

raw_map = []
map = []

with open('example.txt') as f:
    raw_map = f.read().splitlines()

print(get_cheapest_cost(raw_map))
