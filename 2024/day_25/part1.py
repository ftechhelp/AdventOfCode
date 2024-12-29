from collections import Counter

class Raw:

    def _load_raw(self, raw_key_or_lock: list[list[str]]) -> list[int]:

        heights = [0,0,0,0,0]
        
        for y, row in enumerate(raw_key_or_lock):

            if y == 0 or y == 6:
                continue

            for x, cell in enumerate(row[0]):
                
                if cell == "#":
                    heights[x] += 1

        return heights


class Key(Raw):

    def __init__(self, raw_key: list[list[str]]):

        self.key_heights = self._load_raw(raw_key)

    def __str__(self):

        return f"Key: {self.key_heights}"

    def __repr__(self):

        return f"Key: {self.key_heights}"

class Lock(Raw):

    def __init__(self, raw_lock: list[list[str]]):

        self.pin_heights = self._load_raw(raw_lock)

    def unlocks(self, key: Key) -> bool:

        for i in range(len(self.pin_heights)):

            if self.pin_heights[i] + key.key_heights[i] > 5:
                return False

        return True


    def __str__(self):

        return f"Lock: {self.pin_heights}"

    def __repr__(self):

        return f"Lock: {self.pin_heights}"

raw_lock_key_info = []
keys: list[Key] = []
locks: list[Lock] = []

with open("input_data.txt") as f:
    temp = []
    for line in f:
        if line.strip() == "":
            raw_lock_key_info.append(temp)
            temp = []
        else:
            temp.append(line.strip().split())
    raw_lock_key_info.append(temp)

for raw_lock_key in raw_lock_key_info:

    if raw_lock_key[0] == ["#####"]:
        locks.append(Lock(raw_lock_key))
    
    elif raw_lock_key[0] == ["....."]:
        keys.append(Key(raw_lock_key))

print(f"Keys: {len(keys)} Locks: {len(locks)}")
print(f"Keys: {keys}")
print(f"Locks: {locks}")

unique_pairs = 0

for lock in locks:
    for key in keys:
        if lock.unlocks(key):
            unique_pairs += 1

print(f"Unique Pairs: {unique_pairs}")




