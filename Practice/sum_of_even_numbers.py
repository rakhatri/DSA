n = 50
total_sum = 0
current_even_number = 2

# Loop through the first n even numbers and add them to total_sum
for i in range(n):
    total_sum += current_even_number
    current_even_number += 2  # Increment by 2 to get the next even number

print(total_sum)