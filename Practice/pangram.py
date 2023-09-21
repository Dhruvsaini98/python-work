import string

def is_pangram(input_string):
    # Convert the input string to lowercase for case-insensitive comparison
    input_string_lower = input_string.lower()

    # Create a set of unique characters in the input string (excluding non-alphabetic characters)
    unique_chars = set()

    for char in input_string_lower:
        if char.isalpha():
            unique_chars.add(char)

    
    # Create a set of all lowercase alphabets
    all_alphabets = set(string.ascii_lowercase)

    # Check if the set of unique characters is equal to the set of all lowercase alphabets
    return unique_chars == all_alphabets

 # Test case
sentence = "The quick brown fox jumps over the lazy dog."
print(is_pangram(sentence))  # Output: True
