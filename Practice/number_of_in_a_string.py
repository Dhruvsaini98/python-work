def count_words(input_string):
     # Split the string into words using split()
     words_list = input_string.split()
    
     # Return the number of words in the list
     return len(words_list)

 # Test case
sentence = "This is a sample sentence with some words."
word_count = count_words(sentence)
print(word_count)  # Output: 9 (This, is, a, sample, sentence, with, some, words.)
