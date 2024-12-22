import sys
sys.path.append("..")
from Libraries.navigate import Navigate
from collections import deque, Counter

class Racetrack:

    def __init__(self, grid: list):
        self.grid = grid
        self.start = Navigate().get_position_of_item(grid, "S")
        self.end = Navigate().get_position_of_item(grid, "E")
        self.shortest_path_picoseconds = self._shortest_path(self.start, self.end)
        self.shortest_paths_picoseconds_saved_with_cheat = Counter() # key: picoseconds saved, value: count
        

    def _shortest_path(self, start, goal) -> int:
        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)

        while queue:
            (x, y), steps = queue.popleft()

            if (x, y) == goal:
                return steps

            for direction_x, direction_y in Navigate().directions:
                next_position = Navigate().get_next_position((direction_x, direction_y), (x, y))
                nx, ny = next_position

                if Navigate().is_valid_position(self.grid, next_position) and grid[ny][nx] != "#" and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))

        return -1

    def faster_paths_when_cheating(self, start, goal, picoseconds_greater_than = 0) -> int:

        picoseconds_saved = 0
        faster_paths = Counter()
        wall_total_count = len([cell for row in self.grid for cell in row if cell == "#"])
        wall_count = 0

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):

                if cell == "#":
                    wall_count += 1
                    print(f"Wall Count: {wall_count}/{wall_total_count}")
                    self.grid[y][x] = "."
                    shortest_path_steps = self._shortest_path(start, goal)
                    picoseconds_saved = self.shortest_path_picoseconds - shortest_path_steps
                    #print(f"Picoseconds Saved: {picoseconds_saved}")
                    
                    if picoseconds_saved >= picoseconds_greater_than:
                        faster_paths[picoseconds_saved] += 1

                    self.grid[y][x] = "#"

        return sum(faster_paths.values())

raw_grid = []

with open("input_data.txt") as f:
    raw_grid = f.read().splitlines()

grid = [list(row) for row in raw_grid]

racetrack = Racetrack(grid)

shortest_path_steps = racetrack.shortest_path_picoseconds
print(f"Shortest Path Steps: {shortest_path_steps}")

faster_paths_when_cheating = racetrack.faster_paths_when_cheating(racetrack.start, racetrack.end, 100)
print(f"Faster Paths When Cheating: {faster_paths_when_cheating}")