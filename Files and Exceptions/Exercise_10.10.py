from pathlib import Path

path = Path("Files and Exceptions/GOT.txt")

try:
    content = path.read_text(encoding = 'utf-8')
except FileNotFoundError:
    print("File not found")
else:
    the = content.lower().count("the ")
    print(the)