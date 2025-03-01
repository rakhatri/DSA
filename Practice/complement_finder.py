num_list = [2, 7, 3, 11]
sum_target = 9
output = []
complement_dict = {}

for i, num in enumerate(num_list):
    complement = sum_target - num
    print(i, num, complement)
    if complement in complement_dict:
        output.append(complement_dict[complement])
        output.append(i)
    complement_dict[num] = i
    print(complement_dict)

print(output)