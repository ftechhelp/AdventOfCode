from collections import deque, Counter

class Button:

    def __init__(self, button: str, button_programming: str):
        
        x = int(button_programming.split(",")[0].split(" ")[2].split("+")[1])
        y = int(button_programming.split(",")[1].split("+")[1])

        self.button = button
        self.x = x
        self.y = y
        self.cost = 1 if button == "B" else 3

    def press(self, claw_money, x, y, times_pressed = 1):

        for _ in range(times_pressed):
            claw_money += self.cost
            x += self.x
            y += self.y

        return claw_money, x, y

    def __str__(self):
        return f"{self.button}: X+{self.x}, Y+{self.y}"

class ClawMachine:

    def __init__(self, machine_makeup):

        a_button = machine_makeup[0]
        b_button = machine_makeup[1]

        prize = machine_makeup[2]
        prize_x = int("10000000000000" + prize.split(",")[0].split(" ")[1].split("=")[1])
        prize_y = int("10000000000000" + prize.split(",")[1].split("=")[1])
        self.a_button = Button("A", a_button)
        self.b_button = Button("B", b_button)
        self.money_put_in = 0
        self.prize = (prize_x, prize_y)
        self.claw_position = (0, 0)

    def greatest_common_divisor(self, a, b):
        
        while b:
            a, b = b, a % b
        return a

    def can_reach_prize(self):

        x_gcd = self.greatest_common_divisor(self.a_button.x, self.b_button.x)
        y_gcd = self.greatest_common_divisor(self.a_button.y, self.b_button.y)
        target_x, target_y = self.prize
        
        return target_x % x_gcd == 0 and target_y % y_gcd == 0

    def __str__(self):
        return f"{self.a_button}, {self.b_button}, Money: {self.money_put_in}, Prize: {self.prize}, Claw Position: {self.claw_position}"


claw_machine_instructions = []

with open('input_data.txt') as f:
    claw_machine_instructions = f.read().splitlines()

machines: list[ClawMachine] = []
machine_makeup = []



for instruction in claw_machine_instructions:

    if instruction == "":
        machines.append(ClawMachine(machine_makeup))
        machine_makeup = []
        continue

    machine_makeup.append(instruction)

machines.append(ClawMachine(machine_makeup))

cheapest_cost = Counter()

for machine_number, machine in enumerate(machines):

    queue = deque([(0, 0, 0)])  # x, y, cost
    visited = set((0, 0))

    while queue:
        x, y, cost = queue.popleft()

        if not machine.can_reach_prize():
            continue

        if (x, y) == machine.prize:
            print(f"Machine number {machine_number} Won!")
            print(f"Cost: {cost}")
            print(machine)

            if cheapest_cost[machine_number] == 0 or cost < cheapest_cost[machine_number]:
                cheapest_cost[machine_number] = cost
        
        #A button
        next_x, next_y = x + machine.a_button.x, y + machine.a_button.y
        next_cost = cost + machine.a_button.cost

        if (next_x, next_y) not in visited and next_x <= machine.prize[0] and next_y <= machine.prize[1]:
            queue.append((next_x, next_y, next_cost))
            visited.add((next_x, next_y))

        #B button
        next_x, next_y = x + machine.b_button.x, y + machine.b_button.y
        next_cost = cost + machine.b_button.cost

        if (next_x, next_y) not in visited and next_x <= machine.prize[0] and next_y <= machine.prize[1]:
            queue.append((next_x, next_y, next_cost))
            visited.add((next_x, next_y))

print(f"Cheapest cost for all claw machines is {sum(cheapest_cost.values())}")