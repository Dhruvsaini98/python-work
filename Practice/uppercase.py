str = "I enjoy doing python programming"
vowels = "aeiou"
new_str = ""
for vowel in str:
    if vowel in vowels:
        s = vowel.upper()
        new_str += s
    else:
        new_str += vowel
print(new_str)