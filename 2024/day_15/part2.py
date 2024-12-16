import sys
sys.path.append("..")
from Libraries.navigate import Navigate

class Robot:

    def __init__(self, starting_position: tuple[int, int]):

        self.position = starting_position
        self.movements = []
        self.movement_index = 0

    def __str__(self):
        return f"Position: {self.position}, Movement Index: {self.movement_index}, Movements Left: {[str(m) for m in self.movements[self.movement_index:]]}"

class WarehouseMap:

    def __init__(self, map: list, robot: Robot):

        self.map = map
        self.robot = robot

    def do_warehouse_work(self):

        for movement in self.robot.movements[self.robot.movement_index:]:

            next_position = Navigate().get_next_position(movement, self.robot.position)
            next_item = Navigate().get_item_at_position(self.map, next_position)

            if next_item == "#":
                self.robot.movement_index += 1
                self.print_map(movement)
                continue

            if next_item == "O":
                self.push_box(movement)
                self.robot.movement_index += 1
                self.print_map(movement)
                continue
            
            next_x, next_y = next_position
            x, y = self.robot.position
            self.map[y][x] = "."
            self.map[next_y][next_x] = "@"

            self.robot.position = next_position
            self.robot.movement_index += 1

            self.print_map(movement)

    def translate_movement(self, movement: tuple[int, int]):

        if movement == Navigate().left:
            return "<"

        if movement == Navigate().right:
            return ">"

        if movement == Navigate().up:
            return "^"

        if movement == Navigate().down:
            return "v"
        
    def print_map(self, movement: tuple[int, int]):
        print = False

        if print:
            print(f"Movement: {self.translate_movement(movement)}")
            Navigate().print_map(self.map)

    def calculate_box_gps_distances(self):

        box_distances = []

        for y, row in enumerate(self.map):

            for x, cell in enumerate(row):

                if cell == "O":
                    box_distances.append(100 * y + x)

        return sum(box_distances)


            

    def push_box(self, direction: tuple[int, int]):

        next_position = Navigate().get_next_position(direction, self.robot.position)
        box_positions = []

        while Navigate().get_item_at_position(self.map, next_position) == "O":

            box_positions.append(next_position)
            next_position = Navigate().get_next_position(direction, next_position)

        if Navigate().get_item_at_position(self.map, next_position) == "#":
            return
        
        for box_position in reversed(box_positions):
            box_x, box_y = box_position
            replace_x, replace_y = next_position

            self.map[replace_y][replace_x] = "O"
            self.map[box_y][box_x] = "."

            next_position = box_position

        robot_x, robot_y = self.robot.position
        next_x, next_y = next_position
        self.map[next_y][next_x] = "@"
        self.map[robot_y][robot_x] = "."

        self.robot.position = next_position

        

raw_map = []

with open("example.txt") as f:
    raw_map = f.read().splitlines()

is_robot_movements = False
map = []
robot = None

for row in raw_map:

    if is_robot_movements:
        movements = []
        for movement in row:
            if movement == "<":
                movements.append(Navigate().left)
            elif movement == ">":
                movements.append(Navigate().right)
            elif movement == "^":
                movements.append(Navigate().up)
            elif movement == "v":
                movements.append(Navigate().down)
        
        if robot is None:
            robot = Robot(Navigate().get_position_of_item(map, "@"))
        
        robot.movements.extend(movements)

        continue

    if row == "":
        is_robot_movements = True
        continue
    
    map_row = []
    for cell in row:
        if cell == "#":
            map_row.append("#")
            map_row.append("#")
        elif cell == ".":
            map_row.append(".")
            map_row.append(".")
        elif cell == "@":
            map_row.append("@")
            map_row.append(".")
        elif cell == "O":
            map_row.append("[")
            map_row.append("]")
    map.append(map_row)


Navigate().print_map(map)
#warehouse = WarehouseMap(map, robot)
#print(robot)
#warehouse.do_warehouse_work()
#print(robot)
#print(f"Sum of all box distances: {warehouse.calculate_box_gps_distances()}")