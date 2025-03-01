def binary_to_decimal(binary_str):
    decimal_value = 0
    length = len(binary_str)

    # Iterate over each character in the binary string
    for i in range(length):
        # Get the digit (either '0' or '1')
        digit = binary_str[length - 1 - i]  # Start from the end of the string

        # If the digit is '1', add the corresponding power of 2 to the decimal value
        if digit == '1':
            decimal_value += 2 ** i  # Add 2 raised to the current power

    return decimal_value


print(binary_to_decimal("101"))
1011010011010100100011001
1011010011010100100011001

