def filter_list(l):
    'return a new list with the strings filtered out'
    return [elem for elem in l if not isinstance(elem, str)]



print(filter_list([1,2,'a','b']))

# n = 'a'
# print(type(n))
# if isinstance(n, str):
#     print('yes')
