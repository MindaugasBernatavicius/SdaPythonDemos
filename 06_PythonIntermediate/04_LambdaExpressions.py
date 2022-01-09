# 0. Elementary lambda
# def l(x):
#     return x.lower()

# l = lambda x: x.lower()
# # different syntax (what is written), same semantics (what is performed)
#
# print(l("HA HA HA"))  # "ha ha ha"
# print(l("CHA CHA CHA"))
# print(l("BLAH BLAH BLAH"))
#
# # print(l(1))
# # print(l("BLAH BLAH BLAH", "A"))
#
# cube_lambda = lambda x: x ** 3
# print(cube_lambda(4))  # 64
#
# # multiple params
# check_if_equals = lambda x, y: x == y
# print(check_if_equals(1, 2))  # False
#
# # no arguments, only print (still returns None)
# lambda_that_only_prints = lambda: print(">>>")
# lambda_that_only_prints()
#
# # default arguments
# multiply = lambda x=5, y=2: x*y
# print(multiply())


# 1. Lambda usage with map, filter, reduce
# def get_vowels(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#
# sequence = "My name is Jonas"
# print("Original: " + sequence)
# # filter for vowels - return vowels that are in the sentence
# filtered = filter(get_vowels, sequence)
# print("Filtered: " + str(list(filtered)))

sequence = "My name is Jonas"
print("Original: " + sequence)
filtered = filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], sequence)
print("Filtered: " + str(list(filtered)))

items = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 != 0, items))) # odd numbers
print(list(filter(lambda x: x % 2 == 0, items))) # even numbers

print(list(map(lambda x: x ** 2, items)))

from functools import reduce
print(reduce(lambda x, y: x + y, items)) # sum reduction
print(reduce(lambda x, y: x * y, items))

print(reduce(lambda a, b: a if a > b else b, items)) # max reduction
print(reduce(lambda a, b: a if a < b else b, items)) # min reduction

# sorting more complex lists
pairs = [(2, 2), (3, 8), (2, 9), (1, 10)]

# pairs.sort()
# print(pairs)
# print(sorted(pairs, key=lambda x: x[1])) # increasing order
print(sorted(pairs, key=lambda x: x[1], reverse=True)) # decreasing order
print(sorted(pairs, key=lambda x: x[0] * x[1], reverse=True)) # decreasing order

print(min(pairs))  # (1, 10)
print(min(pairs, key=lambda x: x[1]))  # (3, 8)
print(max(pairs, key=lambda x: x[0] + x[1])) # will return first max if the are dublicates

# Exercise: naudodamiesi lambda išraiškomis sukurkite sąrašą, kuriame bus skaičiai, reprezentuojantys ilgius sakinių, laikomų kitame liste (hint: panaudoti kažkurį iš map/filter/reduce metodų)