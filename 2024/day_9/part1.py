class SpaceCompacterProgram:

    def __init__(self, disk_map):
        self.disk_map = disk_map
        self.empty_space_indexes = []
    
    def _get_decompressed_disk_map(self) -> list:
        decompressed_disk_map = []
        self.empty_space_indexes = []
        data_id = 0

        for index, data in enumerate(self.disk_map):

            if index % 2 == 0: #file block

                if data == "0":
                    continue

                for i in range(int(data)):
                    decompressed_disk_map.append(str(data_id))

                data_id += 1
                
            else: #empty space

                if data == "0":
                    continue

                for i in range(int(data)):
                    decompressed_disk_map.append(".")
                    self.empty_space_indexes.append(len(decompressed_disk_map) - 1)

        return decompressed_disk_map
    
    def _fragment(self) -> list:
        decompressed_disk_map = self._get_decompressed_disk_map()
        print(f"Empty Space Indexes: {self.empty_space_indexes}")
        print(f"Decompressed Disk Map length: {len(decompressed_disk_map)}")

        while self.empty_space_indexes:

            for index, data in reversed(list(enumerate(decompressed_disk_map))):

                if data == ".":
                    continue

                first_empty_space_index = self.empty_space_indexes.pop(0)
                #print(f"Processing Empty Space Index: {first_empty_space_index}")

                if first_empty_space_index > index:
                    break

                decompressed_disk_map[first_empty_space_index] = data
                decompressed_disk_map[index] = "."
                #print(f"Fragmenting in progress: {decompressed_disk_map}")
                break

        return decompressed_disk_map
    
    def get_updated_filesystem_checksum(self):
        fragmented_disk_map = self._fragment()
        checksum = 0

        for index, data in enumerate(fragmented_disk_map):

            if data == ".":
                break

            checksum += (index * int(data))

        return checksum




disk_map = ""

with open('input_data.txt') as f:
    disk_map = f.read()

program = SpaceCompacterProgram(disk_map)
print(f"Checksum: {program.get_updated_filesystem_checksum()}")