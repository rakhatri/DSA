def generate_square(n):
    string_array = []
    for num in range(n):
        string_array.append('*' * n)
    return string_array

print(generate_square(5))