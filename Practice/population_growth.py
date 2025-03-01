# def nb_year(p0, percent, aug, p):
#     # your code
#     year = 0
#     while p0 < p:
#         p0 = p0 + int(p0 * (percent / 100)) + aug
#         year += 1
#     return year
#
#
# print(nb_year(1500, 5, 100, 5000))
#
# print(set("Hello"))


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


print(find_uniq([2, 1, 1, 1, 1, 1, 1 ]))

