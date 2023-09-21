or_list = []

while True:
    print("Enter a number to put in a list.")
    print("Enter 'done' when done entering the numbers")
    num = input()

    if num == 'done':
        break
        
    else:
        num = int(num)
        or_list.append(num)
print(f"Original list:\n\t{or_list}\n")

even_num = []
for e in or_list:
    if e % 2 == 0:
        even_num.append(e)

print(f"New list with even numbers:\n\t{even_num}")
    