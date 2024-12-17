import sys
from collections import deque
sys.path.append("..")
from Libraries.navigate import Navigate

raw_map = []
map = []

with open('example.txt') as f:
    raw_map = f.read().splitlines()

for row in raw_map:
    map.append(list(row))

reindeer_position = Navigate().get_position_of_item(map, "S")
end_tile_postion = Navigate().get_position_of_item(map, "E")
end_scores = []

queue = deque([(reindeer_position, Navigate().right, 0)])
visited = set()

while queue:

    position, direction, cost = queue.popleft()

    print(f"Position: {position} Direction: {direction} Cost: {cost}")

    if position == end_tile_postion:
        print(f"We have reached the end with a cost of {cost}")
        end_scores.append(cost)
        print(f"End Scores: {end_scores}")
        continue

    if position in visited:
        continue

    visited.add(position)

    for dx, dy in Navigate().directions:

        next_position = Navigate().get_next_position((dx, dy), position)

        print(f"Next Position: {next_position}")

        if Navigate().get_item_at_position(map, next_position) != "#":
            cost = cost + 1 if (dx, dy) == direction else cost + 1001
            queue.append((next_position, direction, cost))
            print(f"Queue: {queue}")

print(min(end_scores))
