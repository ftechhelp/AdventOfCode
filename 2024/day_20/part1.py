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

        return -1

    def picoseconds_saved_with_cheat_path_count(self, start, goal, picoseconds_greater_than = 0) -> int:

        queue = deque([(start, 0, None, set([(start, None)]))]) # position, steps, cheat_pos, visited

        while queue:
            print(f"Queue Length: {len(queue)}")

            (x, y), steps, cheat_pos, visited = queue.popleft()

            # reached goal within specified picoseconds
            if (x, y) == goal:
                self.shortest_paths_picoseconds_saved_with_cheat[self.shortest_path_picoseconds - steps] += 1
                continue
            
            #stop if not faster then fastest non cheating time or 
            if steps >= self.shortest_path_picoseconds or self.shortest_path_picoseconds - steps < picoseconds_greater_than:
                continue

            for direction_x, direction_y in Navigate().directions:
                next_position = Navigate().get_next_position((direction_x, direction_y), (x, y))
                nx, ny = next_position

                if Navigate().is_valid_position(self.grid, next_position):

                    if grid[ny][nx] != "#":
                        new_state = (next_position, cheat_pos)

                        if new_state not in visited:
                            new_visited = visited | {new_state}
                            queue.append((next_position, steps + 1, cheat_pos, new_visited))

                    elif cheat_pos is None:  
                        new_state = (next_position, next_position)
                        
                        if new_state not in visited:
                            new_visited = visited | {new_state}
                            queue.append((next_position, steps + 1, next_position, new_visited))

        return sum(self.shortest_paths_picoseconds_saved_with_cheat.values())

raw_grid = []

with open("input_data.txt") as f:
    raw_grid = f.read().splitlines()

grid = [list(row) for row in raw_grid]

racetrack = Racetrack(grid)

shortest_path_steps = racetrack.shortest_path_picoseconds
print(f"Shortest Path Steps: {shortest_path_steps}")

shortest_path_picosends_saved_with_cheat_path_count = racetrack.picoseconds_saved_with_cheat_path_count(racetrack.start, racetrack.end, 100)
print(f"Shortest Path Picoseconds Saved with Cheat Path Count: {shortest_path_picosends_saved_with_cheat_path_count}")