class Navigate:

    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)
    directions = [left, right, up, down]

    def is_valid_position(self, map: list, position: tuple) -> bool:

        x, y = position

        return (0 <= x < len(map[0]) and 0 <= y < len(map))
        
    def get_next_position(self, direction: tuple, position: tuple, number_of_moves: int = 1) -> tuple[int, int]:

        x, y = position
        direction_x, direction_y = direction

        return (x + direction_x * number_of_moves, y + direction_y * number_of_moves)
    
    def opposite_direction(self, direction: tuple) -> tuple:

        return (-direction[0], -direction[1])

    def print_map(self, map: list) -> None:
                    
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for row in map:
            for cell in row:
                print(cell, end="")
            print()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def get_string_map(self, map: list) -> str:

        return "".join("".join(row) for row in map)
    
    def get_position_of_item(self, map: list, item: str) -> tuple[int, int]:
        
        for y, row in enumerate(map):

            for x, cell in enumerate(row):

                if cell == item:
                    return (x, y)
                
    def swap_positions(self, map: list, position1: tuple, position2: tuple) -> None:

        x1, y1 = position1
        item_at_position_1 = map[y1][x1]
        x2, y2 = position2
        item_at_position_2 = map[y2][x2]


        map[y1][x1] = item_at_position_2
        map[y2][x2] = item_at_position_1
                
    def get_item_at_position(self, map: list, position: tuple) -> str:

        x, y = position

        return map[y][x]

