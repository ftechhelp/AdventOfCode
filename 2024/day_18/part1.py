import sys
sys.path.append("..")
from Libraries.navigate import Navigate

coordinates = []

with open("example.txt") as f:
    raw_coordinates = f.read().splitlines()

    for coordinate in raw_coordinates:
        coordinates.append((int(coordinate.split(",")[0]), int(coordinate.split(",")[1])))

grid_width = 6 + 1
grid_height = 6 + 1

grid = [["." for _ in range(grid_width)] for _ in range(grid_height)]

for nanosecond, coordinate in enumerate(coordinates):
    grid[coordinate[0]][coordinate[1]] = "#"

for nanosecond in range(13):
    

Navigate().print_map(grid)
