from pathlib import Path

path = Path("Files and Exceptions/guest_list.txt")

while True:
    name = input("Enter your name for the guest list or enter 'done' when done with the names:")
    
    if name == "done":
        break
    else:
        
        path.write_text(f"{name}\n")
    
    
#path.write_text(f"{name}\n")