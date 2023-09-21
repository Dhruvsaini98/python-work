str = input("Enter a string: ")
vowels = "aeiou"
v_n = 0
c_n = 0
for vowel in str:
    if vowel.lower() in vowels:
        v_n += 1
    elif vowel.isalpha():
        c_n += 1

print(f"Vowel count: {v_n}, Consonant count: {c_n}")