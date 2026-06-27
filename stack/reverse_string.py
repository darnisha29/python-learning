from collections import deque

stack = deque()
# string = input("Enter a string: ")

# for char in string:
#     stack.append(char)

# reverse_string = "" 
# while stack:
#     reverse_string += stack.pop()
# print("Reversed string :: ",reverse_string)


def reverse_string(s):
    rev_string = ""
    for char in s:
        stack.append(char)
    while stack:
        rev_string += stack.pop()
    return rev_string

print("Reversed String :: ", reverse_string("We will conquere COVID-19"))