def perfect_num(num):
    sum = 0
    for n in range(1,num // 2 + 1):  # The loop only iterates through the possible divisors up to half of the num (inclusive) 
                                     # since any number greater than num//2 cannot be a proper divisor of num. 
                                     # This optimization helps reduce the number of iterations in the loop, making the code more efficient.
        if num % n == 0:
            sum = sum + n
    return sum == num
num = int(input("Enter a number: "))

print(perfect_num(num))

