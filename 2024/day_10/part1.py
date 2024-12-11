class TopographicMap:

    def __init__(self, raw_map):

        up = (0, -1)
        down = (0, 1)
        left = (-1, 0)
        right = (1, 0)
        self.directions = [up, down, left, right]
        self.map = raw_map

    def _is_valid_position(self, position):

        x, y = position

        return (0 <= x < len(self.map[0]) and 0 <= y < len(self.map))
    
    def find_trail_score(self, start_position) -> int:
        visited_9s = set()
        self._navigate_trail(start_position, visited_9s)

        return len(visited_9s)

    def _navigate_trail(self, position: tuple, visited_9s: set):

        x, y = position
        current_height = int(self.map[position[1]][position[0]])

        if current_height == 9:
            visited_9s.add(position)
        
        for dx, dy in self.directions:
            next_position = (x + dx, y + dy)

            if not self._is_valid_position(next_position):
                continue
            
            nx, ny = next_position
            next_position_height = int(self.map[ny][nx])

            if next_position_height - current_height == 1:
                self._navigate_trail(next_position, visited_9s)

raw_map = []

with open('input_data.txt') as f:
    raw_map = f.read().splitlines()

map = TopographicMap(raw_map)
trailhead_count = 0
trailhead_scores = []
total_score = 0
score = 0

for y, row in enumerate(raw_map):

    for x in range(len(row)):

        if raw_map[y][x] == "0":
            trailhead_count += 1
            #print(f"Found trail {trailhead_count} head at {(x, y)}")
            trailhead_score = map.find_trail_score((x, y))
            trailhead_scores.append(trailhead_score)
            total_score += trailhead_score


print(f"Total Trailhead Score: {total_score}")