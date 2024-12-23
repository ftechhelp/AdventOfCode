import sys
sys.path.append("..")
from Libraries.navigate import Navigate
import heapq

class Keypad:

    def __init__(self, type: str, entity_name: str, directions: list[tuple] = Navigate().directions):

        if type == "numeric":
            self.keypad = [
                ["7", "8", "9"],
                ["4", "5", "6"],
                ["1", "2", "3"],
                [None, "0", "A"]
            ]
            self.position = (2, 3)

        elif type == "directional":
            self.keypad = [
                [None, "^", "A"],
                ["<", "v", ">"]
            ]
            self.position = (2, 0)

        self.entity_name = entity_name
        self.directions = directions

    def _go_to(self, key: str) -> list[str]:
        
        shortest_path_directions = self._get_shortest_path_directions(key)

        shortest_path_visuals = []

        for direction in shortest_path_directions:
            
            if direction == Navigate().right:
                shortest_path_visuals.append(">")
            
            elif direction == Navigate().left:
                shortest_path_visuals.append("<")
            
            elif direction == Navigate().up:
                shortest_path_visuals.append("^")
            
            elif direction == Navigate().down:
                shortest_path_visuals.append("v")

        shortest_path_visuals += ["A"]

        #print(f"{self.entity_name} goes to {key} by hitting {shortest_path_visuals}")

        return shortest_path_visuals

    def _get_shortest_path_directions(self, end: str) -> list[tuple]:

        queue = [(0, self.position, [])]
        visited = set()

        while queue:
            cost, position, directions = heapq.heappop(queue)

            if not Navigate().is_valid_position(self.keypad, position):
                continue

            if self.keypad[position[1]][position[0]] == None:
                continue

            if position in visited:
                continue

            visited.add(position)

            if self.keypad[position[1]][position[0]] == end:
                self.position = position
                return directions

            for direction in self.directions:
                new_position = Navigate().get_next_position(direction, position)

                if new_position not in visited:
                    heapq.heappush(queue, (cost + 1, new_position, directions + [direction]))

    def type_in(self, combination: str):

        all_directions_needed = []

        for key in combination:
            shortest_path = self._go_to(key)
            all_directions_needed.extend(shortest_path)

        return all_directions_needed

numeric_keypad = Keypad("numeric", "Numeric Keypad Robot")
robot1_directional_keypad = Keypad("directional", "Robot 1", [Navigate().down, Navigate().left, Navigate().right, Navigate().up])
robot2_directional_keypad = Keypad("directional", "Robot 2", [Navigate().left, Navigate().down, Navigate().right, Navigate().up])
my_directional_keypad = Keypad("directional", "Me")

robot1_input = numeric_keypad.type_in("029A")
print(f"\nRobot 1 sequence: {''.join(robot1_input)} with length {len(robot1_input)}")

robot2_input = robot1_directional_keypad.type_in(robot1_input)
print(f"Robot 2 sequence: {''.join(robot2_input)} with length {len(robot2_input)}")

my_input = robot2_directional_keypad.type_in(robot2_input)
print(f"Final sequence: {''.join(my_input)} with length {len(my_input)}")