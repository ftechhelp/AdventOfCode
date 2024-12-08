class Map:
    def __init__(self, raw_map):
        self.original_map = [row.copy() for row in raw_map]
        self.map = [row.copy() for row in raw_map]
        self.right = (1, 0)
        self.left = (-1, 0)
        self.up = (0, -1)
        self.down = (0, 1)
        self.directions = [self.up, self.right, self.down, self.left]
        self.direction_index = 0
        self.current_position = self._find_guard()

    def _find_guard(self) -> tuple:

        for y in range(len(self.map)):

            for x in range(len(self.map[y])):

                if self.map[y][x] == '^':
                    return (x, y)

    def _is_valid_position(self, position):
        x, y = position

        return (0 <= x < len(self.map[0]) and 0 <= y < len(self.map))

    def _get_object_in_front(self, position, direction):
        next_position = (position[0] + direction[0], position[1] + direction[1])
        
        if not self._is_valid_position(next_position):
            return "OOB"
        
        return self.map[next_position[1]][next_position[0]]

    def detect_loop_positions(self):
        loop_positions = set()

        for y in range(len(self.map)):

            for x in range(len(self.map[y])):

                if (x, y) == self.current_position or self.original_map[y][x] == '#':
                    continue
                
                self.map = [row.copy() for row in self.original_map]
                self.map[y][x] = '#'

                if self._simulate_with_loop_check():
                    loop_positions.add((x, y))

        return len(loop_positions)

    def _simulate_with_loop_check(self):

        visited = set()
        position = self.current_position
        direction_index = 0

        while(True):
            current_state = (position, direction_index)
            
            if current_state in visited:
                return True
            
            visited.add(current_state)
            direction = self.directions[direction_index]

            if self._get_object_in_front(position, direction) == '#':
                direction_index = (direction_index + 1) % 4 #Go to next direction (turn right)
            else:
                position = (position[0] + direction[0], position[1] + direction[1]) # Move forward

                if not self._is_valid_position(position):
                    return False

raw_map = []

with open('input_data.txt') as f:
    for row in f.read().splitlines():
        raw_map.append(list(row))

map = Map(raw_map)
print(map.detect_loop_positions())