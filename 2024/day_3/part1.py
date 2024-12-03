import re

memory = ""

with open('input_data.txt') as f:
    memory = f.read()

pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
instructions = re.findall(pattern, memory)

instruction_result_sum = 0

for instruction in instructions:
    number1, number2 = instruction
    instruction_result = int(number1) * int(number2)
    instruction_result_sum += instruction_result

print(instruction_result_sum)