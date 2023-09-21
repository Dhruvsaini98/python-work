def even_odd(num):
    num1 = int(num)
    if num1 % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

n = input("Enter a number: ")
even_odd(n)