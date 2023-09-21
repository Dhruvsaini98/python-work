def find_longest_word(sentence):
    # Split the sentence into words using split()
    words_list = sentence.split()

    # Find the longest word using max() with a custom key
    longest_word = max(words_list, key=len)

    return longest_word

# Test case
sentence = "This is a sample sentence with some long words."
longest_word = find_longest_word(sentence)
print(longest_word)  # Output: "sentence"
