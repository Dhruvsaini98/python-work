from pathlib import Path

path = Path("Files and Exceptions/Cats.txt")
path1 = Path("Files and Exceptions/Dogs.txt")

try:
    contents = path.read_text(encoding = 'utf-8')
    contents1 = path1.read_text(encoding = 'utf-8')

except FileNotFoundError:
    pass

else:
    print(contents)
    print(contents1)