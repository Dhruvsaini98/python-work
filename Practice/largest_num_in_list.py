def num():
    list = []
    while True:
        print("Enter a number to put in a list.")
        print("Enter 'done' when done entering the numbers")
        num = input()

        if num == 'done':
            break       
        else:
            try:
                num = int(num)

            except ValueError:
                print("Enter a valid number\n")
            else:    
                list.append(num)
    return list

def largest(num_list):
    try:
        print(f"Largest number is {max(num_list)}")
    except ValueError:
        print("There is no number in the list")
        

num_list = num()
largest(num_list)