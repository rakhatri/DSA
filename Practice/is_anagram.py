s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print("F")
if sorted(s.lower()) == sorted(t.lower()):
    print("T")
else:
    print("F")

# def is_anagram(s, t):
#     if len(s) != len(t):
#         return False
#
#         # Create two arrays to count character frequencies for both strings
#     char_count_s = [0] * 26  # Assuming lowercase a-z characters
#     char_count_t = [0] * 26  # Assuming lowercase a-z characters
#     print(char_count_s)
#     # Loop through the characters in the first string (s) and count occurrences
#     for char in s:
#         char_count_s[ord(char) - ord('a')] += 1
#         print(char_count_s[ord(char) - ord('a')])
#     print(char_count_s)
#     # Loop through the characters in the second string (t) and count occurrences
#     for char in t:
#         char_count_t[ord(char) - ord('a')] += 1
#
#     # Compare the character frequency arrays for both strings
#     for i in range(26):
#         if char_count_s[i] != char_count_t[i]:
#             return False  # If there is a mismatch in frequencies, return False
#
#     return True
#
# print(is_anagram("anagram", "nagaram"))