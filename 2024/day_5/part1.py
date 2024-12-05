class Rule:

    def __init__(self, before_numbers= set(), after_numbers = set()):
        self.before_numbers = before_numbers
        self.after_numbers = after_numbers

    def __str__(self):
        return f"Before Numbers: {self.before_numbers} | After Numbers: {self.after_numbers}"
    
    def __repr__(self):
        return f"Before Numbers: {self.before_numbers} | After Numbers: {self.after_numbers}"

def compile_rules(raw_rules: list) -> dict:
    rules = {}

    for rule in raw_rules:
        before_and_after_numbers = rule.split("|")
        before_number = before_and_after_numbers[0]
        after_number = before_and_after_numbers[1]

        if before_number not in rules:
            rules[before_number] = Rule(after_numbers={after_number})
        else:
            rules[before_number].after_numbers.add(after_number)
        
        if after_number not in rules:
            rules[after_number] = Rule(before_numbers={before_number})
        else:
            rules[after_number].before_numbers.add(before_number)

    return rules

def is_valid_update_number(number: str, index: int, rule: Rule, list_update: list) -> bool:

    print(f"{number}")

    for before_number in rule.before_numbers:

        if before_number in list_update and list_update.index(before_number) > index:
            print(f"Before number {before_number}, index {list_update.index(before_number)} > number index {index}")
            return False
        
    for after_number in rule.after_numbers:

        if after_number in list_update and list_update.index(after_number) < index:
            print(f"After number {after_number}, index {list_update.index(after_number)} < number index {index}")
            return False
    
    print(f"{number} does not break any ordering rules")
    return True

raw_rules = []
raw_updates = []

with open('example_rules.txt') as f:
    raw_rules = f.read().splitlines()

with open('example_updates.txt') as f:
    raw_updates = f.read().splitlines()

rules = compile_rules(raw_rules)
middle_page_numbers = []

for update in raw_updates:
    list_update = update.split(",")
    correct_updates = 0
    
    for i in range(len(list_update)):
        current_number = list_update[i]
        rule = rules[current_number]

        if is_valid_update_number(current_number, i, rule, list_update):
            correct_updates += 1

    if correct_updates == len(list_update):
        middle_page_numbers.append(list_update[len(list_update) // 2])

print(middle_page_numbers)
