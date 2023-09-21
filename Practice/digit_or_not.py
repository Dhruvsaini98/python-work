char = input("Enter a character: ")
# Exception handing
try:
    char1 = int(char)
except ValueError:
    print("Given character is not a digit")
else:
    print("Given character is a digit")

# isdigit() method
if char.isdigit():
    print("Digit")
else:
    print("Not a digit")