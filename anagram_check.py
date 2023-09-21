def are_anagrams(str1, str2):
    # Convert both strings to lowercase to perform a case-insensitive comparison
    str1_lower = str1.lower()
    str2_lower = str2.lower()

    # Sort both strings and compare the sorted versions
    sorted_str1 = sorted(str1_lower)
    sorted_str2 = sorted(str2_lower)

    # Check if the sorted versions are equal
    return sorted_str1 == sorted_str2

# Test cases
string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2))  # Output: True

string3 = "Race"
string4 = "care"
print(are_anagrams(string3, string4))  # Output: True
