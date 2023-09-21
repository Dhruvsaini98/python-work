from pathlib import Path

path = Path("Files and Exceptions/guests.txt")
contents = path.write_text("Dhruv")
print(contents)