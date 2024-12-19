def can_form_word(word, pieces):

    if not word:
        return True
    
    for piece in pieces:

        if word.startswith(piece):

            if can_form_word(word[len(piece):], pieces):
                return True
            
    return False

def check_words(words, pieces):

    results = {}

    for word in words:
        results[word] = can_form_word(word, pieces)
    
    return results

raw = []
pieces = []
words = []

with open("input_data.txt") as f:
    raw = f.read().splitlines()

pieces = raw[0].split(", ")

for i in range(2, len(raw)):
    words.append(raw[i])


#print (pieces)
#print(words)
results = check_words(words, pieces)
print(len([word for word, result in results.items() if result]))