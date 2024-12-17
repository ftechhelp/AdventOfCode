import sys
sys.path.append("..")
from Libraries.navigate import Navigate

class Robot:

    def __init__(self, starting_position: tuple[int, int]):

        self.position = starting_position
        self.movements: list[tuple[int, int]] = []
        self.movement_index: int = 0

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

            if next_item == "[" or next_item == "]":
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
        can_print = True

        if can_print:
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

        if direction == Navigate().left or direction == Navigate().right:
            other_side_of_box = Navigate().get_next_position(direction, self.robot.position, 2)
            next_position = Navigate().get_next_position(direction, self.robot.position)
            other_side_of_boxes = []

            while Navigate().get_item_at_position(self.map, other_side_of_box) == "]" or Navigate().get_item_at_position(self.map, other_side_of_box) == "[":
                other_side_of_boxes.append(other_side_of_box)
                next_position = Navigate().get_next_position(direction, other_side_of_box)
                other_side_of_box = Navigate().get_next_position(direction, other_side_of_box, 2)

            if Navigate().get_item_at_position(self.map, next_position) == "#":
                return
            
            for other_side_of_box in reversed(other_side_of_boxes):
                replace_right_x, replace_right_y = other_side_of_box
                replace_left_x, replace_left_y = Navigate().get_next_position(direction, other_side_of_box)
                empty_space_x, empty_space_y = Navigate().get_next_position(Navigate().opposite_direction(direction), other_side_of_box)

                self.map[empty_space_y][empty_space_x] = "."
                self.map[replace_right_y][replace_right_x] = "]" if direction == Navigate().left else "["
                self.map[replace_left_y][replace_left_x] = "[" if direction == Navigate().left else "]"

                next_position = (empty_space_x, empty_space_y)

            robot_x, robot_y = self.robot.position
            next_x, next_y = next_position
            self.map[next_y][next_x] = "@"
            self.map[robot_y][robot_x] = "."

            self.robot.position = next_position

        elif direction == Navigate().up or direction == Navigate().down:

            
        

raw_map = []

with open("other_example.txt") as f:
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
warehouse = WarehouseMap(map, robot)
print(robot)
warehouse.do_warehouse_work()
print(robot)
print(f"Sum of all box distances: {warehouse.calculate_box_gps_distances()}")