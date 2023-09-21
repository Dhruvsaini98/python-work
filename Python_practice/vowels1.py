def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Example usage
user_input = input("Enter a string: ")
result = count_vowels(user_input)
print("Number of vowels:", result)
