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