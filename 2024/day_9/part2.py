from collections import OrderedDict

class SpaceCompacterProgram:

    def __init__(self, disk_map):
        self.disk_map = disk_map
        self.empty_space_indexes = OrderedDict()
        self.id_groups = OrderedDict()
    
    def _get_decompressed_disk_map(self) -> list:
        decompressed_disk_map = []
        self.empty_space_indexes = {}
        data_id = 0

        for index, data in enumerate(self.disk_map):

            if index % 2 == 0: #file block

                if data == "0":
                    continue

                self.id_groups[str(len(decompressed_disk_map))] = (data)

                for i in range(int(data)):
                    decompressed_disk_map.append(str(data_id))

                data_id += 1
                
            else: #empty space

                if data == "0":
                    continue

                self.empty_space_indexes[str(len(decompressed_disk_map))] = (len(decompressed_disk_map), data)

                for i in range(int(data)):
                    decompressed_disk_map.append(".")
        
        self.id_groups = OrderedDict(reversed(list(self.id_groups.items())))
        #print(f"Decompressed Disk Map Length: {len(decompressed_disk_map)}")
        return decompressed_disk_map
    
    def _fragment(self) -> list:
        decompressed_disk_map = self._get_decompressed_disk_map()
        #print(f"Decompressed Disk Map: {decompressed_disk_map}")
        #print(f"Empty Space Indexes: {self.empty_space_indexes}")
        #print(f"ID Groups: {self.id_groups}")

        for group_start_index, group_count in self.id_groups.items():
            group_start_index = int(group_start_index)
            group_count = int(group_count)

            file_id = decompressed_disk_map[group_start_index]

            for empty_space_start_index, space_index_and_count in self.empty_space_indexes.items():

                #print(f"Empty Space And Count: {space_index_and_count} for start index: {empty_space_start_index}")
                #print(f"Group Start Index: {group_start_index} and Group Count: {group_count} and File ID: {file_id}")

                if space_index_and_count[0] == None:
                    #print(f"No more space at index {empty_space_start_index}")
                    continue

                if space_index_and_count[0] >= group_start_index:
                    #print(f"We are looking for empty space past file id {file_id} (Empty space index: {space_index_and_count[0]}, Group Start Index: {group_start_index})")
                    break

                space_count = int(space_index_and_count[1])

                if group_count > space_count: #space too small, check next one
                    #print(f"Space too small ({space_count}) for file id {file_id} ({group_count}). Skipping...")
                    continue

                #update disk map
                for i in range(space_index_and_count[0], space_index_and_count[0] + group_count):
                    decompressed_disk_map[i] = file_id
                
                for i in range(group_start_index, group_start_index + group_count):
                    decompressed_disk_map[i] = "."

                #print(f"Moved file ID {file_id}, update disk map: {decompressed_disk_map}")
                
                #update empty space
                if space_count - group_count == 0:
                    self.empty_space_indexes[empty_space_start_index] = (None, None)
                    break

                self.empty_space_indexes[empty_space_start_index] = (int(space_index_and_count[0]) + (group_count), str(space_count - group_count))
                #print(f"Updated empty space: {self.empty_space_indexes[empty_space_start_index]}")
                
                break
        
        return decompressed_disk_map
    
    def get_updated_filesystem_checksum(self):
        fragmented_disk_map = self._fragment()
        #print(f"Fragmented Disk Map: {fragmented_disk_map}")
        checksum = 0

        for index, data in enumerate(fragmented_disk_map):

            if data == ".":
                continue

            checksum += (index * int(data))

        return checksum




disk_map = ""

with open('input_data.txt') as f:
    disk_map = f.read()

program = SpaceCompacterProgram(disk_map)
print(f"Checksum: {program.get_updated_filesystem_checksum()}")