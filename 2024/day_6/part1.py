class Map:

    def __init__(self, raw_map):
        self.map = raw_map
        self.right = (1, 0)
        self.left = (-1, 0)
        self.up = (0, -1)
        self.down = (0, 1)
        self.direction_going = self.up
        self.current_position = self._find_guard()
        self.distinct_positions_visited = set()

    def _find_guard(self) -> tuple:

        for y in range(len(self.map)):

            for x in range(len(self.map[y])):

                if self.map[y][x] != "^":
                    continue
                
                return (x, y)
            
    def _get_object_in_front(self) -> str:
        
        position_in_front = (self.current_position[0] + self.direction_going[0], self.current_position[1] + self.direction_going[1])

        if position_in_front[0] > (len(self.map[self.current_position[1]]) - 1) or position_in_front[0] < 0 or position_in_front[1] > (len(self.map) - 1) or position_in_front[1] < 0:
            return "OOB"
                
        return self.map[position_in_front[1]][position_in_front[0]]
    
    def _move(self):
        direction = self.direction_going
        
        self.current_position = (self.current_position[0] + direction[0], self.current_position[1] + direction[1])

    def _change_direction(self):

        if self.direction_going == self.up:
            self.direction_going = self.right

        elif self.direction_going == self.right:
            self.direction_going = self.down
        
        elif self.direction_going == self.down:
            self.direction_going = self.left

        elif self.direction_going == self.left:
            self.direction_going = self.up
            
    def get_guard_distinct_positions_number(self) -> int:
        
        while (self._get_object_in_front() != "OOB"):

            if self._get_object_in_front() == "#":
                self._change_direction()

            self.distinct_positions_visited.add(self.current_position)
            self._move()

        return len(self.distinct_positions_visited) + 1


raw_map = []

with open('input_data.txt') as f:
    raw_map = f.read().splitlines()

map = Map(raw_map)
visited_number = map.get_guard_distinct_positions_number()
print(visited_number)