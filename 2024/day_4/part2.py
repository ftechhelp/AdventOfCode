class WordSearch:

    def __init__(self, word, word_search):
        self.word = word
        self.word_search = word_search
        self.criss_cross = 0
        self.criss_cross_indexes = {}

    def find(self):

        for row_index in range(len(word_search)):
            current_row = word_search[row_index]

            for character_index in range(len(current_row)):
                current_character = current_row[character_index]
                    
                if current_character == self.word[0]:
                    self._check_next(self.word[0], row_index, character_index, "right", "up", 0)
                    self._check_next(self.word[0], row_index, character_index, "right", "down", 0)
                    self._check_next(self.word[0], row_index, character_index, "left", "up", 0)
                    self._check_next(self.word[0], row_index, character_index, "left", "down", 0)

        for criss_cross_index in self.criss_cross_indexes:
            if self.criss_cross_indexes[criss_cross_index] == 2:
                self.criss_cross += 1

        print(self.criss_cross)

    def _check_next(self, building_word, row_index, character_index, left_or_right, up_or_down, character_count) -> int:
        character_count += 1
        
        if building_word == self.word:
            print(f"We found the word '{self.word}'!")
            print("Recording criss cross index")
            if left_or_right == "right" and up_or_down == "up":
                if f"{row_index + 1}-{character_index - 1}" not in self.criss_cross_indexes:
                    self.criss_cross_indexes[f"{row_index + 1}-{character_index - 1}"] = 1
                else:
                    self.criss_cross_indexes[f"{row_index + 1}-{character_index - 1}"] += 1
            
            if left_or_right == "right" and up_or_down == "down":
                if f"{row_index - 1}-{character_index - 1}" not in self.criss_cross_indexes:
                    self.criss_cross_indexes[f"{row_index - 1}-{character_index - 1}"] = 1
                else:
                    self.criss_cross_indexes[f"{row_index - 1}-{character_index - 1}"] += 1
            
            if left_or_right == "left" and up_or_down == "up":
                if f"{row_index + 1}-{character_index + 1}" not in self.criss_cross_indexes:
                    self.criss_cross_indexes[f"{row_index + 1}-{character_index + 1}"] = 1
                else:
                    self.criss_cross_indexes[f"{row_index + 1}-{character_index + 1}"] += 1

            if left_or_right == "left" and up_or_down == "down":
                if f"{row_index - 1}-{character_index + 1}" not in self.criss_cross_indexes:
                    self.criss_cross_indexes[f"{row_index - 1}-{character_index + 1}"] = 1
                else:
                    self.criss_cross_indexes[f"{row_index - 1}-{character_index + 1}"] += 1
            
            return 1
        
        if character_count > len(self.word):
            print(f"Character count {character_count} greater than the length of the word ({len(self.word)})")
            return 0
        
        if left_or_right == "right":
            print(f"Going right")
            if (character_index + 1) >= len(self.word_search[row_index]):
                print(f"Character index ({character_index + 1})is past row index max ({len(self.word_search[row_index]) - 1})")
                return 0
            
            character_index += 1

        if left_or_right == "left":
            print(f"Going left")
            if (character_index - 1) < 0:
                print(f"Character index ({character_index - 1})is past row index min (0)")
                return 0
            
            character_index -= 1

        if up_or_down == "up":
            print(f"Going up")
            if (row_index - 1) < 0:
                print(f"Row index ({row_index - 1}) is past word_search index min (0)")
                return 0
            
            row_index -= 1

        if up_or_down == "down":
            print(f"Going down")
            if (row_index + 1) >= len(self.word_search):
                print(f"Row index ({row_index + 1}) is past word_search index max ({len(self.word_search) - 1})")
                return 0
            
            row_index += 1

        print(f"Check if {self.word[character_count]} is equal to {self.word_search[row_index][character_index]}")

        if self.word[character_count] == self.word_search[row_index][character_index]:
            building_word += self.word_search[row_index][character_index]
            print(f"Nice, it is! Now our building word is: {building_word}")
            return self._check_next(building_word, row_index, character_index, left_or_right, up_or_down, character_count)
        
        print(f"Word we are looking for is no longer {self.word}")
        return 0


word_search = []

with open('input_data.txt') as f:
    word_search = f.read().splitlines()
            
search = WordSearch("MAS", word_search)
search.find()