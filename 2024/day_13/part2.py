from collections import deque, Counter
import numpy as np

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
        prize_x = int(prize.split(",")[0].split(" ")[1].split("=")[1]) + 10000000000000
        prize_y = int(prize.split(",")[1].split("=")[1]) + 10000000000000
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
        target_x, target_y = self.prize
        
        # Get the determinant of the button movement matrix
        det = self.a_button.x * self.b_button.y - self.b_button.x * self.a_button.y
        
        if det == 0:  # buttons are linearly dependent
            return False
            
        # Use Cramer's rule with integer arithmetic
        num_a = target_x * self.b_button.y - self.b_button.x * target_y
        num_b = self.a_button.x * target_y - target_x * self.a_button.y
        
        # Check if there's an integer solution
        if num_a % det != 0 or num_b % det != 0:
            return False
            
        # Get the solution
        a_presses = num_a // det
        b_presses = num_b // det
        
        # Check if solution requires non-negative button presses
        return a_presses >= 0 and b_presses >= 0

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

    if not machine.can_reach_prize():
        continue

    A = [machine.a_button.x, machine.a_button.y]
    B = [machine.b_button.x, machine.b_button.y]
    target = [machine.prize[0], machine.prize[1]]

    try:
        a = np.array([[A[0], B[0]], [A[1], B[1]]])
        b = np.array(target)
        solution = np.linalg.solve(a, b)

        # More lenient check for non-negative and near-integer solutions
        if all(s >= 0 for s in solution):
            print(f" machine number: {machine_number}, solution[0]: {np.int64(solution[0])}, solution[1]: {np.int64(solution[1])}")

            cost_a = np.int64(round(solution[0]) * 3)
            cost_b = np.int64(round(solution[1]))

            cheapest_cost[machine_number] = cost_a + cost_b
    except np.linalg.LinAlgError:
        continue
    


print(f"Cheapest cost for all claw machines is {sum(cheapest_cost.values())}")