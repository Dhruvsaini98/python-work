filename = 'python_notes.txt'
new_file_prefix = filename.removeprefix('python_')   #Removed prefix of the string using removeprefix() method
new_file_suffix = filename.removesuffix('.txt')      #Removed suffix of the string using removesuffix() method
print(f"{new_file_prefix}\n{new_file_suffix}")       #Used f string to format the string and printed using print() function