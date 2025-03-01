tup = (1, 2, 3, 2, 1, 2)

i = 0
j = len(tup) - 1
while i < len(tup):
    if tup[i] != tup[j]:
        print("False")
    else:
        print("True")
    i += 1
    j -= 1