from pathlib import Path

path = Path("Files and Exceptions/learning_python.txt")
contents = path.read_text()
contents = contents.rstrip()
print(contents)
print("/n")
lines = contents.splitlines()
for line in lines:
    print(line)

print(len(lines))