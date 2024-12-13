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
        prize_x = int(prize.split(",")[0].split(" ")[1].split("=")[1])
        prize_y = int(prize.split(",")[1].split("=")[1])


        self.a_button = Button("A", a_button)
        self.b_button = Button("B", b_button)
        self.money_put_in = 0
        self.prize = (prize_x, prize_y)
        self.claw_position = (0, 0)

    def press_button_a(self, times_pressed: int = 1):

        clawmoney, x, y = self.a_button.press(self.money_put_in, self.claw_position[0], self.claw_position[1], times_pressed)
        self.money_put_in = clawmoney
        self.claw_position = (x, y)

    def press_button_b(self, times_pressed: int = 1):

        clawmoney, x, y = self.b_button.press(self.money_put_in, self.claw_position[0], self.claw_position[1], times_pressed)
        self.money_put_in = clawmoney
        self.claw_position = (x, y)

    def is_winning_position(self):
        return self.claw_position == self.prize

    def reset(self):
        self.money_put_in = 0
        self.claw_position = (0, 0)

    def __str__(self):
        return f"{self.a_button}, {self.b_button}, Money: {self.money_put_in}, Prize: {self.prize}"


claw_machine_instructions = []

with open('example.txt') as f:
    claw_machine_instructions = f.read().splitlines()

machines = []
machine_makeup = []

for instruction in claw_machine_instructions:

    if instruction == "":
        machines.append(ClawMachine(machine_makeup))
        machine_makeup = []
        continue

    machine_makeup.append(instruction)


total_money_spent = 0

