def sum_of_digits(num):
    # Initialize a variable to store the sum of digits
    digit_sum = 0

    # Take the absolute value of the number to handle negative integers
    num = abs(num)

    # Loop through each digit in the number
    while num > 0:
        # Extract the last digit of the number
        digit = num % 10

        # Add the digit to the sum
        digit_sum += digit

        # Remove the last digit from the number
        num //= 10

    return digit_sum

# Test cases
print(sum_of_digits(16789))    # Output: 6 (1 + 2 + 3)
print(sum_of_digits(456789))  # Output: 39 (4 + 5 + 6 + 7 + 8 + 9)
print(sum_of_digits(-987))   # Output: 24 (9 + 8 + 7)
