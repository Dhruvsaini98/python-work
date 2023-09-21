def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned_string = ""
    for char in s:
        if char.isalnum():
            cleaned_string = cleaned_string + char.lower()

# cleaned_string = ''.join(char.lower() for char in s if char.isalnum()) List comprehension

    # Compare the cleaned string with its reverse
    print(cleaned_string == cleaned_string[::-1])

# Test cases
p = input("Enter a word or a sentence: ")
is_palindrome(p)
# is_palindrome("rA#Ce@car") # Output: True
# print(is_palindrome("123321"))    # Output: False
# print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
