def int_to_binary(n):

    if n == 0:
        return "0"

    binary_number = ""

    is_negative = n < 0
    if is_negative:
        n = -n

    while n > 0:
        rem = n % 2
        binary_number = str(rem) + binary_number
        n = n // 2
    if is_negative:
        binary_number = "-" + binary_number
    return binary_number

print(int_to_binary(23701785))