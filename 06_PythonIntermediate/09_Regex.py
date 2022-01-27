import re

# # 0. RE Search
# # print(re.search(r"[A-Z]la", "ala Ola Ela"))
#
# # ... what happens when there is a match
# my_str = "ala Ola Ela"
#
# # ... reading this regex: find anything between A-Z in the 1st position, l in 2nd and a in the 3rd
# match = re.search(r"[A-Z]la", my_str)
# print(match.span())
# print(match.group())
# print(my_str[match.span()[0]:match.span()[1]]) # same as group()
#
# # ... what happens when there is no match
# my_str = "ala Ola Ela"
# match = re.search(r"Ala", my_str)
# if match is not None:
#     print(match.span()) # AttributeError: 'NoneType' object has no attribute 'span'
#
# # 1. RE match
# print(re.match(r"[A-Z]la", "ala Ola Ela")) # "[A-Za-z]la"
#
# # ... lookup from specific part
# my_str = "ala Ola Ela"
# print(f">>> { my_str[0:5] }")
# print(re.search(r"ala", my_str[0:5]))


# 2. Fullmatch - match
print(re.fullmatch(r"[A-Z]la", "Ela"))
print(re.fullmatch(r"[A-Z]la", "aEla"))
print(re.fullmatch(r"[A-Z]la?", "Ela"))
print(re.fullmatch(r"[A-Z]la?", "El"))

# 3. Findall
print(re.findall(r"[A-Z]la", "Ola ala Ela"))
print(re.findall(r".la", "Ola ala Ela"))

# 4. Finditer
iter = re.finditer(r".la", "Ola ala Ela")
for elem in iter:
    print(elem)


# 5. Split
print(re.split(r",|\.", "apple,pear,grapes,carrot.cabbage,veggies.fruit,yard"))
print(re.split(r",|\.|;", "apple,pear;grapes,carrot.cabbage,veggies.fruit,yard"))

# 6. Sub (replace)
print(re.sub(r"[a-z]{8}", "dog", "Alice has elephant"))
print(re.sub(r"(?<=Alice has )\w+", "dog", "Alice has parrot"))
print(re.sub(r"(?<=Alice has )a? \w+", "elephant", "Alice has a parrot"))

# 7. Subn
print(re.subn(r"[a-z]{8}", "dog", "Alice has elephant"))
print(re.subn(r"(?<=Alice ha(?:s|d) )a? \w+", "elephant", "Alice has a parrot and Alice had a fish"))


# 8. Grouping
text = "Thomas W. (33), last seen in Krakow"
pattern = r"([A-Z]{1}[a-z]+ [A-Z]{1}\.) \((\d+)\)"
match = re.search(pattern, text)
print(match)
print(match.groups())
print(f"-----------")
print(match.group(0)) # first match
print(match.group(1))
print(match.group(2))

# text = "Thomas (33) i Eva (24) agreed to go shopping together tomorrow"
# pattern = r"([A-Z]{1}[a-z]+) \((\d+) l.\)"
# print(re.findall(pattern, text))