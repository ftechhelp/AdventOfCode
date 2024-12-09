class Map:

    def __init__(self, antenna_map):
        self.antenna_map = antenna_map
        self.antennas = self._find_antennas()

    def _find_antennas(self) -> dict:
        antennas = {}

        for y, row in enumerate(self.antenna_map):

            for x, char in enumerate(row):

                if char != '.':

                    if char not in antennas:
                        antennas[char] = []
                    
                    antennas[char].append((x, y))

        return antennas
    
    def find_antinodes(self):
        antinodes = set()

        for frequency, positions in self.antennas.items():

            print(f"Frequency: {frequency}: {positions}")

            for p_index in range(len(positions)):

                for other_p_index in range(p_index + 1, len(positions)):
                    x1, y1 = positions[p_index]
                    x2, y2 = positions[other_p_index]

                    antinodes.add((x1, y1))
                    antinodes.add((x2, y2))

                    dx = x2 - x1
                    dy = y2 - y1

                    print(f"Position difference: {dx}, {dy} between {frequency} {positions[p_index]} and {frequency} {positions[other_p_index]}")

                    antinode1_x = x1 + (dx * -1)
                    antinode1_y = y1 + (dy * -1)

                    while (0 <= antinode1_x < len(self.antenna_map[0]) and 0 <= antinode1_y < len(self.antenna_map)):
                        antinodes.add((antinode1_x, antinode1_y))
                        print(f"Added antinode 1: {antinode1_x}, {antinode1_y}")
                        antinode1_x += (dx * -1)
                        antinode1_y += (dy * -1)

                    antinode2_x = x2 + dx
                    antinode2_y = y2 + dy

                    while (0 <= antinode2_x < len(self.antenna_map[0]) and 0 <= antinode2_y < len(self.antenna_map)):
                        antinodes.add((antinode2_x, antinode2_y))
                        print(f"Added antinode 2: {antinode2_x}, {antinode2_y}")
                        antinode2_x += dx
                        antinode2_y += dy

        return len(antinodes)

raw_map = []

with open('input_data.txt') as f:
    raw_map = f.read().splitlines()

map = Map(raw_map)

print(map.find_antinodes())