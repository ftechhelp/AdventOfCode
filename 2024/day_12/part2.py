class Navigate:

    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)
    directions = [left, right, up, down]

    up_left_corner = (-0.5, -0.5)
    up_right_corner = (0.5, -0.5)
    down_left_corner = (-0.5, 0.5)
    down_right_corner = (0.5, 0.5)

    corners = [up_left_corner, up_right_corner, down_left_corner, down_right_corner]

    def is_valid_position(self, map: list, position: tuple) -> bool:

        x, y = position

        return (0 <= x < len(map[0]) and 0 <= y < len(map))
    
    def get_next_position(self, direction, position):

        return (position[0] + direction[0], position[1] + direction[1])

class Plot:
    
    def __init__(self, position: tuple, plant_type: str):

        self.position = position
        self.plant_type = plant_type

    def get_corners(self) -> set:

        corners = set()

        for corner in Navigate().corners:
            corners.add(Navigate().get_next_position(corner, self.position))

        return corners
class Region:

    def __init__(self, map: list, plant_type: str):

        self.plots: list[Plot] = []
        self.plant_type = plant_type
        self.map = map

    def get_perimiter(self) -> int:

        possible_region_corners = set()

        for plot in self.plots:
            possible_region_corners = possible_region_corners.union(plot.get_corners())

        plot_positions = [plot.position for plot in self.plots]

        region_corner = 0

        for corner_x, corner_y in possible_region_corners:
            is_touching_region_plot_or_empty_spot_map = [(plot_x, plot_y) in plot_positions for plot_x, plot_y in [(corner_x - 0.5, corner_y - 0.5), (corner_x - 0.5, corner_y + 0.5), (corner_x + 0.5, corner_y + 0.5), (corner_x + 0.5, corner_y - 0.5)] ] # check if corner is touching region plot or empty spot map of plots around it
            number_of_touching_plots = sum(is_touching_region_plot_or_empty_spot_map)

            if number_of_touching_plots == 1:
                region_corner += 1
            elif number_of_touching_plots == 2:

                if is_touching_region_plot_or_empty_spot_map == [True, False, True, False] or is_touching_region_plot_or_empty_spot_map == [False, True, False, True]:
                    region_corner += 2
            elif number_of_touching_plots == 3:
                region_corner += 1

        return region_corner

    def get_area(self) -> int:

        return len(self.plots)
    
    def get_fence_cost(self) -> int:

        return self.get_area() * self.get_perimiter()
    
class GardenPlotMap:

    def __init__(self, map: list):

        self.map = map
        self.plots_visited = set()
        self.regions = []

    def get_regions(self) -> None:

        for y, row in enumerate(self.map):

            for x, plant_type in enumerate(row):

                if (x, y) in self.plots_visited:
                    continue
                
                region = Region(self.map, plant_type)
                self.walk_region((x, y), region)
                self.regions.append(region)
    
    def walk_region(self, position: tuple, region: Region) -> None:

        if position in self.plots_visited:
            return
        
        plot = Plot(position, region.plant_type)
        region.plots.append(plot)
        self.plots_visited.add(position)

        for direction in Navigate().directions:

            next_position = Navigate().get_next_position(direction, position)
            nx, ny = next_position
            
            if Navigate().is_valid_position(self.map, next_position) and self.map[ny][nx] == region.plant_type:
                self.walk_region(next_position, region)

    def get_total_fence_cost(self) -> int:

        total_fence_cost = 0

        for region in self.regions:
            total_fence_cost += region.get_fence_cost()

        return total_fence_cost

########################################################
small_example_map = []

with open('small_example.txt') as f:
    small_example_map = f.read().splitlines()

print("Small Example")

garden_plot_map = GardenPlotMap(small_example_map)
garden_plot_map.get_regions()

for region in garden_plot_map.regions:
    print(f"Plant Type: {region.plant_type} Area: {region.get_area()} Perimeter: {region.get_perimiter()} Fence Cost: {region.get_fence_cost()}")

print(f"Total Fence Cost: {garden_plot_map.get_total_fence_cost()}")
#########################################################
x_o_example_map = []

with open('x_o_example.txt') as f:
    x_o_example_map = f.read().splitlines()

print("X-O Example")

garden_plot_map = GardenPlotMap(x_o_example_map)
garden_plot_map.get_regions()

for region in garden_plot_map.regions:
    print(f"Plant Type: {region.plant_type} Area: {region.get_area()} Perimeter: {region.get_perimiter()} Fence Cost: {region.get_fence_cost()}")

print(f"Total Fence Cost: {garden_plot_map.get_total_fence_cost()}")
#########################################################
e_example_map = []

with open('e_example.txt') as f:
    e_example_map = f.read().splitlines()

print("E Example")

garden_plot_map = GardenPlotMap(e_example_map)
garden_plot_map.get_regions()

for region in garden_plot_map.regions:
    print(f"Plant Type: {region.plant_type} Area: {region.get_area()} Perimeter: {region.get_perimiter()} Fence Cost: {region.get_fence_cost()}")

print(f"Total Fence Cost: {garden_plot_map.get_total_fence_cost()}")
########################################################

#########################################################
example_map = []

with open('example.txt') as f:
    example_map = f.read().splitlines()

print("Example")

garden_plot_map = GardenPlotMap(example_map)
garden_plot_map.get_regions()

for region in garden_plot_map.regions:
    print(f"Plant Type: {region.plant_type} Area: {region.get_area()} Perimeter: {region.get_perimiter()} Fence Cost: {region.get_fence_cost()}")

print(f"Total Fence Cost: {garden_plot_map.get_total_fence_cost()}")
########################################################
map = []

with open('input_data.txt') as f:
    map = f.read().splitlines()

print("Input Data")

garden_plot_map = GardenPlotMap(map)
garden_plot_map.get_regions()

#for region in garden_plot_map.regions:
#    print(f"Plant Type: {region.plant_type} Area: {region.get_area()} Perimeter: {region.get_perimiter()} Fence Cost: {region.get_fence_cost()}")

print(f"Total Fence Cost: {garden_plot_map.get_total_fence_cost()}")
