
def is_prime(num):
    # Handle special cases for 1 and 2
    if num <= 1:
        return False
    elif num == 2:
        return True

    # Check if the number is divisible by any integer from 2 up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

# Test cases
print(is_prime(7))   # Output: True
print(is_prime(15))  # Output: False
print(is_prime(1))   # Output: False
print(is_prime(23))  # Output: True
