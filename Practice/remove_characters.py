def remove_chars(str, chars):
    new_str = ""
    for s in str:
        if s.lower() not in chars:
            new_str = new_str + s.lower()
    return new_str

str = "My Name is Dhruv Saini"
chars = ["v", "n", "r", "m", "s"]
result = remove_chars(str, chars)
print(result)