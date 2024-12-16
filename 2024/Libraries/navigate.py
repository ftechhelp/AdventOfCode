class Navigate:

    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)
    directions = [left, right, up, down]

    def is_valid_position(self, map: list, position: tuple) -> bool:

        x, y = position

        return (0 <= x < len(map[0]) and 0 <= y < len(map))
        
    def get_next_position(self, direction, position) -> tuple[int, int]:

        return (position[0] + direction[0], position[1] + direction[1])
    
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
                
    def get_item_at_position(self, map: list, position: tuple) -> str:

        x, y = position

        return map[y][x]
