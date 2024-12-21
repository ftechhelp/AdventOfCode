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
        

    def _shortest_path(self, start, goal):
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

        return -1  # return -1 if no path is found

    def picoseconds_saved_with_cheat(self, start, goal):
        queue = deque([(start, 0, False, set((start, False)))])

        while queue:

            print(f"Queue Length: {len(queue)}")

            (x, y), steps, cheat_used, visited = queue.popleft()

            if steps >= self.shortest_path_picoseconds:
                continue

            if (x, y) == goal:
                self.shortest_paths_picoseconds_saved_with_cheat[self.shortest_path_picoseconds - steps] += 1
                continue

            for direction_x, direction_y in Navigate().directions:
                next_position = Navigate().get_next_position((direction_x, direction_y), (x, y))
                nx, ny = next_position

                if Navigate().is_valid_position(grid, next_position) and (next_position, cheat_used) not in visited:

                    if grid[ny][nx] != "#":
                        visited.add((next_position, cheat_used))
                        queue.append((next_position, steps + 1, cheat_used, visited))

                    elif not cheat_used:
                        visited.add((next_position, True))
                        queue.append((next_position, steps + 1, True, visited))

raw_grid = []

with open("example.txt") as f:
    raw_grid = f.read().splitlines()

grid = [list(row) for row in raw_grid]

racetrack = Racetrack(grid)

shortest_path_steps = racetrack.shortest_path_picoseconds
print(f"Shortest Path Steps: {shortest_path_steps}")

racetrack.picoseconds_saved_with_cheat(racetrack.start, racetrack.end)
print(f"Shortest Path Picoseconds Saved: {racetrack.shortest_paths_picoseconds_saved_with_cheat}")