# # def is_palindrome(s):
string1 = "A man a plan a canal Panama"
# string_list = []
# for char in string1.lower():
#     if char != " ":
#         string_list.append(char)
# print(string_list)
# string_rev_list = []
# i = 0
# for i in range(len(string_list)):
#     string_rev_list.append(string_list[len(string_list) - 1 - i])
# print(string_rev_list)
# if string_list == string_rev_list:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

string2 = ''.join(char.lower() for char in string1 if char.isalnum())
print(string2)
if string2 == string2[::-1]:
    print("P")
s = "programming"
dummy_string = ''
for char in s:
    if char not in dummy_string:
        dummy_string += char
print(dummy_string)


