
def blink(stones: list, n):

    for i in range(n):

        #print (f"Blink {i + 1}")

        new_stones = []

        for position, engraving in enumerate(stones):

            if engraving == "0":
                new_stones.append("1")
            elif len(engraving) % 2 == 0:
                new_stones.append(engraving[:len(engraving) // 2])
                new_stones.append(str(int(engraving[len(engraving) // 2:])))
            else:
                new_stones.append(str(int(engraving) * 2024))

        #print(new_stones)
        stones = new_stones
    
    print(len(stones))


stones = []

with open('input_data.txt') as f:
    stones = f.read().split(" ")

blink(stones, 75)