import sys
sys.path.append("..")
from Libraries.navigate import Navigate
from collections import deque

def shortest_path(grid, start, goal, coordinate):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == goal:
            return -1

        for direction_x, direction_y in Navigate().directions:
            next_position = Navigate().get_next_position((direction_x, direction_y), (x, y))
            nx, ny = next_position

            if Navigate().is_valid_position(grid, next_position) and grid[ny][nx] != "#" and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return coordinate

coordinates = []

#with open("example.txt") as f:
with open("input_data.txt") as f:
    raw_coordinates = f.read().splitlines()

    for coordinate in raw_coordinates:
        coordinates.append((int(coordinate.split(",")[0]), int(coordinate.split(",")[1])))

#grid_width = 6 + 1
#grid_height = 6 + 1
#place_to_stop = 12 - 1

grid_width = 70 + 1
grid_height = 70 + 1
place_to_stop = 1024 - 1

grid = [["." for _ in range(grid_width)] for _ in range(grid_height)]

for index, coordinate in enumerate(coordinates):

    grid[coordinate[1]][coordinate[0]] = "#"

    if index > place_to_stop:
        shortest_path_steps = shortest_path(grid, (0, 0), (grid_width - 1, grid_height - 1), coordinate)

        if shortest_path_steps != -1:
            print(shortest_path_steps)
            break