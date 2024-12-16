class Navigate:

    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)
    directions = [left, right, up, down]

    def is_valid_position(self, map: list, position: tuple):

        x, y = position

        return (0 <= x < len(map[0]) and 0 <= y < len(map))
        
    def get_next_position(self, direction, position):

        return (position[0] + direction[0], position[1] + direction[1])
    
    def print_map(self, map: list):
                    
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for row in map:
            for cell in row:
                print(cell, end="")
            print()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def get_string_map(self, map: list):

        return "".join("".join(row) for row in map)
