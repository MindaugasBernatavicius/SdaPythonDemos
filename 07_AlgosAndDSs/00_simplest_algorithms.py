# max
# numbers = [5, 9, 10, 100, 2] # input
# numbers = [-5, -9, -10, -100, -2]
#
# curr_max = 0
# for number in numbers:
#     if(number > curr_max):
#         curr_max = number
#
# print(curr_max) # output


# # ...
# numbers = [-5, -9, -10, -100, -2]
#
# # could throw exception or smth.
# curr_max = numbers[0] if len(numbers) > 0 else 0
# # ... small optimization of we use numbers[0] as a starting point
# for i in range(1, len(numbers)):
#     if(numbers[i] > curr_max):
#         curr_max = numbers[i]
#
# print(curr_max) # output


# min
# numbers = [-5, -9, -10, -100, -2]
#
# # could throw exception or smth.
# curr_max = numbers[0] if len(numbers) > 0 else 0
# # ... small optimization of we use numbers[0] as a starting point
# for i in range(1, len(numbers)):
#     if(numbers[i] < curr_max):
#         curr_max = numbers[i]
#
# print(curr_max) # output

# swap
# a = 5
# b = 2
# print(f"a: {a}, b: {b}")
# tmp = a
# a = b
# b = tmp
# print(f"a: {a}, b: {b}")

# swap as a function
# def swap(a, b):
#     tmp = a
#     a = b
#     b = tmp
#     return a, b

# def swap(a, b):
#     return b, a
#
# a = 5
# b = 2
# print(f"a: {a}, b: {b}")
# a, b = swap(a, b)
# print(f"a: {a}, b: {b}")

a = 5
b = 2
print(f"a: {a}, b: {b}")
a, b = b, a
print(f"a: {a}, b: {b}")
