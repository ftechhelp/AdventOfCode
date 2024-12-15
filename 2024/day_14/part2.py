class Navigate:

    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)
    directions = [left, right, up, down]

    def is_valid_position(self, max: tuple, position: tuple):

        x, y = position
        max_x, max_y = max

        return (0 <= x < max_x and 0 <= y < max_y)

            
    def get_next_position(self, direction, position):

        return (position[0] + direction[0], position[1] + direction[1])

class Robot:

    def __init__(self, starting_position: tuple[int, int], velocity: tuple[int, int]):

        self.position = starting_position
        self.velocity = velocity

    def _is_exactly_in_middle(self, max: tuple[int, int]):

        x, y = self.position
        max_x, max_y = max
        middle_x, middle_y = max_x // 2, max_y // 2

        return x == middle_x or y == middle_y


    def __str__(self):
        return f"Position: {self.position}, Velocity: {self.velocity}"

raw_robots: list[str] = []
robots: list[Robot] = []

with open('input_data.txt') as f:
    raw_robots = f.read().splitlines()

for raw_robot in raw_robots:
    starting_x = int(raw_robot.split(" ")[0].split("=")[1].split(",")[0])
    starting_y = int(raw_robot.split(" ")[0].split("=")[1].split(",")[1])
    velocity_x = int(raw_robot.split(" ")[1].split("=")[1].split(",")[0])
    velocity_y = int(raw_robot.split(" ")[1].split("=")[1].split(",")[1])
    robots.append(Robot((starting_x, starting_y), (velocity_x, velocity_y)))

bathroom_width = 101
bathroom_height = 103

#bathroom_width = 11
#bathroom_height = 7

middle_x, middle_y = bathroom_width // 2, bathroom_height // 2
#print(f"Middle: {middle_x}, {middle_y}")
first_quadrant_robot_count = 0
second_quadrant_robot_count = 0
third_quadrant_robot_count = 0
fourth_quadrant_robot_count = 0
seconds_elapsed = 0

position_tracker = {}

for robot_number, robot in enumerate(robots):

    #print(f"Moving robot {robot_number}")

    for second in range(100):

        seconds_elapsed += 1

        #print(f"Second: {second + 1}")
        #print(f"Current Position: {robot.position}")

        robot_next_position = Navigate().get_next_position(robot.velocity, robot.position)

        #print(f"Moving to position: {robot_next_position}")

        if not Navigate().is_valid_position((bathroom_width, bathroom_height), robot_next_position):
            
            #print("Needs to Teleport...")
            next_x, next_y = robot_next_position
            #fix y
            if next_y < 0:
                next_y += bathroom_height

            elif next_y >= bathroom_height:
                next_y -= bathroom_height

            #fix x
            if next_x < 0:
                next_x += bathroom_width

            elif next_x >= bathroom_width:
                next_x -= bathroom_width

            #print(f"Teleporting to: {next_x}, {next_y}")

            robot_next_position = (next_x, next_y)


        robot.position = robot_next_position

        


    #print(f"Final Position: {robot.position} for robot {robot_number}")

    if robot.position[0] < middle_x and robot.position[1] < middle_y:
        first_quadrant_robot_count += 1

    elif robot.position[0] < middle_x and robot.position[1] > middle_y:
        third_quadrant_robot_count += 1

    elif robot.position[0] > middle_x and robot.position[1] < middle_y:
        second_quadrant_robot_count += 1

    elif robot.position[0] > middle_x and robot.position[1] > middle_y:
        fourth_quadrant_robot_count += 1


#print(first_quadrant_robot_count)
#print(second_quadrant_robot_count)
#print(third_quadrant_robot_count)
#print(fourth_quadrant_robot_count)

security_factor = first_quadrant_robot_count * second_quadrant_robot_count * third_quadrant_robot_count * fourth_quadrant_robot_count
#print(f"Security Factor: {security_factor}")

