reports = []

with open('input_data.txt') as f:
    reports = f.read().splitlines()

safe_reports = 0

for report in reports:
    levels = report.split(" ")
    increasing = False
    decreasing = False

    print(f"Processing Report: {report}")

    for i in range(len(levels)):
        print(f"Index: {i}")

        if increasing and decreasing:
            print(f"UNSAFE! We are increasing and decreasing.")
            print(f"-----------------------------------------")
            break

        the_end = i == len(levels) - 1

        print(f"The End?: {the_end}")

        if the_end:
            safe_reports += 1
            print(f"Safe Report Count: {safe_reports}")
            print(f"-----------------------------------------")
            break

        current_level = int(levels[i])
        next_level = int(levels[i + 1])

        print(f"Current Level: {current_level}")
        print(f"Next Level: {next_level}")
        
        if current_level == next_level:
            print(f"UNSAFE! {current_level} and {next_level} are the same")
            print(f"-----------------------------------------")
            break

        level_difference = abs(int(current_level) - int(next_level))
        print(f"Level Difference Between {current_level} and {next_level}: {level_difference}")
        
        if level_difference > 3:
            print(f"UNSAFE! {current_level} and {next_level} differ more than 3")
            print(f"-----------------------------------------")
            break

        if current_level > next_level:
            print(f"We Are Decreasing v")
            decreasing = True

        if current_level < next_level:
            print(f"We Are Increasing ^")
            increasing = True

print(safe_reports)

        