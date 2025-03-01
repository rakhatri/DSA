dict1 = {'a': 1, 'b': 2}
dict2 =  {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

for (key, value) in dict2.items():
    dict1[key] = value
for (key, value) in dict3.items():
    dict1[key] = value
print(dict1)