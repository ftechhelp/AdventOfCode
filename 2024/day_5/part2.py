class Rule:

    def __init__(self, before_numbers, after_numbers):
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

        print(f"Rule: {rule}")
        print(f"Before and after numbers: {before_and_after_numbers}")
        print(f"Before Number: {before_number}")
        print(f"After Number: {after_number}")

        if before_number not in rules:
            rules[before_number] = Rule(set(), {after_number})
            print(f"[{before_number}] -> Init rule with after numbers: {rules[before_number].after_numbers}")
        else:
            rules[before_number].after_numbers.add(after_number)
            print(f"[{before_number}] -> Added {after_number} to after numbers: {rules[before_number].after_numbers}")
        
        if after_number not in rules:
            rules[after_number] = Rule({before_number}, set())
            print(f"[{after_number}] -> Init rule with before numbers: {rules[after_number].before_numbers}")
        else:
            rules[after_number].before_numbers.add(before_number)
            print(f"[{after_number}] -> Added {before_number} to before numbers: {rules[after_number].before_numbers}")

        print("-----------------------------------")

    return rules

def is_valid_update_number(number: str, index: int, rule: Rule, list_update: list) -> bool:

    print(f"{number}")

    for before_number in rule.before_numbers:

        if before_number in list_update and list_update.index(before_number) > index:
            print(f"Before number {before_number}, index {list_update.index(before_number)} > number index {index}")
            print(f"[{number}] -> {rule}")
            return False
        
    for after_number in rule.after_numbers:

        if after_number in list_update and list_update.index(after_number) < index:
            print(f"After number {after_number}, index {list_update.index(after_number)} < number index {index}")
            print(f"[{number}] -> {rule}")
            return False
    
    print(f"{number} does not break any ordering rules")
    return True

def is_valid_update_number(number: str, index: int, rule: Rule, list_update: list) -> bool:

    print(f"{number}")

    for before_number in rule.before_numbers:

        if before_number in list_update and list_update.index(before_number) > index:
            print(f"Before number {before_number}, index {list_update.index(before_number)} > number index {index}")
            print(f"[{number}] -> {rule}")

            return False
        
    for after_number in rule.after_numbers:

        if after_number in list_update and list_update.index(after_number) < index:
            print(f"After number {after_number}, index {list_update.index(after_number)} < number index {index}")
            print(f"[{number}] -> {rule}")
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
invalid_update_rows = []

for update in raw_updates:
    list_update = update.split(",")
    
    for i in range(len(list_update)):
        current_number = list_update[i]
        rule = rules[current_number]

        if not is_valid_update_number(current_number, i, rule, list_update):
            invalid_update_rows.append(list_update)
            break

print(invalid_update_rows)
            


