def vowel_count(sentence):
    v = 0
    vowels = 'aeiou'
    for vowel in sentence:
        vowel_lower = vowel.lower()
        if vowel_lower in vowels:
            v = v + 1
    return v

sentence = input("Enter a sentence: ")
v_c = vowel_count(sentence) 
print(f"Vowel count: {v_c}")

