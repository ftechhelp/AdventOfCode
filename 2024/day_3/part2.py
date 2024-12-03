import re

def get_instructions_result(corrupted) -> int:
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    instructions = re.findall(pattern, corrupted)

    instruction_result_sum = 0

    for instruction in instructions:
        number1, number2 = instruction
        instruction_result = int(number1) * int(number2)
        instruction_result_sum += instruction_result

    return instruction_result_sum

def get_do_corrupted_instructions(memory) -> str:
    do = True
    dont = False
    do_corrupted_instructions = ""

    while len(memory.split("don't()")) > 1:

        if do:
            do_split = memory.split("don't()")
            do_corrupted_instructions += do_split[0]
            where_to_cut_off = len(do_split[0]) - 1
            memory = memory[where_to_cut_off:]
            do = False
            dont = True
        
        if dont:
            dont_split = memory.split("do()")
            where_to_cut_off = len(dont_split[0]) - 1
            memory = memory[where_to_cut_off:]
            do = True
            dont = False

    return do_corrupted_instructions

memory = ""

with open('input_data.txt') as f:
    memory = f.read()

do_corrupted_instructions = get_do_corrupted_instructions(memory)
do_instructions_result = get_instructions_result(do_corrupted_instructions)

print(do_instructions_result)