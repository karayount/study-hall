# given a dictionary of word positions (where they are in a body of text), find
# the starting indices of all instances of an input 2-word phrase

word_positions = {
    "chicken": [29, 35, 46, 59, 67, 99],
    "wings": [30, 47, 78, 100],
}

phrase = "chicken wings"

def find_phrase(word_positions, phrase):
    phrase_words = phrase.split()
    first = phrase_words[0]
    second = phrase_words[1]
    first_positions = word_positions.get(first, [])
    second_positions = word_positions.get(second, [])

    result = []

    # brute force solution
    # for fp in first_positions:
    #     for sp in second_positions:
    #         if sp == fp + 1:
    #             result.append(fp)

    # solve in better than O(n^2), using pointer to loop second list
    index = 0
    for pos in first_positions:
        while (second_positions[index] < pos) and (index < len(second_positions)):
            index += 1
        if (pos + 1) == second_positions[index]:
            result.append(pos)

    return result

fred = find_phrase(word_positions, phrase)
print fred