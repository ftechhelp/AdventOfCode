class Map:

    def __init__(self, raw_map):
        self.map = raw_map
        self.right = (1, 0)
        self.left = (-1, 0)
        self.up = (0, -1)
        self.down = (0, 1)
        self.direction_going = self.up
        self.current_position = self._find_guard()
        self.last_simulation_position = self.current_position
        self.last_simulation_direction = self.direction_going
        self.simulation_positions_visited = [self.current_position]
        self.loop_obstacle_positions = []
        self.obstruction_position = None
        self.obstacle_hit_count = {}

    def _find_guard(self) -> tuple:

        for y in range(len(self.map)):

            for x in range(len(self.map[y])):

                if self.map[y][x] != "^":
                    continue
                
                return (x, y)
            
    def _get_object_in_front(self, position) -> str:
        
        position_in_front = self._get_position_in_front() if position == None else position

        if position_in_front[0] > (len(self.map[self.current_position[1]]) - 1) or position_in_front[0] < 0 or position_in_front[1] > (len(self.map) - 1) or position_in_front[1] < 0:
            print(f"Object in front: Out of Bounds!")
            return "OOB"
        
        print(f"Object in front: {self.map[position_in_front[1]][position_in_front[0]]}")
        return self.map[position_in_front[1]][position_in_front[0]]
    
    def _get_position_in_front(self):
        print(f"Position in front: {(self.current_position[0] + self.direction_going[0], self.current_position[1] + self.direction_going[1])}")
        return (self.current_position[0] + self.direction_going[0], self.current_position[1] + self.direction_going[1])
    
    def _move(self):

        if self._get_object_in_front(None) == "#":

            if self._get_position_in_front() not in self.obstacle_hit_count:
                self.obstacle_hit_count[self._get_position_in_front()] = 1
            else:
                self.obstacle_hit_count[self._get_position_in_front()] += 1
            
            self._change_direction()
        
        direction = self.direction_going
        
        self.current_position = (self.current_position[0] + direction[0], self.current_position[1] + direction[1])
        print(f"Moved to position {self.current_position}")

        self.simulation_positions_visited.append(self.current_position)

    def _add_obstruction(self):

        if self._get_object_in_front(None) == ".":
            position_in_front = self._get_position_in_front()
            self.map[position_in_front[1]][position_in_front[0]] = "#"
            self.obstruction_position = position_in_front
            print(f"Added obstruction at position {self.obstruction_position}")

    def _remove_obstruction(self):
        
        if self.obstruction_position != None:
            self.map[self.obstruction_position[1]][self.obstruction_position[0]] = "."
            self.obstruction_position = None
            print(f"Removed obstruction")

    def _reset(self):
        self.current_position = self.last_simulation_position
        self.direction_going = self.last_simulation_direction
        self.simulation_positions_visited = []
        self._remove_obstruction()
        print(f"Reset current position, direction going, position visited and removed obstruction")

    def stuck_in_loop(self):
        sus_obstacles = []

        for position in self.obstacle_hit_count:

            if self.obstacle_hit_count[position] >= 10:
                sus_obstacles.append(position)

        if len(sus_obstacles) >= 4:
            self.loop_obstacle_positions.append(self.obstruction_position)
            print("We are stuck in a loop!")
            return True

        return False
        

    def _walk(self):
        
        print("Walking...")

        while (not self.stuck_in_loop() and self._get_object_in_front(None) != "OOB"):
            self._move()


    def _change_direction(self):

        if self.direction_going == self.up:
            self.direction_going = self.right

        elif self.direction_going == self.right:
            self.direction_going = self.down
        
        elif self.direction_going == self.down:
            self.direction_going = self.left

        elif self.direction_going == self.left:
            self.direction_going = self.up

        print(f"Changed direction to {self.direction_going}")
            
    def simulate(self) -> int:

        while self._get_object_in_front(self.last_simulation_position) != "OOB":

            self._add_obstruction()
            self._walk()
            self._reset()
            self._move()

            if self._get_object_in_front(self.current_position) == "#":
                self._change_direction()
                self.last_simulation_direction = self.direction_going
            
            self.last_simulation_position = self.current_position

        return len(self.loop_obstacle_positions)

raw_map = []

with open('example.txt') as f:
    for row in f.read().splitlines():
        raw_map.append(list(row))

map = Map(raw_map)
print(map.simulate())