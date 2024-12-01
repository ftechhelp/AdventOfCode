list_data = []

with open('input_data.txt') as f:
    list_data = f.read().splitlines()

list1 = []
list2 = []

for list_items in list_data:
    list1_number = list_items.split("   ")[0]
    list2_number = list_items.split("   ")[1]

    list1.append(list1_number)
    list2.append(list2_number)

list1_sorted = sorted(list1)
list2_sorted = sorted(list2)

distance_total = 0

for i in range(len(list1)):
    distance_total += abs(int(list1_sorted[i]) - int(list2_sorted[i]))

print(distance_total)