import math

class SecretNumberGenerator:

    def __init__(self):

        self.secret_number = None

    def generate_secret_number(self, initial_value: int, nth_times: int) -> int:
        
        self.secret_number = initial_value

        for i in range(nth_times):
            self._calculate_secret_number(self.secret_number, i + 1)

        return self.secret_number

    def _mix(self, value: int) -> int:
        self.secret_number = value ^ self.secret_number

    def _prune(self) -> int:
        self.secret_number = self.secret_number % 16777216

    def _calculate_secret_number(self, initial_value: int, nth_time: int) -> int:

        multiplied_secret = initial_value * 64
        self._mix(multiplied_secret)
        self._prune()

        divided_secret = math.floor(self.secret_number / 32)
        self._mix(divided_secret)
        self._prune()

        multiplied_secret2 = self.secret_number * 2048
        self._mix(multiplied_secret2)
        self._prune()

        #print(f"Secret Number: {self.secret_number} After {nth_time} times")

initial_secret_numbers = []

with open('input_data.txt') as f:
    initial_secret_numbers = f.read().splitlines()

generator = SecretNumberGenerator()
secret_numbers = []

for initial_secret_number in initial_secret_numbers:
    secret_number = generator.generate_secret_number(int(initial_secret_number), 2000)
    secret_numbers.append(secret_number)
    print(f"{initial_secret_number}: {secret_number}")

print(f"Total Secret Number: {sum(secret_numbers)}")