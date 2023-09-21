while True:
    print("Enter two numbers, we will add them")
    try:
        f_number = int(input("First number: "))
        
    except ValueError:
        print("Please enter only a number\n")
    else:
        try:
            s_number = int(input("Second number: "))

        except ValueError:
            print("Please enter only a number\n")
        else:
            sum = f_number + s_number
            print(sum)
            break