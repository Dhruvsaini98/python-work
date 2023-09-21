str = "My name is Dhruv Saini"
vowels = "aeiou"

for i in range(len(str)):
    if str[i].lower() in vowels:
        str = str[:i] + '-' + str[i+1:]
        break

print(str)
