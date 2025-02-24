new_list = [1, 2, 3]
result = new_list[0]
print(result)

if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        break

new_list.append(4)
new_list.insert(0, 5)
print(new_list)
new_list.remove(5)
print(new_list)
new_list.extend([7, 8, 9])
print(new_list)
