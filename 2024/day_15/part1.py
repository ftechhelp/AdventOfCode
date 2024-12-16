import sys
sys.path.append("..")
from Libraries.navigate import Navigate

class Robot:
    

raw_map = []

with open('small_example.txt') as f:
    raw_map = f.read().splitlines()

is_robot_movements = False
map = []

for row in raw_map:

    if is_robot_movements:
        #Do some stuff
        continue

    if row[0] == "":
        is_robot_movements = True
        continue

    map.append(list(row))

