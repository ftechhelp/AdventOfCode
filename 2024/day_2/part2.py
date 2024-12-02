def problem_dampner(report) -> int:
    levels = report.split(" ")

    for i in range(len(levels)):
        levels = report.split(" ")
        del levels[i]
        safe_report = process_report(levels)

        if safe_report == 1:
            return 1
        
    return 0


def process_report(report) -> int:
    levels = report
    increasing = False
    decreasing = False

    print(f"Processing Report: {report}")

    for i in range(len(levels)):
        print(f"Index: {i}")

        if increasing and decreasing:
            print(f"UNSAFE! We are increasing and decreasing.")
            print(f"-----------------------------------------")
            return 0

        the_end = i == len(levels) - 1

        print(f"The End?: {the_end}")

        if the_end:
            print(f"Safe Report Count: {safe_reports}")
            print(f"-----------------------------------------")
            return 1

        current_level = int(levels[i])
        next_level = int(levels[i + 1])

        print(f"Current Level: {current_level}")
        print(f"Next Level: {next_level}")
            
        if current_level == next_level:
            print(f"UNSAFE! {current_level} and {next_level} are the same")
            print(f"-----------------------------------------")
            return 0

        level_difference = abs(int(current_level) - int(next_level))
        print(f"Level Difference Between {current_level} and {next_level}: {level_difference}")
            
        if level_difference > 3:
            print(f"UNSAFE! {current_level} and {next_level} differ more than 3")
            print(f"-----------------------------------------")
            return 0

        if current_level > next_level:
            print(f"We Are Decreasing v")
            decreasing = True

        if current_level < next_level:
            print(f"We Are Increasing ^")
            increasing = True

reports = []

with open('input_data.txt') as f:
    reports = f.read().splitlines()

safe_reports = 0

for report in reports:
    safe_report = process_report(report.split(" "))

    if safe_report == 1:
        safe_reports += safe_report
        continue
    print(f"Sending Through Problem Dampner...")
    safe_reports += problem_dampner(report)

print(safe_reports)

        