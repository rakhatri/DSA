sentence = "the quick brown fox jumps over the lazy dog"

words = sentence.split()
dict = {}
word_count = 0
for elem in words:
    if elem in dict:
        dict[elem] += 1
    else:
        dict[elem] = 1
print(dict)