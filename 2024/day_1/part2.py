list_data = []

with open('input_data.txt') as f:
    list_data = f.read().splitlines()

list1 = []
list2 = {}

for list_items in list_data:
    list1_number = list_items.split("   ")[0]
    list2_number = list_items.split("   ")[1]

    list1.append(list1_number)
    
    if list2_number not in list2:
        list2[list2_number] = 1
    else:
        list2[list2_number] += 1

similarity_score = 0

for number in list1:
    similarity = int(number) * list2[number] if number in list2 else 0
    similarity_score += similarity