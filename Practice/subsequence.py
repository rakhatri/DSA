s = "abcde"
t = "ace"

i = 0
j = 0

while i < len(s) and j < len(t):
    if s[i] == t[j]:
        j += 1
    i += 1
if j == len(t):
    print("subsequence")
else:
    print("not")