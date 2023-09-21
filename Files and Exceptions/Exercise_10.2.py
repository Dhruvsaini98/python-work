from pathlib import Path

path = Path("Files and Exceptions/learning_python.txt")
contents = path.read_text()
#contents = contents.rstrip()
content = contents.replace("Python", "Java")
print(content)