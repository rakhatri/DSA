lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]

for elem in lst1:
    found = False
    for item in lst2:
        if item == elem:
            found = True
            break
    if not found:
        print("False")
print("True")