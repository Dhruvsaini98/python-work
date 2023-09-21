def reve(string):
    reverse_string = string[::-1]
    return reverse_string

string = input("Enter any sentence: ")
reversed_string = reve(string)
print(reversed_string)