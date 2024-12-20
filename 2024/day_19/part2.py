def count_combinations(word, pieces, memo = None):

    if memo is None:
        memo = {}
    
    if word in memo:
        return memo[word]

    if not word:
        return 1
    
    count = 0

    for piece in pieces:

        if word.startswith(piece):

            count += count_combinations(word[len(piece):], pieces, memo)
            
    memo[word] = count
    return count

def check_words_combinations(words, pieces):

    results = {}

    for word_count, word in enumerate(words):
        results[word] = count_combinations(word, pieces)
        print(f"Processed words: {word_count + 1} / {len(words)}")
    
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
results = check_words_combinations(words, pieces)
print(sum(results.values()))