dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]

dummy_dict = {}
for dict in dicts:
    for key, value in dict.items():
        if key in dummy_dict:
            dummy_dict[key] += value
        else:
            dummy_dict[key] = value
print(dummy_dict)