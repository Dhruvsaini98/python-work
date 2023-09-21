def binary_to_decimal(binary):
    decimal = 0

    for position, bit in enumerate(reversed(binary)):
        decimal += (2 ** position) * int(bit)

    return decimal

binary = "1000111"
result = binary_to_decimal(binary)
print(result)
