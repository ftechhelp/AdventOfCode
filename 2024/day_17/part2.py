class Computer:

    def __init__(self, initial_A: int, program: list):

        self.register_A = initial_A
        self.register_B = 0
        self.register_C = 0
        self.program = program
        self.instruction_pointer = 0
        self.output_buffer = []

    def _get_combo_operand(self, operand: int):

        if 0 <= operand <= 3:
            return operand

        if operand == 4:
            return self.register_A

        if operand == 5:
            return self.register_B

        if operand == 6:
            return self.register_C
        
    def _adv(self, operand: int):

        numerator = self.register_A
        denominator = 2 ** self._get_combo_operand(operand)
        self.register_A = numerator // denominator

        #print(f"Ran _adv setting register A: {self.register_A}")

    def _bxl(self, operand: int):

        bitwise_XOR = self.register_B ^ operand
        self.register_B = bitwise_XOR

        #print(f"Ran _bxl setting register B: {self.register_B}")

    def _bst(self, operand: int):

        self.register_B = self._get_combo_operand(operand) % 8

        #print(f"Ran _bst setting register B: {self.register_B}")

    def _jnz(self, operand: int):

        if self.register_A == 0:
            self.instruction_pointer += 2
            return
        
        self.instruction_pointer = operand

        #print(f"Ran _jnz setting instruction pointer: {self.instruction_pointer}")

    def _bxc(self, operand: int):

        self.register_B = self.register_B ^ self.register_C

        #print(f"Ran _bxc setting register B: {self.register_B}")

    def _out(self, operand: int):

        output = self._get_combo_operand(operand) % 8
        self.output_buffer.append(output)

        #print(f"Ran _out setting output buffer: {self.output_buffer}")

    def _bdv(self, operand: int):

        numerator = self.register_A
        denominator = 2 ** self._get_combo_operand(operand)
        self.register_B = numerator // denominator

        #print(f"Ran _bdv setting register B: {self.register_B}")

    def _cdv(self, operand: int):

        numerator = self.register_A
        denominator = 2 ** self._get_combo_operand(operand)
        self.register_C = numerator // denominator

        #print(f"Ran _cdv setting register C: {self.register_C}")
    
    def run_program(self):

        while self.instruction_pointer < len(self.program):

            #print(f"Instruction Pointer: {self.instruction_pointer}")

            instruction = self.program[self.instruction_pointer]

            #print(f"Instruction: {instruction}")

            if instruction == 0:
                self._adv(self.program[self.instruction_pointer + 1])
                self.instruction_pointer += 2

            if instruction == 1:
                self._bxl(self.program[self.instruction_pointer + 1])
                self.instruction_pointer += 2

            if instruction == 2:
                self._bst(self.program[self.instruction_pointer + 1])
                self.instruction_pointer += 2

            if instruction == 3:
                self._jnz(self.program[self.instruction_pointer + 1])

            if instruction == 4:
                self._bxc(self.program[self.instruction_pointer + 1])
                self.instruction_pointer += 2

            if instruction == 5:
                self._out(self.program[self.instruction_pointer + 1])
                self.instruction_pointer += 2

            if instruction == 6:
                self._bdv(self.program[self.instruction_pointer + 1])
                self.instruction_pointer += 2

            if instruction == 7:
                self._cdv(self.program[self.instruction_pointer + 1])
                self.instruction_pointer += 2

        return  self.output_buffer


def find_self_replicating_A(is_example: bool = True):

    program = [0,3,5,4,3,0] if is_example else [2,4,1,5,7,5,4,5,0,3,1,6,5,5,3,0]
    
    for initial_A in range(100000000, 1000000000):

        if is_example:
            if initial_A == 2024:
                continue

        computer = Computer(initial_A, program)
        output = computer.run_program()
        
        if output == program:
            return initial_A
            
    return None

# Run the search
result = find_self_replicating_A(False)
print(f"Lowest value of A that produces self-replicating output: {result}")