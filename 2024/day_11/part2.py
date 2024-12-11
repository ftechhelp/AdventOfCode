from collections import Counter

def transform(stone: str) -> list:

    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        return [str(int(stone[:len(stone) // 2])), str(int(stone[len(stone) // 2:]))]
    else:
        return [str(int(stone) * 2024)]

def blink(stones: list, n):
    stones: Counter = Counter(stones)

    for i in range(n):
        print (f"Blink {i + 1}")
        #print(f"Stones: {stones}")
        new_stones = Counter()

        for engraving in stones.keys():
            
            for new_engraving in transform(engraving):
                new_stones[new_engraving] += stones[engraving]

        stones = new_stones

    print(sum(stones.values()))

stones = []

with open('input_data.txt') as f:
    stones = f.read().split(" ")

#print(f"Initial Stones: {stones}")
blink(stones, 75)