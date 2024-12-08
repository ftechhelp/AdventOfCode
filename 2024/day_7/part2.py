import itertools

class Equation:

    def __init__(self, equation):
        self.result = int(equation.split(":")[0])
        self.numbers = equation.split(":")[1].strip().split(" ")
        self.operator_variations = self._generate_operator_variations(len(self.numbers) - 1)
        self.calibration_results = []

        #print(f"Equation: Numbers = {self.numbers}, Result = {self.result}")
        #print(f"Operator Variations: {self.operator_variations}")

    def _generate_operator_variations(self, n) -> list[tuple]:
        
        return list(itertools.product(["+", "*", "||"], repeat=n))
    
    def _is_equation_true(self):

        for operator_variation in self.operator_variations:
            
            #print(f"Current operation variation: {operator_variation}")
            
            equation_result = 0

            for i in range(len(self.numbers)):

                if (i + 1) == len(self.numbers):
                    break
                
                current_number = equation_result if i != 0 else self.numbers[i]
                next_number = self.numbers[i + 1]
                operator = operator_variation[i]

                if operator == "||":
                    equation_result = str(current_number) + str(next_number)
                if operator == "+":
                    #print(f"Doing: {current_number} + {next_number}")
                    equation_result = (int(current_number) + int(next_number))
                elif operator == "*":
                    #print(f"Doing: {current_number} * {next_number}")
                    equation_result = (int(current_number) * int(next_number))
                
                #print(f"Equation Result: {equation_result}")

            if int(equation_result) == self.result:
                #print(f"Equation True for: {self.numbers}, {operator_variation}")
                return True
            
            #print(f"Equation False for: {self.numbers}, {operator_variation} | {equation_result} != {self.result}")
        
        #print(f"Equation False for all operator variations")
        return False
    def get_calibration_result(self) -> int:
        
        if self._is_equation_true():
            return self.result
        
        return 0

raw_equations = []

with open('input_data.txt') as f:
    raw_equations = f.read().splitlines()


#equation = Equation(raw_equations[3])
#print(equation._is_equation_true())

total_calibration_result = 0

for raw_equation in raw_equations:
    equation = Equation(raw_equation)
    total_calibration_result += equation.get_calibration_result()

print(total_calibration_result)
