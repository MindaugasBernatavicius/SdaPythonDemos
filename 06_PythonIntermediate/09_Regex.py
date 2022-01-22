import re

# 0. RE Search
# print(re.search(r"[A-Z]la", "ala Ola Ela"))

# ... what happens when there is a match
my_str = "ala Ola Ela"
match = re.search(r"[A-Z]la", my_str)
print(match.span())
print(match.group())
print(my_str[match.span()[0]:match.span()[1]]) # same as group()

# ... what happens when there is no match
my_str = "ala Ola Ela"
match = re.search(r"Ala", my_str)
if match is not None:
    print(match.span()) # AttributeError: 'NoneType' object has no attribute 'span'

# 1. RE match
print(re.match(r"[A-Z]la", "ala Ola Ela")) # "[A-Za-z]la"

# ... lookup from specific part
my_str = "ala Ola Ela"
print(f">>> { my_str[0:5] }")
print(re.search(r"ala", my_str[0:5]))