import sys
sys.path.append("..")
from Libraries.navigate import Navigate
from collections import deque, Counter
import heapq

class Racetrack:

    def __init__(self, grid: list):
        self.grid = grid
        self.start = Navigate().get_position_of_item(grid, "S")
        self.end = Navigate().get_position_of_item(grid, "E")
        self.shortest_path_picoseconds = self._shortest_path_part1(self.start, self.end)
        self.shortest_paths_picoseconds_saved_with_cheat = Counter() # key: picoseconds saved, value: count

    def _shortest_path_part1(self, start, goal) -> int:
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

    def _shortest_path(self, start, goal) -> int:
        queue = [(start, 0, Navigate().up, 2, False)]
        tiles_over_shortest_path = {}

        while queue:

            print(f"Queue size: {len(queue)}")

            (x, y), steps, direction, hack_picoseconds, cheat_started = heapq.heappop(queue)

            if (x, y, direction) not in tiles_over_shortest_path:
                tiles_over_shortest_path[(x, y, direction)] = steps
            elif tiles_over_shortest_path[(x, y, direction)] >= self.shortest_path_picoseconds:
                continue

            picoseconds_saved = self.shortest_path_picoseconds - steps

            if picoseconds_saved < 100:
                continue

            if (x, y) == goal:
                picoseconds_saved = self.shortest_path_picoseconds - steps
                self.shortest_paths_picoseconds_saved_with_cheat[picoseconds_saved] += 1
                continue

            for direction_x, direction_y in Navigate().directions:
                next_position = Navigate().get_next_position((direction_x, direction_y), (x, y))
                nx, ny = next_position

                if Navigate().is_valid_position(self.grid, next_position) and self.grid[ny][nx] == "#":
                    if not cheat_started:
                        cheat_started = True

                if cheat_started and hack_picoseconds > 0:
                    queue.append((next_position, steps + 1, (direction_x, direction_y), hack_picoseconds - 1, cheat_started))
                    continue

                if Navigate().is_valid_position(self.grid, next_position) and self.grid[ny][nx] != "#" and (nx, ny):
                    queue.append((next_position, steps + 1, (direction_x, direction_y), hack_picoseconds, cheat_started))

        return -1

    def faster_paths_when_cheating(self, start, goal, picoseconds_greater_than = 0) -> int:

        self._shortest_path(start, goal)

        return sum(self.shortest_paths_picoseconds_saved_with_cheat.values())

raw_grid = []

with open("input_data.txt") as f:
    raw_grid = f.read().splitlines()

grid = [list(row) for row in raw_grid]

racetrack = Racetrack(grid)

shortest_path_steps = racetrack.shortest_path_picoseconds
print(f"Shortest Path Steps: {shortest_path_steps}")

faster_paths_when_cheating = racetrack.faster_paths_when_cheating(racetrack.start, racetrack.end, 100)
print(f"Faster Paths When Cheating: {faster_paths_when_cheating}")